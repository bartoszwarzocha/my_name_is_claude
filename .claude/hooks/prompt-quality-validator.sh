#!/bin/bash

# Prompt Quality Validator Hook
# Validates quality of newly created or modified prompts
# Checks structure, completeness, examples, and formatting

PROMPT_FILE="${1:-}"
VALIDATION_MODE="${2:-comprehensive}"

echo "📝 Prompt Quality Validator Hook - Validating prompt quality..."

EXIT_CODE=0

if [[ -z "$PROMPT_FILE" ]]; then
    echo "🔍 No specific file provided - validating all prompts..."
    PROMPT_FILES=($(find .claude/prompts/agents -name "*.md" 2>/dev/null))
else
    if [[ ! -f "$PROMPT_FILE" ]]; then
        echo "❌ Prompt file not found: $PROMPT_FILE"
        exit 1
    fi
    PROMPT_FILES=("$PROMPT_FILE")
fi

# Quality check functions
check_markdown_structure() {
    local file="$1"
    echo "  🔍 Checking markdown structure..."
    
    # Check for required headers
    REQUIRED_HEADERS=("# " "## Mission" "## Process" "## Deliverables")
    for header in "${REQUIRED_HEADERS[@]}"; do
        if ! grep -q "^$header" "$file"; then
            echo "    ❌ Missing required header: $header"
            EXIT_CODE=1
        fi
    done
    
    # Check for proper markdown formatting
    if grep -q "^[^#].*:$" "$file"; then
        echo "    ⚠️  Potential heading formatting issues (missing #)"
    fi
}

check_content_completeness() {
    local file="$1"
    echo "  📋 Checking content completeness..."
    
    # Check minimum content length
    WORD_COUNT=$(wc -w < "$file")
    if [[ $WORD_COUNT -lt 500 ]]; then
        echo "    ⚠️  Prompt may be too short ($WORD_COUNT words) - consider adding more detail"
    fi
    
    # Check for examples or templates
    if ! grep -q -i -E "(example|template|sample|```)" "$file"; then
        echo "    ⚠️  No examples or code blocks found - consider adding practical examples"
    fi
    
    # Check for collaboration points
    if ! grep -q -i -E "(coordinate|collaborate|handoff|align)" "$file"; then
        echo "    ⚠️  No collaboration points found - consider adding multi-agent coordination guidance"
    fi
}

check_technical_accuracy() {
    local file="$1"
    echo "  🔧 Checking technical accuracy..."
    
    # Check for agent-specific technical requirements
    AGENT_TYPE=$(basename "$(dirname "$file")")
    
    case "$AGENT_TYPE" in
        "frontend")
            if ! grep -q -i -E "(typescript|angular|react|css|javascript|accessibility)" "$file"; then
                echo "    ⚠️  Frontend prompt missing key technology references"
            fi
            ;;
        "security")
            if ! grep -q -i -E "(threat|vulnerability|compliance|encryption|authentication)" "$file"; then
                echo "    ⚠️  Security prompt missing key security concepts"
            fi
            ;;
        "api")
            if ! grep -q -i -E "(rest|graphql|api|endpoint|swagger|openapi)" "$file"; then
                echo "    ⚠️  API prompt missing key API concepts"
            fi
            ;;
        "business")
            if ! grep -q -i -E "(requirement|stakeholder|process|analysis|business case)" "$file"; then
                echo "    ⚠️  Business prompt missing key business concepts"
            fi
            ;;
    esac
}

check_formatting_standards() {
    local file="$1"
    echo "  📐 Checking formatting standards..."
    
    # Check for consistent bullet points
    MIXED_BULLETS=$(grep -c -E "^[[:space:]]*[-*+]" "$file")
    if [[ $MIXED_BULLETS -gt 0 ]]; then
        DASH_BULLETS=$(grep -c -E "^[[:space:]]*-" "$file")
        STAR_BULLETS=$(grep -c -E "^[[:space:]]*\*" "$file")
        if [[ $DASH_BULLETS -gt 0 ]] && [[ $STAR_BULLETS -gt 0 ]]; then
            echo "    ⚠️  Mixed bullet point styles detected - consider standardizing"
        fi
    fi
    
    # Check for proper code block formatting
    CODE_BLOCKS=$(grep -c "^```" "$file")
    if [[ $((CODE_BLOCKS % 2)) -ne 0 ]]; then
        echo "    ❌ Unmatched code blocks detected"
        EXIT_CODE=1
    fi
    
    # Check for proper heading hierarchy
    if grep -q "^####" "$file" && ! grep -q "^###" "$file"; then
        echo "    ⚠️  Heading hierarchy may be incorrect (h4 without h3)"
    fi
}

validate_deliverables_section() {
    local file="$1"
    echo "  📦 Validating deliverables section..."
    
    if grep -q "## Deliverables" "$file"; then
        # Check if deliverables section has actual content
        DELIVERABLES_CONTENT=$(awk '/^## Deliverables/,/^## / {print}' "$file" | wc -w)
        if [[ $DELIVERABLES_CONTENT -lt 50 ]]; then
            echo "    ⚠️  Deliverables section may be too brief"
        fi
        
        # Check for specific deliverable types
        if ! grep -A 10 "## Deliverables" "$file" | grep -q -E "(.md|.json|.yml|.ts|.js|.py|documentation|report|analysis)"; then
            echo "    ⚠️  No specific file types or deliverable formats mentioned"
        fi
    else
        echo "    ❌ Missing Deliverables section"
        EXIT_CODE=1
    fi
}

# Main validation loop
mkdir -p work/quality-reports

TOTAL_FILES=${#PROMPT_FILES[@]}
echo "📊 Validating $TOTAL_FILES prompt file(s)..."

for prompt_file in "${PROMPT_FILES[@]}"; do
    echo ""
    echo "📄 Validating: $prompt_file"
    
    # Create individual quality report
    REPORT_FILE="work/quality-reports/$(basename "$prompt_file" .md)_quality_report.txt"
    
    {
        echo "Prompt Quality Report"
        echo "===================="
        echo "File: $prompt_file"
        echo "Date: $(date)"
        echo "Validation Mode: $validation_mode"
        echo ""
    } > "$REPORT_FILE"
    
    # Run all checks
    check_markdown_structure "$prompt_file" | tee -a "$REPORT_FILE"
    
    if [[ "$validation_mode" == "comprehensive" ]]; then
        check_content_completeness "$prompt_file" | tee -a "$REPORT_FILE"
        check_technical_accuracy "$prompt_file" | tee -a "$REPORT_FILE"
        check_formatting_standards "$prompt_file" | tee -a "$REPORT_FILE"
        validate_deliverables_section "$prompt_file" | tee -a "$REPORT_FILE"
    fi
    
    # Add score
    ISSUES_COUNT=$(grep -c -E "(❌|⚠️)" "$REPORT_FILE")
    if [[ $ISSUES_COUNT -eq 0 ]]; then
        echo "  ✅ Quality Score: EXCELLENT (0 issues)" | tee -a "$REPORT_FILE"
    elif [[ $ISSUES_COUNT -le 2 ]]; then
        echo "  🟡 Quality Score: GOOD ($ISSUES_COUNT minor issues)" | tee -a "$REPORT_FILE"
    elif [[ $ISSUES_COUNT -le 5 ]]; then
        echo "  🟠 Quality Score: FAIR ($ISSUES_COUNT issues)" | tee -a "$REPORT_FILE"
    else
        echo "  🔴 Quality Score: NEEDS IMPROVEMENT ($ISSUES_COUNT issues)" | tee -a "$REPORT_FILE"
        EXIT_CODE=1
    fi
done

# Generate summary report
SUMMARY_FILE="work/quality-reports/summary_$(date +%Y%m%d_%H%M%S).md"

cat > "$SUMMARY_FILE" << EOF
# Prompt Quality Summary Report

**Generated:** $(date)
**Files Validated:** $TOTAL_FILES
**Validation Mode:** $validation_mode

## Results Overview

$(
for prompt_file in "${PROMPT_FILES[@]}"; do
    REPORT_FILE="work/quality-reports/$(basename "$prompt_file" .md)_quality_report.txt"
    if [[ -f "$REPORT_FILE" ]]; then
        SCORE_LINE=$(grep "Quality Score:" "$REPORT_FILE")
        echo "- **$(basename "$prompt_file"):** $SCORE_LINE"
    fi
done
)

## Recommendations

### High Priority
- Fix all ❌ critical issues
- Address structural problems first
- Ensure all required sections are present

### Medium Priority  
- Resolve ⚠️ warning issues
- Improve content completeness
- Add practical examples and templates

### Low Priority
- Standardize formatting consistency
- Enhance collaboration guidance
- Add domain-specific technical details

## Quality Metrics

- **Critical Issues (❌):** $(find work/quality-reports -name "*_quality_report.txt" -exec grep -l "❌" {} \; | wc -l)
- **Warning Issues (⚠️):** $(find work/quality-reports -name "*_quality_report.txt" -exec grep -l "⚠️" {} \; | wc -l)
- **Excellent Prompts:** $(find work/quality-reports -name "*_quality_report.txt" -exec grep -l "EXCELLENT" {} \; | wc -l)

EOF

echo ""
echo "📊 Quality validation completed!"
echo "📁 Individual reports: work/quality-reports/"
echo "📋 Summary report: $SUMMARY_FILE"

# Log validation activity
echo "$(date): Prompt quality validation completed - $TOTAL_FILES files, exit code: $EXIT_CODE" >> work/quality-validation.log

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ All prompts meet quality standards"
else
    echo "❌ Some prompts need improvement - review quality reports"
fi

echo "📝 Prompt Quality Validator Hook completed"
exit $EXIT_CODE