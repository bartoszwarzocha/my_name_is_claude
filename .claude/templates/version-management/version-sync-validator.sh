#!/bin/bash

# Claude Code Framework - Version Synchronization Validator
# Validates that all version references across the framework are synchronized

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "🔍 Claude Code Framework - Version Synchronization Validator"
echo "=============================================================="
echo ""

# Initialize variables
ERRORS=0
WARNINGS=0
declare -A VERSIONS
declare -A FILES_CHECKED

# Function to extract version from file
extract_version() {
    local file="$1"
    local pattern="$2"
    local description="$3"

    if [[ ! -f "$file" ]]; then
        echo -e "${RED}❌ MISSING: $file${NC}"
        ((ERRORS++))
        return 1
    fi

    local version=$(grep -oP "$pattern" "$file" 2>/dev/null | head -n1)
    if [[ -z "$version" ]]; then
        echo -e "${RED}❌ NOT FOUND: $description in $file${NC}"
        ((ERRORS++))
        return 1
    fi

    VERSIONS["$description"]="$version"
    FILES_CHECKED["$file"]=1
    echo -e "${BLUE}📄 $file: $description = $version${NC}"
    return 0
}

# Function to validate semantic version format
validate_version_format() {
    local version="$1"
    if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo -e "${YELLOW}⚠️  WARNING: Version '$version' doesn't follow semantic versioning (X.Y.Z)${NC}"
        ((WARNINGS++))
        return 1
    fi
    return 0
}

echo "🔍 Extracting versions from framework files..."
echo ""

# Extract versions from different files
extract_version "README.md" 'Version-\K[0-9]+\.[0-9]+\.[0-9]+' "README Badge"
extract_version "README.md" 'Current Version:\*\* \K[0-9]+\.[0-9]+\.[0-9]+' "README Current Version"
extract_version "CLAUDE.md" '"project_version": "\K[0-9]+\.[0-9]+\.[0-9]+' "CLAUDE.md Project Version"

# Check docs/README.md if it exists
if [[ -f "docs/README.md" ]]; then
    # Look for any version pattern in docs
    docs_version=$(grep -oP 'Version[: ]*\K[0-9]+\.[0-9]+\.[0-9]+' "docs/README.md" 2>/dev/null | head -n1 || true)
    if [[ -n "$docs_version" ]]; then
        VERSIONS["docs/README.md"]="$docs_version"
        FILES_CHECKED["docs/README.md"]=1
        echo -e "${BLUE}📄 docs/README.md: Version = $docs_version${NC}"
    else
        echo -e "${GREEN}✅ docs/README.md: No version references found (OK)${NC}"
    fi
fi

# Extract latest version from CHANGELOG.md
if [[ -f "CHANGELOG.md" ]]; then
    changelog_version=$(grep -oP '## \[\K[0-9]+\.[0-9]+\.[0-9]+' "CHANGELOG.md" 2>/dev/null | head -n1 || true)
    if [[ -n "$changelog_version" ]]; then
        VERSIONS["CHANGELOG Latest"]="$changelog_version"
        FILES_CHECKED["CHANGELOG.md"]=1
        echo -e "${BLUE}📄 CHANGELOG.md: Latest Version = $changelog_version${NC}"
    else
        echo -e "${YELLOW}⚠️  WARNING: No version entries found in CHANGELOG.md${NC}"
        ((WARNINGS++))
    fi
fi

echo ""
echo "🔍 Version Analysis..."
echo ""

# Check if all versions are the same
unique_versions=($(printf '%s\n' "${VERSIONS[@]}" | sort -u))

if [[ ${#unique_versions[@]} -eq 0 ]]; then
    echo -e "${RED}❌ CRITICAL: No versions found in any file!${NC}"
    ((ERRORS++))
elif [[ ${#unique_versions[@]} -eq 1 ]]; then
    version="${unique_versions[0]}"
    echo -e "${GREEN}✅ SUCCESS: All versions synchronized to $version${NC}"

    # Validate semantic versioning format
    validate_version_format "$version"

    echo ""
    echo "📋 Version Summary:"
    for desc in "${!VERSIONS[@]}"; do
        echo -e "   ${GREEN}✓${NC} $desc: ${VERSIONS[$desc]}"
    done
else
    echo -e "${RED}❌ ERROR: Version mismatch detected!${NC}"
    ((ERRORS++))
    echo ""
    echo "📋 Version Conflicts:"
    for desc in "${!VERSIONS[@]}"; do
        echo -e "   ${RED}✗${NC} $desc: ${VERSIONS[$desc]}"
    done
    echo ""
    echo -e "${YELLOW}💡 Action Required:${NC}"
    echo "   1. Choose the correct version number"
    echo "   2. Update all files to use the same version"
    echo "   3. Use .claude/templates/version-management/version-update-checklist.md"
fi

echo ""
echo "📁 Files Checked:"
for file in "${!FILES_CHECKED[@]}"; do
    echo -e "   ${GREEN}✓${NC} $file"
done

# Check for potential missed files
echo ""
echo "🔍 Scanning for additional version references..."

# Search for version patterns in other common files
additional_files=(
    "package.json"
    "composer.json"
    "pyproject.toml"
    "Cargo.toml"
    "VERSION"
    ".version"
)

found_additional=0
for file in "${additional_files[@]}"; do
    if [[ -f "$file" ]] && [[ -z "${FILES_CHECKED[$file]}" ]]; then
        version_found=$(grep -i "version" "$file" 2>/dev/null | head -n3 || true)
        if [[ -n "$version_found" ]]; then
            echo -e "${YELLOW}⚠️  Found version references in $file:${NC}"
            echo "$version_found" | sed 's/^/   /'
            ((found_additional++))
        fi
    fi
done

if [[ $found_additional -eq 0 ]]; then
    echo -e "${GREEN}✅ No additional version files found${NC}"
fi

echo ""
echo "📊 Validation Summary:"
echo "======================"

if [[ $ERRORS -eq 0 ]] && [[ $WARNINGS -eq 0 ]]; then
    echo -e "${GREEN}🎉 PERFECT: All versions synchronized, no issues found!${NC}"
    exit 0
elif [[ $ERRORS -eq 0 ]]; then
    echo -e "${YELLOW}⚠️  SUCCESS with WARNINGS: $WARNINGS warning(s) found${NC}"
    echo "   Consider addressing warnings for better consistency"
    exit 0
else
    echo -e "${RED}❌ FAILED: $ERRORS error(s) and $WARNINGS warning(s) found${NC}"
    echo ""
    echo -e "${YELLOW}🔧 Next Steps:${NC}"
    echo "   1. Review the errors above"
    echo "   2. Use: .claude/templates/version-management/version-update-checklist.md"
    echo "   3. Fix all version mismatches"
    echo "   4. Run this validator again"
    exit 1
fi