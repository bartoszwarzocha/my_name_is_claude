# Desktop Application Deployment and Packaging

## Mission
Create comprehensive deployment and packaging solutions for desktop applications, adapting to the technology stack and target platforms specified in CLAUDE.md. Implement cross-platform distribution, auto-update mechanisms, and professional installation packages.

## Pre-Implementation Analysis

### Step 1: Technology and Platform Detection
**CRITICAL: Always analyze CLAUDE.md first to determine technology stack and target platforms:**
```bash
# Read project configuration
cat CLAUDE.md | grep -A 5 "primary_language\|Desktop\|deployment\|platform"
```

**Platform-specific analysis:**
```bash
# Check target platforms
uname -a
echo "Current platform: $(uname -s)"

# Windows deployment tools
where innosetup 2>/dev/null || echo "Inno Setup not found"
where "C:\Program Files (x86)\NSIS\makensis.exe" 2>/dev/null || echo "NSIS not found"

# macOS deployment tools  
which pkgbuild 2>/dev/null || echo "pkgbuild not found"
which create-dmg 2>/dev/null || echo "create-dmg not found"

# Linux deployment tools
which dpkg-deb 2>/dev/null || echo "dpkg-deb not found"
which rpmbuild 2>/dev/null || echo "rpmbuild not found"
which appimage-builder 2>/dev/null || echo "appimage-builder not found"
```

### Step 2: Application Technology Analysis
```bash
# Python applications
find . -name "*.py" -o -name "requirements.txt" -o -name "setup.py" | head -5
ls -la dist/ build/ *.spec 2>/dev/null

# C++ applications
find . -name "*.cpp" -o -name "CMakeLists.txt" -o -name "Makefile" | head -5
ls -la bin/ Release/ Debug/ 2>/dev/null

# .NET applications
find . -name "*.csproj" -o -name "*.sln" | head -5
ls -la bin/Release/ bin/Debug/ publish/ 2>/dev/null

# Electron applications
find . -name "package.json" -o -name "electron-builder.yml" | head -5
ls -la dist/ out/ 2>/dev/null
```

## Technology-Specific Deployment Solutions

**⚠️ IMPORTANT: Select deployment approach based on CLAUDE.md technology and platform specification**

### Python Desktop Application Deployment

**Use when CLAUDE.md specifies: Python, wxPython, desktop**

```python
# build_scripts/build_config.py - Build configuration management
import os
import sys
import platform
import json
from pathlib import Path
from typing import Dict, List, Optional

class BuildConfig:
    def __init__(self, config_file: str = "build_config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
        self.platform = platform.system().lower()
        
    def _load_config(self) -> Dict:
        """Load build configuration from file"""
        default_config = {
            "app_name": "Desktop Application",
            "app_version": "1.0.0",
            "app_author": "Your Company",
            "app_description": "Desktop application built with Python",
            "app_icon": "assets/icon.ico",
            "main_script": "main.py",
            "hidden_imports": [
                "wx", "sqlite3", "logging", "json", "threading"
            ],
            "data_files": [
                ("assets", "assets/*"),
                ("config", "config/*"),
                ("data", "data/*.sql")
            ],
            "exclude_modules": [
                "tkinter", "test", "unittest", "pdb", "pydoc"
            ],
            "target_platforms": ["windows", "linux", "macos"],
            "signing": {
                "enabled": False,
                "certificate_path": "",
                "certificate_password": ""
            },
            "auto_update": {
                "enabled": True,
                "update_server": "https://your-server.com/updates",
                "check_interval": 3600
            }
        }
        
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        else:
            # Create default config
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def get_pyinstaller_spec(self) -> str:
        """Generate PyInstaller spec file content"""
        hidden_imports = ", ".join([f"'{imp}'" for imp in self.config["hidden_imports"]])
        datas = []
        
        for data_folder, pattern in self.config["data_files"]:
            datas.append(f"('{pattern}', '{data_folder}')")
        
        datas_str = ", ".join(datas)
        
        spec_content = f'''# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path

block_cipher = None

a = Analysis(
    ['{self.config["main_script"]}'],
    pathex=[],
    binaries=[],
    datas=[{datas_str}],
    hiddenimports=[{hidden_imports}],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes={self.config["exclude_modules"]},
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{self.config["app_name"].replace(" ", "_")}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='{self.config["app_icon"]}',
    version='version_info.py'
)
'''
        return spec_content
    
    def get_version_info(self) -> str:
        """Generate Windows version info file"""
        if self.platform != "windows":
            return ""
        
        version_parts = self.config["app_version"].split(".")
        while len(version_parts) < 4:
            version_parts.append("0")
        
        version_tuple = ", ".join(version_parts)
        
        return f'''VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({version_tuple}),
    prodvers=({version_tuple}),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [StringStruct(u'CompanyName', u'{self.config["app_author"]}'),
           StringStruct(u'FileDescription', u'{self.config["app_description"]}'),
           StringStruct(u'FileVersion', u'{self.config["app_version"]}'),
           StringStruct(u'InternalName', u'{self.config["app_name"]}'),
           StringStruct(u'LegalCopyright', u'© {self.config["app_author"]}'),
           StringStruct(u'OriginalFilename', u'{self.config["app_name"].replace(" ", "_")}.exe'),
           StringStruct(u'ProductName', u'{self.config["app_name"]}'),
           StringStruct(u'ProductVersion', u'{self.config["app_version"]}')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)'''
```

```python
# build_scripts/builder.py - Cross-platform build system
import subprocess
import shutil
import zipfile
from pathlib import Path
from build_config import BuildConfig
import logging

class DesktopAppBuilder:
    def __init__(self, config: BuildConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.dist_dir = Path("dist")
        self.build_dir = Path("build")
        
    def clean_build(self):
        """Clean previous build artifacts"""
        if self.dist_dir.exists():
            shutil.rmtree(self.dist_dir)
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
        
        # Remove PyInstaller files
        for pattern in ["*.spec", "version_info.py"]:
            for file in Path(".").glob(pattern):
                file.unlink(missing_ok=True)
    
    def build_executable(self) -> bool:
        """Build executable using PyInstaller"""
        try:
            # Create spec file
            spec_content = self.config.get_pyinstaller_spec()
            with open("app.spec", "w") as f:
                f.write(spec_content)
            
            # Create version info for Windows
            if self.config.platform == "windows":
                version_content = self.config.get_version_info()
                with open("version_info.py", "w") as f:
                    f.write(version_content)
            
            # Run PyInstaller
            cmd = [
                "pyinstaller",
                "--clean",
                "--noconfirm",
                "app.spec"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                self.logger.error(f"PyInstaller failed: {result.stderr}")
                return False
            
            self.logger.info("Executable built successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Build failed: {e}")
            return False
    
    def create_windows_installer(self) -> bool:
        """Create Windows installer using Inno Setup"""
        if self.config.platform != "windows":
            return True
        
        iss_content = self._get_inno_setup_script()
        iss_file = Path("installer.iss")
        
        with open(iss_file, "w") as f:
            f.write(iss_content)
        
        try:
            # Try to find Inno Setup
            inno_paths = [
                "C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe",
                "C:\\Program Files\\Inno Setup 6\\ISCC.exe",
                "iscc.exe"  # If in PATH
            ]
            
            inno_exe = None
            for path in inno_paths:
                if Path(path).exists() or shutil.which(path):
                    inno_exe = path
                    break
            
            if not inno_exe:
                self.logger.warning("Inno Setup not found, skipping installer creation")
                return False
            
            result = subprocess.run([inno_exe, str(iss_file)], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("Windows installer created successfully")
                return True
            else:
                self.logger.error(f"Inno Setup failed: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Installer creation failed: {e}")
            return False
    
    def _get_inno_setup_script(self) -> str:
        """Generate Inno Setup script"""
        app_name = self.config.config["app_name"]
        app_version = self.config.config["app_version"]
        app_author = self.config.config["app_author"]
        
        return f'''[Setup]
AppName={app_name}
AppVersion={app_version}
AppPublisher={app_author}
DefaultDirName={{autopf}}\\{app_name}
DefaultGroupName={app_name}
OutputDir=dist\\installer
OutputBaseFilename={app_name.replace(" ", "_")}_Setup_{app_version}
Compression=lzma
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
SetupIconFile={self.config.config["app_icon"]}
UninstallDisplayIcon={{app}}\\{app_name.replace(" ", "_")}.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{{cm:CreateQuickLaunchIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked; OnlyBelowVersion: 6.1

[Files]
Source: "dist\\{app_name.replace(" ", "_")}\\*"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{{group}}\\{app_name}"; Filename: "{{app}}\\{app_name.replace(" ", "_")}.exe"
Name: "{{autodesktop}}\\{app_name}"; Filename: "{{app}}\\{app_name.replace(" ", "_")}.exe"; Tasks: desktopicon
Name: "{{userappdata}}\\Microsoft\\Internet Explorer\\Quick Launch\\{app_name}"; Filename: "{{app}}\\{app_name.replace(" ", "_")}.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{{app}}\\{app_name.replace(" ", "_")}.exe"; Description: "{{cm:LaunchProgram,{app_name}}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{{app}}"
'''
    
    def create_macos_bundle(self) -> bool:
        """Create macOS application bundle"""
        if self.config.platform != "darwin":
            return True
        
        app_name = self.config.config["app_name"]
        app_bundle = Path(f"dist/{app_name}.app")
        
        try:
            # Create bundle structure
            contents_dir = app_bundle / "Contents"
            macos_dir = contents_dir / "MacOS"
            resources_dir = contents_dir / "Resources"
            
            for dir_path in [contents_dir, macos_dir, resources_dir]:
                dir_path.mkdir(parents=True, exist_ok=True)
            
            # Copy executable
            exe_src = Path(f"dist/{app_name.replace(' ', '_')}")
            exe_dst = macos_dir / app_name.replace(' ', '_')
            shutil.copy2(exe_src, exe_dst)
            exe_dst.chmod(0o755)
            
            # Create Info.plist
            plist_content = self._get_macos_plist()
            with open(contents_dir / "Info.plist", "w") as f:
                f.write(plist_content)
            
            # Copy icon if available
            icon_path = Path(self.config.config["app_icon"])
            if icon_path.exists() and icon_path.suffix.lower() == '.icns':
                shutil.copy2(icon_path, resources_dir / "icon.icns")
            
            self.logger.info("macOS bundle created successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"macOS bundle creation failed: {e}")
            return False
    
    def _get_macos_plist(self) -> str:
        """Generate macOS Info.plist"""
        app_name = self.config.config["app_name"]
        app_version = self.config.config["app_version"]
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>{app_name.replace(' ', '_')}</string>
    <key>CFBundleIdentifier</key>
    <string>com.yourcompany.{app_name.lower().replace(' ', '')}</string>
    <key>CFBundleName</key>
    <string>{app_name}</string>
    <key>CFBundleVersion</key>
    <string>{app_version}</string>
    <key>CFBundleShortVersionString</key>
    <string>{app_version}</string>
    <key>CFBundleIconFile</key>
    <string>icon.icns</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>'''
    
    def create_linux_packages(self) -> bool:
        """Create Linux distribution packages"""
        if self.config.platform != "linux":
            return True
        
        success = True
        
        # Create AppImage
        if not self._create_appimage():
            success = False
        
        # Create DEB package
        if not self._create_deb_package():
            success = False
        
        return success
    
    def _create_appimage(self) -> bool:
        """Create AppImage for Linux"""
        try:
            app_name = self.config.config["app_name"]
            appdir = Path(f"dist/{app_name}.AppDir")
            
            # Create AppDir structure
            usr_bin = appdir / "usr" / "bin"
            usr_share = appdir / "usr" / "share"
            usr_share.mkdir(parents=True, exist_ok=True)
            usr_bin.mkdir(parents=True, exist_ok=True)
            
            # Copy executable
            exe_src = Path(f"dist/{app_name.replace(' ', '_')}")
            exe_dst = usr_bin / app_name.replace(' ', '_')
            shutil.copy2(exe_src, exe_dst)
            exe_dst.chmod(0o755)
            
            # Create AppRun
            apprun_content = f'''#!/bin/bash
SELF=$(readlink -f "$0")
HERE=${{SELF%/*}}
EXEC="${{HERE}}/usr/bin/{app_name.replace(' ', '_')}"
exec "${{EXEC}}" "$@"
'''
            with open(appdir / "AppRun", "w") as f:
                f.write(apprun_content)
            (appdir / "AppRun").chmod(0o755)
            
            # Create desktop file
            desktop_content = f'''[Desktop Entry]
Type=Application
Name={app_name}
Exec={app_name.replace(' ', '_')}
Icon={app_name.lower().replace(' ', '')}
Categories=Utility;
'''
            with open(appdir / f"{app_name.replace(' ', '')}.desktop", "w") as f:
                f.write(desktop_content)
            
            self.logger.info("AppImage directory created successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"AppImage creation failed: {e}")
            return False
    
    def build_all_platforms(self):
        """Build for all target platforms"""
        self.logger.info("Starting cross-platform build process")
        
        # Clean previous builds
        self.clean_build()
        
        # Build executable
        if not self.build_executable():
            self.logger.error("Executable build failed")
            return False
        
        # Platform-specific packaging
        if self.config.platform == "windows":
            self.create_windows_installer()
        elif self.config.platform == "darwin":
            self.create_macos_bundle()
        elif self.config.platform == "linux":
            self.create_linux_packages()
        
        self.logger.info("Build process completed")
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    config = BuildConfig()
    builder = DesktopAppBuilder(config)
    builder.build_all_platforms()
```

### C++ Cross-Platform Deployment

**Use when CLAUDE.md specifies: C++, wxWidgets, CMake**

```cmake
# CMakeLists.txt - Cross-platform build configuration
cmake_minimum_required(VERSION 3.16)
project(DesktopApplication VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Package information
set(CPACK_PACKAGE_NAME "Desktop Application")
set(CPACK_PACKAGE_VERSION_MAJOR 1)
set(CPACK_PACKAGE_VERSION_MINOR 0)
set(CPACK_PACKAGE_VERSION_PATCH 0)
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Desktop application built with C++ and wxWidgets")
set(CPACK_PACKAGE_VENDOR "Your Company")
set(CPACK_PACKAGE_CONTACT "contact@yourcompany.com")

# Find required packages
find_package(wxWidgets REQUIRED COMPONENTS core base)
find_package(SQLite3 REQUIRED)

if(wxWidgets_FOUND)
    include(${wxWidgets_USE_FILE})
endif()

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# Source files
file(GLOB_RECURSE SOURCES
    "src/*.cpp"
    "src/*.h"
    "include/*.h"
)

# Exclude platform-specific files
if(NOT WIN32)
    list(FILTER SOURCES EXCLUDE REGEX ".*windows.*")
endif()

if(NOT APPLE)
    list(FILTER SOURCES EXCLUDE REGEX ".*macos.*")
endif()

if(NOT UNIX OR APPLE)
    list(FILTER SOURCES EXCLUDE REGEX ".*linux.*")
endif()

# Create executable
if(WIN32)
    add_executable(${PROJECT_NAME} WIN32 ${SOURCES})
    
    # Windows-specific settings
    set_target_properties(${PROJECT_NAME} PROPERTIES
        VS_DPI_AWARE "PerMonitor"
        WIN32_EXECUTABLE TRUE
    )
    
    # Windows resources
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/resources/app.rc")
        target_sources(${PROJECT_NAME} PRIVATE resources/app.rc)
    endif()
    
elseif(APPLE)
    add_executable(${PROJECT_NAME} MACOSX_BUNDLE ${SOURCES})
    
    # macOS-specific settings
    set_target_properties(${PROJECT_NAME} PROPERTIES
        MACOSX_BUNDLE TRUE
        MACOSX_BUNDLE_GUI_IDENTIFIER "com.yourcompany.desktopapp"
        MACOSX_BUNDLE_BUNDLE_NAME "Desktop Application"
        MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
        MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION}
        MACOSX_BUNDLE_COPYRIGHT "© Your Company"
    )
    
    # macOS icon
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/resources/app.icns")
        set_target_properties(${PROJECT_NAME} PROPERTIES
            MACOSX_BUNDLE_ICON_FILE app.icns
        )
        set_source_files_properties(resources/app.icns PROPERTIES
            MACOSX_PACKAGE_LOCATION Resources
        )
        target_sources(${PROJECT_NAME} PRIVATE resources/app.icns)
    endif()
    
else()
    add_executable(${PROJECT_NAME} ${SOURCES})
endif()

# Link libraries
target_link_libraries(${PROJECT_NAME}
    ${wxWidgets_LIBRARIES}
    SQLite::SQLite3
)

# Compiler-specific settings
if(MSVC)
    target_compile_options(${PROJECT_NAME} PRIVATE /W4)
    # Static linking for Windows
    set_property(TARGET ${PROJECT_NAME} PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
else()
    target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -pedantic)
endif()

# Installation settings
if(WIN32)
    install(TARGETS ${PROJECT_NAME}
        DESTINATION .
    )
    
    # Install Visual C++ Redistributables
    include(InstallRequiredSystemLibraries)
    
    # Windows installer with NSIS
    set(CPACK_GENERATOR "NSIS")
    set(CPACK_NSIS_DISPLAY_NAME "Desktop Application")
    set(CPACK_NSIS_PACKAGE_NAME "Desktop Application")
    set(CPACK_NSIS_HELP_LINK "https://yourcompany.com/support")
    set(CPACK_NSIS_URL_INFO_ABOUT "https://yourcompany.com")
    set(CPACK_NSIS_CONTACT "contact@yourcompany.com")
    set(CPACK_NSIS_MODIFY_PATH ON)
    set(CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL ON)
    
    # Desktop shortcut
    set(CPACK_NSIS_CREATE_ICONS_EXTRA
        "CreateShortCut '$DESKTOP\\\\Desktop Application.lnk' '$INSTDIR\\\\${PROJECT_NAME}.exe'"
    )
    
    set(CPACK_NSIS_DELETE_ICONS_EXTRA
        "Delete '$DESKTOP\\\\Desktop Application.lnk'"
    )
    
elseif(APPLE)
    install(TARGETS ${PROJECT_NAME}
        BUNDLE DESTINATION .
    )
    
    # macOS Bundle
    set(CPACK_GENERATOR "DragNDrop")
    set(CPACK_DMG_FORMAT "UDBZ")
    set(CPACK_DMG_VOLUME_NAME "Desktop Application")
    set(CPACK_DMG_DS_STORE "${CMAKE_CURRENT_SOURCE_DIR}/resources/DS_Store")
    set(CPACK_DMG_BACKGROUND_IMAGE "${CMAKE_CURRENT_SOURCE_DIR}/resources/dmg_background.png")
    
else()
    install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION bin
    )
    
    # Linux packages
    set(CPACK_GENERATOR "DEB;RPM;TGZ")
    
    # DEB package settings
    set(CPACK_DEBIAN_PACKAGE_DEPENDS "libwxgtk3.0-gtk3-0v5, libsqlite3-0")
    set(CPACK_DEBIAN_PACKAGE_SECTION "utils")
    set(CPACK_DEBIAN_PACKAGE_PRIORITY "optional")
    set(CPACK_DEBIAN_PACKAGE_HOMEPAGE "https://yourcompany.com")
    
    # RPM package settings
    set(CPACK_RPM_PACKAGE_GROUP "Applications/Productivity")
    set(CPACK_RPM_PACKAGE_LICENSE "MIT")
    set(CPACK_RPM_PACKAGE_URL "https://yourcompany.com")
    set(CPACK_RPM_PACKAGE_REQUIRES "wxGTK3-devel, sqlite-devel")
    
    # Install desktop file
    install(FILES resources/desktopapp.desktop
        DESTINATION share/applications
    )
    
    # Install icon
    install(FILES resources/app.png
        DESTINATION share/icons/hicolor/256x256/apps
        RENAME desktopapp.png
    )
endif()

# Resource files
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/resources")
    install(DIRECTORY resources/
        DESTINATION resources
        PATTERN "*.rc" EXCLUDE
        PATTERN "*.icns" EXCLUDE
    )
endif()

# Documentation
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/README.md")
    install(FILES README.md LICENSE
        DESTINATION docs
    )
endif()

# Enable CPack
include(CPack)

# Custom targets for development
add_custom_target(run
    COMMAND ${PROJECT_NAME}
    DEPENDS ${PROJECT_NAME}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Running the application"
)

add_custom_target(install-local
    COMMAND ${CMAKE_COMMAND} --build . --target install
    DEPENDS ${PROJECT_NAME}
    COMMENT "Installing locally"
)

# Platform-specific post-build steps
if(WIN32)
    # Copy wxWidgets DLLs for development
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        $<TARGET_FILE:${wxWidgets_LIBRARIES}>
        $<TARGET_FILE_DIR:${PROJECT_NAME}>
        COMMENT "Copying wxWidgets DLLs"
    )
endif()
```

```bash
#!/bin/bash
# build_scripts/build.sh - Cross-platform build script

set -e

# Configuration
APP_NAME="Desktop Application"
VERSION="1.0.0"
BUILD_TYPE="Release"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detect platform
PLATFORM=$(uname -s)
case $PLATFORM in
    Linux*)     PLATFORM=Linux;;
    Darwin*)    PLATFORM=macOS;;
    CYGWIN*|MINGW*|MSYS*) PLATFORM=Windows;;
    *)          PLATFORM="Unknown";;
esac

log_info "Building for platform: $PLATFORM"

# Create build directory
BUILD_DIR="build-$PLATFORM"
if [ -d "$BUILD_DIR" ]; then
    log_warn "Removing existing build directory"
    rm -rf "$BUILD_DIR"
fi

mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Configure build
log_info "Configuring CMake..."

CMAKE_ARGS="-DCMAKE_BUILD_TYPE=$BUILD_TYPE"

case $PLATFORM in
    Windows)
        CMAKE_ARGS="$CMAKE_ARGS -G \"Visual Studio 16 2019\" -A x64"
        ;;
    macOS)
        CMAKE_ARGS="$CMAKE_ARGS -DCMAKE_OSX_MINIMUM_VERSION=10.13"
        ;;
    Linux)
        CMAKE_ARGS="$CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=/usr"
        ;;
esac

eval "cmake $CMAKE_ARGS .."

# Build
log_info "Building application..."
cmake --build . --config $BUILD_TYPE --parallel $(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)

# Package
log_info "Creating packages..."
case $PLATFORM in
    Windows)
        cpack -G NSIS
        ;;
    macOS)
        cpack -G DragNDrop
        ;;
    Linux)
        cpack -G DEB
        cpack -G RPM
        cpack -G TGZ
        ;;
esac

# Show results
log_info "Build completed successfully!"
log_info "Packages created in: $(pwd)"
ls -la *.exe *.dmg *.deb *.rpm *.tar.gz 2>/dev/null || true

cd ..
```

### .NET Desktop Application Deployment  

**Use when CLAUDE.md specifies: C#, .NET, WPF/WinForms**

```xml
<!-- Directory.Build.props - Global project properties -->
<Project>
  <PropertyGroup>
    <TargetFramework>net6.0-windows</TargetFramework>
    <UseWPF>true</UseWPF>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    
    <!-- Application Information -->
    <AssemblyTitle>Desktop Application</AssemblyTitle>
    <AssemblyDescription>Desktop application built with .NET and WPF</AssemblyDescription>
    <AssemblyCompany>Your Company</AssemblyCompany>
    <AssemblyCopyright>© Your Company</AssemblyCopyright>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <ProductVersion>1.0.0</ProductVersion>
    
    <!-- Publishing Settings -->
    <PublishSingleFile>true</PublishSingleFile>
    <SelfContained>true</SelfContained>
    <PublishTrimmed>true</PublishTrimmed>
    <PublishReadyToRun>true</PublishReadyToRun>
    <IncludeNativeLibrariesForSelfExtract>true</IncludeNativeLibrariesForSelfExtract>
    
    <!-- Icon and Manifest -->
    <ApplicationIcon>Assets\app.ico</ApplicationIcon>
    <ApplicationManifest>app.manifest</ApplicationManifest>
  </PropertyGroup>
  
  <ItemGroup Condition="'$(TargetFramework)' == 'net6.0-windows'">
    <PackageReference Include="Microsoft.WindowsAppSDK" Version="1.4.231008000" />
    <PackageReference Include="Microsoft.Windows.SDK.BuildTools" Version="10.0.22621.2428" />
  </ItemGroup>
</Project>
```

```powershell
# build_scripts/Build-Application.ps1 - PowerShell build script
param(
    [string]$Configuration = "Release",
    [string]$Platform = "x64",
    [string]$OutputPath = "dist",
    [switch]$CreateInstaller = $false,
    [switch]$SignBinaries = $false
)

# Configuration
$AppName = "Desktop Application"
$Version = "1.0.0"
$Publisher = "Your Company"

Write-Host "Building $AppName v$Version" -ForegroundColor Green
Write-Host "Configuration: $Configuration" -ForegroundColor Yellow
Write-Host "Platform: $Platform" -ForegroundColor Yellow

# Clean previous builds
if (Test-Path $OutputPath) {
    Remove-Item -Recurse -Force $OutputPath
    Write-Host "Cleaned previous build artifacts" -ForegroundColor Yellow
}

New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null

# Build for different runtimes
$runtimes = @("win-x64", "win-x86", "win-arm64")

foreach ($runtime in $runtimes) {
    Write-Host "Building for runtime: $runtime" -ForegroundColor Cyan
    
    $publishPath = "$OutputPath\$runtime"
    
    # Publish application
    $publishArgs = @(
        "publish"
        "--configuration", $Configuration
        "--runtime", $runtime
        "--output", $publishPath
        "--self-contained", "true"
        "--publish-single-file", "true"
        "--publish-trimmed", "true"
        "--publish-ready-to-run", "true"
        "/p:IncludeNativeLibrariesForSelfExtract=true"
        "/p:PublishSingleFile=true"
        "/p:Version=$Version"
    )
    
    & dotnet @publishArgs
    
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Build failed for runtime $runtime"
        exit 1
    }
    
    # Sign binaries if requested
    if ($SignBinaries -and (Get-Command "signtool.exe" -ErrorAction SilentlyContinue)) {
        Write-Host "Signing binaries for $runtime" -ForegroundColor Yellow
        
        $exePath = Get-ChildItem "$publishPath\*.exe" | Select-Object -First 1
        if ($exePath) {
            & signtool.exe sign /fd SHA256 /t http://timestamp.digicert.com $exePath.FullName
        }
    }
    
    # Create ZIP archive
    $zipPath = "$OutputPath\$AppName-$Version-$runtime.zip"
    Compress-Archive -Path "$publishPath\*" -DestinationPath $zipPath -Force
    Write-Host "Created archive: $zipPath" -ForegroundColor Green
}

# Create Windows Installer using WiX
if ($CreateInstaller) {
    Write-Host "Creating Windows Installer..." -ForegroundColor Cyan
    
    # Check for WiX Toolset
    $wixPath = Get-Command "candle.exe" -ErrorAction SilentlyContinue
    if (-not $wixPath) {
        Write-Warning "WiX Toolset not found. Install from https://wixtoolset.org/"
    } else {
        # Generate WiX source
        $wxsContent = @"
<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Product Id="*" 
           Name="$AppName" 
           Language="1033" 
           Version="$Version" 
           Manufacturer="$Publisher" 
           UpgradeCode="{12345678-1234-1234-1234-123456789012}">
    
    <Package InstallerVersion="200" 
             Compressed="yes" 
             InstallScope="perMachine"
             Platform="x64" />
    
    <MajorUpgrade DowngradeErrorMessage="A newer version is already installed." />
    <MediaTemplate EmbedCab="yes" />
    
    <Feature Id="ProductFeature" Title="$AppName" Level="1">
      <ComponentGroupRef Id="ProductComponents" />
    </Feature>
    
    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFiles64Folder">
        <Directory Id="INSTALLFOLDER" Name="$AppName" />
      </Directory>
      <Directory Id="ProgramMenuFolder">
        <Directory Id="ApplicationProgramsFolder" Name="$AppName"/>
      </Directory>
      <Directory Id="DesktopFolder" />
    </Directory>
    
    <ComponentGroup Id="ProductComponents" Directory="INSTALLFOLDER">
      <Component Id="MainExecutable" Guid="*">
        <File Id="MainExe" 
              Source="$OutputPath\win-x64\DesktopApplication.exe" 
              KeyPath="yes"
              Checksum="yes" />
        
        <Shortcut Id="ApplicationStartMenuShortcut" 
                  Directory="ApplicationProgramsFolder" 
                  Name="$AppName"
                  WorkingDirectory="INSTALLFOLDER"
                  Icon="AppIcon.exe"
                  IconIndex="0" />
        
        <Shortcut Id="ApplicationDesktopShortcut"
                  Directory="DesktopFolder"
                  Name="$AppName"
                  WorkingDirectory="INSTALLFOLDER"
                  Icon="AppIcon.exe"
                  IconIndex="0" />
      </Component>
      
      <Component Id="ApplicationProgramsMenuFolder" Guid="*">
        <RemoveFolder Id="ApplicationProgramsFolder" On="uninstall"/>
        <RegistryValue Root="HKCU" 
                       Key="Software\$Publisher\$AppName" 
                       Name="installed" 
                       Type="integer" 
                       Value="1" 
                       KeyPath="yes"/>
      </Component>
    </ComponentGroup>
    
    <Icon Id="AppIcon.exe" SourceFile="$OutputPath\win-x64\DesktopApplication.exe" />
    <Property Id="ARPPRODUCTICON" Value="AppIcon.exe" />
    
    <Property Id="WIXUI_INSTALLDIR" Value="INSTALLFOLDER" />
    <UIRef Id="WixUI_InstallDir" />
    
  </Product>
</Wix>
"@
        
        $wxsPath = "$OutputPath\installer.wxs"
        $wxsContent | Out-File -FilePath $wxsPath -Encoding UTF8
        
        # Compile and link
        $objPath = "$OutputPath\installer.wixobj"
        $msiPath = "$OutputPath\$AppName-$Version-Setup.msi"
        
        & candle.exe -out $objPath $wxsPath
        & light.exe -out $msiPath -ext WixUIExtension $objPath
        
        if (Test-Path $msiPath) {
            Write-Host "Created installer: $msiPath" -ForegroundColor Green
            
            # Sign installer
            if ($SignBinaries -and (Get-Command "signtool.exe" -ErrorAction SilentlyContinue)) {
                Write-Host "Signing installer..." -ForegroundColor Yellow
                & signtool.exe sign /fd SHA256 /t http://timestamp.digicert.com $msiPath
            }
        }
    }
}

Write-Host "`nBuild completed successfully!" -ForegroundColor Green
Write-Host "Output directory: $OutputPath" -ForegroundColor Yellow
Get-ChildItem $OutputPath -Recurse -Include "*.exe", "*.zip", "*.msi" | Select-Object Name, Length, LastWriteTime
```

## Quality Gates

### ✅ Deployment Compliance
- [ ] Deployment approach matches CLAUDE.md technology specification
- [ ] Target platforms correctly identified and supported
- [ ] Platform-specific packaging implemented
- [ ] Installation/uninstallation tested on target platforms

### ✅ Distribution Quality
- [ ] Application signed for security (where applicable)
- [ ] Auto-update mechanism implemented
- [ ] Dependency management handled correctly
- [ ] Installation size optimized

### ✅ User Experience
- [ ] Professional installation experience
- [ ] Desktop shortcuts and menu entries created
- [ ] Uninstallation removes all components
- [ ] Application launches correctly after installation

**This prompt ensures desktop applications are packaged and deployed using appropriate methods for the technology stack and target platforms specified in CLAUDE.md, providing professional distribution packages.**