#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Data Collection Infrastructure
Claude Code Multi-Agent Framework Enhancement

This module implements comprehensive data collection infrastructure for training
ML models that will power intelligent agent selection and workflow orchestration.

Components:
- Project Context Analyzer
- Framework Usage Data Collector
- Agent Effectiveness Monitor
- MCP Tools Integration Layer
- Historical Success Pattern Extractor

Version: 1.0.0
Phase: 1 - Foundation Development
"""

import json
import os
import sys
import logging
import subprocess
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
import hashlib
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TechnologyStack:
    """Technology stack detection results"""
    frontend: List[str]
    backend: List[str]
    database: List[str]
    infrastructure: List[str]
    testing: List[str]
    mobile: List[str]
    desktop: List[str]
    graphics: List[str]
    ai_ml: List[str]
    blockchain: List[str]
    cloud_infrastructure: List[str]
    cybersecurity: List[str]
    multimedia: List[str]
    quantum: List[str]
    confidence_score: float

@dataclass
class ProjectComplexity:
    """Project complexity assessment metrics"""
    file_count: int
    code_lines: int
    directory_depth: int
    dependency_count: int
    complexity_rating: str  # startup/sme/enterprise
    complexity_score: float

@dataclass
class BusinessDomain:
    """Business domain classification"""
    primary: str
    secondary: List[str]
    industry_vertical: str
    compliance_requirements: List[str]
    confidence_score: float

@dataclass
class TeamContext:
    """Team and project context information"""
    estimated_team_size: str  # small/medium/large
    experience_indicators: List[str]
    development_patterns: List[str]
    git_activity_level: str
    collaboration_patterns: List[str]

@dataclass
class MCPToolsInsights:
    """Insights from MCP tools integration"""
    serena_available: bool
    serena_analysis: Optional[str]
    context7_available: bool
    context7_patterns: Optional[str]
    playwright_available: bool
    playwright_coverage: Optional[str]
    integration_quality_score: float

@dataclass
class ProjectContext:
    """Complete project context for ML feature extraction"""
    project_path: str
    technology_stack: TechnologyStack
    complexity: ProjectComplexity
    business_domain: BusinessDomain
    team_context: TeamContext
    mcp_insights: MCPToolsInsights
    framework_config: Optional[Dict[str, Any]]
    timestamp: datetime.datetime
    context_hash: str

class TechnologyDetector:
    """Advanced technology stack detection system"""

    def __init__(self):
        self.technology_patterns = {
            # ========== PROGRAMMING LANGUAGES (Complete Coverage) ==========
            'languages': {
                # Compiled Languages - C Family
                'cpp': ['.cpp', '.cxx', '.cc', '.C', '.c++', '.hpp', '.hxx', '.h++', '.hh', '#include <iostream>', 'std::', 'namespace'],
                'c': ['.c', '.h', '#include <stdio.h>', 'printf', 'malloc', 'gcc'],
                'objective_c': ['.m', '.mm', '@interface', '@implementation', 'NSString', 'Cocoa.h'],
                'objective_cpp': ['.mm', '.M'],

                # Modern Systems Languages
                'rust': ['.rs', 'Cargo.toml', 'Cargo.lock', 'fn main', 'use std::', 'rustc'],
                'go': ['.go', 'go.mod', 'go.sum', 'package main', 'import', 'func main'],
                'zig': ['.zig', 'const std', 'pub fn', 'test'],
                'carbon': ['.carbon', 'package', 'import Std'],
                'nim': ['.nim', '.nims', '.nimble', 'proc main'],
                'crystal': ['.cr', 'shards.yml', 'require'],
                'dlang': ['.d', 'dub.json', 'import std', 'void main'],

                # JVM Languages
                'java': ['.java', '.class', '.jar', 'public class', 'public static void main', 'import java'],
                'kotlin': ['.kt', '.kts', 'fun main', 'import kotlin'],
                'scala': ['.scala', '.sc', 'def main', 'object', 'import scala'],
                'groovy': ['.groovy', '.gvy', 'def main', '@Grab'],
                'clojure': ['.clj', '.cljs', '.cljc', 'defn', 'project.clj'],

                # .NET Languages
                'csharp': ['.cs', '.csx', 'using System', 'public class', 'static void Main'],
                'fsharp': ['.fs', '.fsx', '.fsi', 'let main', 'open System'],
                'vbnet': ['.vb', 'Module', 'Sub Main', 'Imports System'],

                # Functional Languages
                'haskell': ['.hs', '.lhs', '.cabal', 'main = ', 'import Prelude'],
                'ocaml': ['.ml', '.mli', '.opam', 'let main', 'open'],
                'erlang': ['.erl', '.hrl', 'rebar.config', '-module', '-export'],
                'elixir': ['.ex', '.exs', 'mix.exs', 'defmodule', 'def main'],
                'elm': ['.elm', 'elm.json', 'main =', 'import'],

                # Scripting Languages
                'python': ['.py', '.pyw', '.pyx', 'def main', 'if __name__', 'import'],
                'ruby': ['.rb', '.rbw', 'Gemfile', 'def main', 'require'],
                'perl': ['.pl', '.pm', 'cpanfile', 'sub main', 'use strict'],
                'php': ['.php', '.phtml', 'composer.json', '<?php', 'function main'],
                'lua': ['.lua', 'main =', 'require', 'local'],
                'tcl': ['.tcl', 'proc main', 'source'],
                'powershell': ['.ps1', '.psm1', '.psd1', 'function Main', 'Import-Module'],
                'bash': ['.sh', '.bash', '#!/bin/bash', 'function main'],
                'zsh': ['.zsh', '#!/bin/zsh'],
                'fish': ['.fish', '#!/usr/bin/fish'],

                # Mobile Languages
                'swift': ['.swift', 'Package.swift', 'import Foundation', 'func main'],
                'dart': ['.dart', 'pubspec.yaml', 'void main', 'import'],

                # Web Languages
                'typescript': ['.ts', '.tsx', 'tsconfig.json', 'interface', 'type'],
                'javascript': ['.js', '.jsx', '.mjs', 'package.json', 'function main'],
                'coffeescript': ['.coffee', 'main =', '->'],

                # Assembly Languages
                'assembly_x86': ['.asm', '.s', '.S', '.nasm', 'mov eax', 'int 0x80'],
                'assembly_arm': ['.s', '.S', 'mov r0', 'bx lr'],
                'assembly_mips': ['.s', 'li $v0', 'syscall'],

                # Legacy Languages
                'fortran': ['.f90', '.f95', '.f03', '.f08', '.for', '.f', 'program main', 'end program'],
                'cobol': ['.cob', '.cbl', 'IDENTIFICATION DIVISION', 'PROGRAM-ID'],
                'pascal': ['.pas', '.pp', 'program main', 'begin', 'end.'],
                'ada': ['.adb', '.ads', 'procedure Main', 'with Ada'],
                'modula': ['.mod', '.def', 'MODULE', 'PROCEDURE Main'],

                # Specialized Languages
                'r': ['.R', '.r', 'DESCRIPTION', 'main <- function', 'library('],
                'julia': ['.jl', 'Project.toml', 'function main', 'using'],
                'matlab': ['.m', '.mat', 'function main', 'addpath'],
                'mathematica': ['.nb', '.wl', '.m', 'Main :='],
                'maple': ['.mw', '.maple', 'main := proc'],
                'octave': ['.m', 'function main'],
                'scilab': ['.sci', '.sce', 'function main'],
                'sage': ['.sage', '.py', 'def main']
            },

            # ========== GUI FRAMEWORKS (Complete Desktop Coverage) ==========
            'gui_frameworks': {
                # C++ GUI Frameworks
                'wxwidgets': ['wx/', 'wxApp', 'wxFrame', 'wxPanel', '#include <wx/', '.wxs', 'wxWidgets', 'wxUSE_'],
                'qt5': ['Qt5/', 'QApplication', 'QWidget', 'QMainWindow', 'qt5-', '#include <Q', 'QT5_'],
                'qt6': ['Qt6/', 'qt6-', 'QT += ', '.pro', '.pri', 'qt_add_', 'QT6_'],
                'fltk': ['FL/', 'Fl_Window', 'Fl_Button', 'fltk-', '#include <FL/'],
                'gtkmm': ['gtkmm/', 'Gtk::Window', 'Gtk::Application', '#include <gtkmm'],
                'fox_toolkit': ['FX/', 'FXApp', 'FXMainWindow', '#include <fx.h>'],
                'cegui': ['CEGUI/', 'cegui/', 'CEGUIBase', '#include <CEGUI'],
                'imgui': ['imgui/', 'ImGui::', 'imgui.h', 'dear imgui', 'IMGUI_'],
                'nana': ['nana/', 'nana::', 'nana/gui', '#include <nana'],
                'nuklear': ['nuklear.h', 'NK_', 'nk_', '#include "nuklear.h"'],
                'iced': ['iced::', 'iced_native', 'iced_winit'],

                # .NET GUI Frameworks
                'winforms': ['.designer.cs', 'System.Windows.Forms', 'Form1.cs', 'using System.Windows.Forms'],
                'wpf': ['.xaml', 'System.Windows', 'Window.xaml', 'using System.Windows'],
                'avalonia': ['Avalonia/', '.axaml', 'AvaloniaUI', 'using Avalonia'],
                'maui': ['Microsoft.Maui', '.NET MAUI', 'Platforms/', 'using Microsoft.Maui'],
                'uno': ['Uno.UI', 'uno-platform', 'using Uno'],

                # Java GUI Frameworks
                'swing': ['javax.swing', 'JFrame', 'JPanel', 'import javax.swing'],
                'javafx': ['javafx', '.fxml', 'Stage', 'Scene', 'import javafx'],
                'swt': ['org.eclipse.swt', 'Display', 'Shell', 'import org.eclipse.swt'],

                # Python GUI Frameworks
                'tkinter': ['tkinter', 'Tk()', 'mainloop', 'import tkinter'],
                'pyqt5': ['PyQt5', 'QApplication', 'pyqt5-tools', 'from PyQt5'],
                'pyqt6': ['PyQt6', 'pyqt6-tools', 'from PyQt6'],
                'pyside2': ['PySide2', 'QtWidgets', 'from PySide2'],
                'pyside6': ['PySide6', 'pyside6-uic', 'from PySide6'],
                'kivy': ['kivy', 'App', 'runTouchApp', 'from kivy'],
                'dear_pygui': ['dearpygui', 'dpg.', 'import dearpygui'],
                'ttkbootstrap': ['ttkbootstrap', 'ttk.Style', 'import ttkbootstrap'],
                'customtkinter': ['customtkinter', 'CTk', 'import customtkinter'],

                # Cross-Platform Web-based
                'electron': ['electron', 'main.js', 'renderer.js', 'package.json'],
                'tauri': ['tauri/', 'tauri.conf.json', 'src-tauri/', '#[tauri::command]'],
                'nwjs': ['nw.js', 'nwjs', 'package.json'],
                'neutralino': ['neutralino', 'neutralino.config.json'],
                'wails': ['wails', 'app.go', 'wails.json', 'embed.go'],

                # Game UI Frameworks
                'cegui_ogre': ['CEGUIOgreRenderer'],
                'coherent_ui': ['coherent/', 'CoherentUI'],
                'noesis_gui': ['NoesisGUI/', 'noesis'],
                'scaleform': ['scaleform/', 'GFx']
            },

            # ========== BACKEND ARCHITECTURES (Enterprise Coverage) ==========
            'backend_architectures': {
                # Web Servers
                'nginx': ['nginx.conf', '/etc/nginx/', 'nginx', 'server {', 'location /'],
                'apache': ['httpd.conf', '.htaccess', 'apache2', '<VirtualHost', 'LoadModule'],
                'iis': ['web.config', 'applicationHost.config', 'system.webServer'],
                'caddy': ['Caddyfile', 'caddy', ':80 {'],
                'traefik': ['traefik.yml', 'traefik.toml', 'api:', 'entryPoints:'],
                'lighttpd': ['lighttpd.conf', 'server.modules'],
                'haproxy': ['haproxy.cfg', 'haproxy', 'global', 'defaults'],

                # Application Servers
                'tomcat': ['server.xml', 'context.xml', 'catalina', 'webapps/'],
                'jetty': ['jetty.xml', 'jetty-web.xml', 'org.eclipse.jetty'],
                'wildfly': ['standalone.xml', 'jboss', 'deployments/'],
                'websphere': ['was.policy', 'ibm-web-ext', 'websphere'],
                'weblogic': ['weblogic.xml', 'config.xml', 'oracle.weblogic'],
                'glassfish': ['domain.xml', 'sun-web.xml', 'glassfish'],
                'jboss': ['jboss-web.xml', 'jboss-deployment'],

                # Microservices Platforms
                'istio': ['istio/', 'VirtualService', 'DestinationRule', 'ServiceMesh'],
                'consul': ['consul.hcl', 'consul-template', 'hashicorp/consul'],
                'vault': ['vault.hcl', 'vault-agent', 'hashicorp/vault'],
                'nomad': ['nomad.hcl', '.nomad', 'hashicorp/nomad'],
                'linkerd': ['linkerd', 'policy.yaml', 'linkerd.io'],
                'envoy': ['envoy.yaml', 'envoy-proxy', 'envoyproxy'],

                # Message Brokers
                'rabbitmq': ['rabbitmq.conf', 'rabbitmq-env', 'amqp://'],
                'apache_kafka': ['server.properties', 'kafka-topics', 'kafka_'],
                'activemq': ['activemq.xml', 'artemis', 'jms.'],
                'nats': ['nats.conf', 'nats-streaming', 'nats://'],
                'redis_streams': ['redis.conf', 'redis-server', 'XREAD'],
                'pulsar': ['broker.conf', 'pulsar', 'pulsar://'],

                # API Gateways
                'kong': ['kong.conf', 'kong.yml', 'kong-'],
                'ambassador': ['ambassador/', 'getambassador', 'ambassador.'],
                'zuul': ['zuul.properties', 'netflix-zuul', '@EnableZuulProxy'],
                'spring_cloud_gateway': ['spring-cloud-gateway', 'RouteLocator'],
                'aws_api_gateway': ['serverless.yml', 'aws-api-gateway']
            },

            # ========== DATABASE SYSTEMS (Complete Coverage) ==========
            'database': {
                # Relational Databases
                'postgresql': ['postgresql.conf', 'pg_hba.conf', 'psql', 'SELECT version()', 'CREATE TABLE'],
                'mysql': ['my.cnf', 'mysql', 'mariadb', 'SHOW TABLES', 'ENGINE=InnoDB'],
                'oracle': ['tnsnames.ora', 'oracle/', 'oci', 'SELECT * FROM dual', 'ORACLE_HOME'],
                'sql_server': ['sql-server/', 'sqlcmd', '.mdf', '.ldf', 'USE master'],
                'db2': ['db2/', 'db2inst', 'DB2_HOME', 'CONNECT TO'],
                'sqlite': ['.sqlite', '.db', 'sqlite3', 'CREATE TABLE', '.schema'],
                'h2': ['h2.mv.db', 'h2-', 'org.h2.Driver'],
                'hsqldb': ['hsqldb/', '.script', 'org.hsqldb'],
                'firebird': ['firebird/', '.fdb', '.gdb'],
                'access': ['.mdb', '.accdb', 'Microsoft.Jet'],

                # NoSQL Document Stores
                'mongodb': ['mongod.conf', 'mongo', 'mongoose', 'db.collection', 'ObjectId'],
                'couchdb': ['couchdb/', 'couchdb.ini', '_design/', 'map:'],
                'couchbase': ['couchbase/', 'cb-', 'N1QL'],
                'amazon_documentdb': ['documentdb', 'docdb'],

                # Graph Databases
                'neo4j': ['neo4j.conf', 'cypher', 'MATCH (', 'CREATE ('],
                'arangodb': ['arangod.conf', 'arangodb', 'FOR doc IN'],
                'orientdb': ['orientdb/', 'orientdb-server', 'SELECT FROM'],
                'amazon_neptune': ['neptune', 'gremlin'],

                # Column Family
                'cassandra': ['cassandra.yaml', 'cqlsh', 'CREATE KEYSPACE', 'SELECT * FROM'],
                'hbase': ['hbase-site.xml', 'hbase', 'org.apache.hadoop.hbase'],
                'dynamodb': ['dynamodb', 'aws-sdk', 'boto3', 'scan('],

                # Key-Value Stores
                'redis': ['redis.conf', 'redis-server', 'redis-cli', 'SET key', 'GET key'],
                'memcached': ['memcached.conf', 'memcached', 'set(', 'get('],
                'etcd': ['etcd.conf', 'etcdctl', 'clientv3'],
                'consul_kv': ['consul/', 'consul-kv', 'consul.kv'],
                'hazelcast': ['hazelcast.xml', 'hazelcast-', 'IMap'],

                # Search Engines
                'elasticsearch': ['elasticsearch.yml', 'elastic', 'GET /_search', 'index:'],
                'solr': ['solr.xml', 'solrconfig.xml', 'select?q='],
                'opensearch': ['opensearch.yml', 'opensearch', '_search'],
                'sphinx': ['sphinx.conf', 'searchd', 'SELECT * FROM'],

                # Time Series Databases
                'influxdb': ['influxdb.conf', 'influx', 'SELECT mean(', 'FROM'],
                'prometheus': ['prometheus.yml', 'promql', 'scrape_configs:'],
                'timescaledb': ['timescaledb', 'postgresql', 'CREATE HYPERTABLE'],
                'victoriametrics': ['victoria-metrics', 'vmselect']
            },

            # ========== DESKTOP-SPECIFIC TECHNOLOGIES ==========
            'desktop_specific': {
                # Windows Desktop Technologies
                'win32_api': ['windows.h', 'user32.lib', 'kernel32.lib', 'HWND', 'WINAPI'],
                'mfc': ['afxwin.h', 'CWinApp', 'CFrameWnd', 'BEGIN_MESSAGE_MAP'],
                'atl': ['atlbase.h', 'ATL', 'CComPtr', 'DECLARE_REGISTRY'],
                'com': ['comdef.h', 'IUnknown', 'CoInitialize', 'HRESULT'],
                'directx': ['d3d9.h', 'd3d11.h', 'directx-sdk', 'ID3D11Device'],
                'directshow': ['dshow.h', 'directshow', 'IGraphBuilder'],
                'wmi': ['wbemidl.h', 'WMI', 'IWbemServices'],
                'powershell': ['.ps1', 'powershell', 'Get-', 'Set-'],

                # macOS Desktop Technologies
                'cocoa': ['Cocoa.h', 'NSApplication', 'NSViewController', '#import <Cocoa/Cocoa.h>'],
                'core_foundation': ['CoreFoundation/', 'CFString', 'CFRelease'],
                'core_graphics': ['CoreGraphics/', 'CGContext', 'CGPoint'],
                'core_animation': ['CoreAnimation/', 'CALayer', 'CABasicAnimation'],
                'app_kit': ['AppKit/', 'NSWindow', 'NSView'],
                'swift_ui': ['SwiftUI', '@State', '@ObservedObject', 'NavigationView'],
                'objective_c': ['.m', '.mm', '@interface', '@implementation'],

                # Linux Desktop Technologies
                'gtk3': ['gtk+-3.0', 'GtkWidget', 'gtk_init', '#include <gtk/gtk.h>'],
                'gtk4': ['gtk4', 'gtk_application_new', 'GtkApplication'],
                'kde': ['KDE/', 'kdelibs', 'plasma', 'KMainWindow'],
                'x11': ['X11/', 'XOpenDisplay', 'xcb', '#include <X11/Xlib.h>'],
                'wayland': ['wayland/', 'wl_display', 'wayland-client'],
                'dbus': ['dbus/', 'dbus-1', 'dbus_connection'],
                'systemd': ['systemd/', '.service', 'ExecStart='],

                # Cross-Platform Native Frameworks
                'sdl2': ['SDL2/', 'SDL_Init', 'SDL_CreateWindow', '#include <SDL2/SDL.h>'],
                'allegro': ['allegro5/', 'al_init', 'ALLEGRO_DISPLAY'],
                'sfml': ['SFML/', 'sf::RenderWindow', '#include <SFML/Graphics.hpp>'],
                'raylib': ['raylib.h', 'InitWindow', 'BeginDrawing'],
                'glfw': ['GLFW/', 'glfwInit', 'glfwCreateWindow', '#include <GLFW/glfw3.h>'],

                # Multimedia Frameworks
                'ffmpeg': ['ffmpeg/', 'libav', 'avcodec', 'av_register_all'],
                'gstreamer': ['gstreamer/', 'gst-', 'gst_init'],
                'vlc': ['vlc/', 'libvlc', 'libvlc_new'],
                'opencv': ['opencv2/', 'cv::', '#include <opencv2/opencv.hpp>'],
                'openal': ['AL/', 'alc', 'openal', 'alGenSources']
            },

            # ========== BUILD SYSTEMS & CONFIGURATION ==========
            'build_systems': {
                # Build Systems
                'cmake': ['CMakeLists.txt', '.cmake', 'cmake-build/', 'add_executable', 'find_package'],
                'autotools': ['configure.ac', 'Makefile.am', 'autogen.sh', 'AC_INIT', 'AM_INIT_AUTOMAKE'],
                'meson': ['meson.build', 'meson_options.txt', 'project(', 'executable('],
                'ninja': ['build.ninja', '.ninja', 'rule compile'],
                'scons': ['SConstruct', 'SConscript', 'env = Environment'],
                'waf': ['wscript', 'waf', 'def configure'],
                'buck': ['BUCK', '.buckconfig', 'cxx_binary'],
                'pants': ['BUILD', 'pants.ini', 'pants.toml'],
                'please': ['BUILD.plz', '.plzconfig', 'cc_binary'],
                'bazel': ['BUILD', 'WORKSPACE', 'cc_binary', 'cc_library'],
                'qmake': ['.pro', '.pri', 'TARGET =', 'SOURCES +='],
                'premake': ['premake5.lua', 'premake4.lua', 'workspace'],
                'xcode': ['.xcodeproj', '.xcworkspace', 'project.pbxproj'],
                'msbuild': ['.sln', '.vcxproj', '.csproj', '<Project'],
                'make': ['Makefile', 'makefile', 'GNUmakefile', '$(CC)', '.PHONY'],

                # Package Managers
                'vcpkg': ['vcpkg.json', 'vcpkg-configuration.json', 'vcpkg install'],
                'conan': ['conanfile.txt', 'conanfile.py', '[requires]'],
                'hunter': ['cmake/Hunter/', 'HunterGate.cmake', 'hunter_add_package'],
                'cpm': ['CPM.cmake', 'cpm-package-lock.cmake', 'CPMAddPackage'],
                'nuget': ['packages.config', '.nuspec', 'PackageReference'],
                'chocolatey': ['.chocolatey', 'chocolateyInstall.ps1', 'choco install'],

                # IDE Project Files
                'visual_studio': ['.sln', '.vcxproj', '.vcxproj.filters', 'Microsoft Visual Studio Solution'],
                'qt_creator': ['.pro', '.pri', '.qbs', 'TEMPLATE = app'],
                'code_blocks': ['.cbp', '.workspace', '<CodeBlocks_project_file>'],
                'dev_cpp': ['.dev', '.layout', '[Project]'],
                'clion': ['.idea/', 'CMakeLists.txt', '.idea/workspace.xml'],
                'eclipse_cdt': ['.cproject', '.project', '<projectDescription>'],
                'netbeans': ['nbproject/', 'Makefile-*', 'project.xml'],
                'kdevelop': ['.kdev4/', '.kdev_include_paths', '.kdev4']
            },

            # ========== GRAPHICS & GAME DEVELOPMENT ==========
            'graphics': {
                # 3D Graphics APIs
                'opengl': ['opengl', 'glfw', 'glad', 'glew', 'gl.h', '#include <GL/gl.h>', 'glBegin', 'glVertex'],
                'vulkan': ['vulkan/', 'vk_', 'vulkan.h', 'VkInstance', 'vkCreateInstance'],
                'directx9': ['d3d9.h', 'IDirect3DDevice9', 'D3DPRESENT_PARAMETERS'],
                'directx11': ['d3d11.h', 'ID3D11Device', 'D3D11CreateDevice'],
                'directx12': ['d3d12.h', 'ID3D12Device', 'D3D12CreateDevice'],
                'metal': ['Metal/', 'MTL', 'id<MTLDevice>', '#include <Metal/Metal.h>'],
                'webgl': ['webgl', 'gl-matrix', 'gl.createShader'],

                # 2D Graphics Libraries
                'sdl2_graphics': ['SDL2/', 'SDL.h', 'SDL_Renderer', 'SDL_CreateRenderer'],
                'allegro_graphics': ['allegro5/', 'allegro.h', 'ALLEGRO_BITMAP'],
                'sfml_graphics': ['SFML/', 'sf::', 'sf::Sprite', 'sf::Texture'],
                'raylib_graphics': ['raylib.h', 'DrawCircle', 'LoadTexture'],
                'cairo': ['cairo/', 'cairo.h', 'cairo_t', 'cairo_create'],
                'skia': ['skia/', 'SkCanvas', 'SkPaint'],

                # Image Processing
                'opencv': ['opencv2/', 'cv2', 'cv::', 'Mat', 'imread'],
                'imagemagick': ['Magick++', 'magick/', 'Image'],
                'pil': ['PIL/', 'Pillow', 'from PIL import Image'],
                'freeimage': ['FreeImage.h', 'FreeImage_Load'],
                'devil': ['IL/', 'ilInit', 'ilLoadImage'],

                # 3D Engines & Frameworks
                'unity3d': ['.unity', 'Assets/', 'UnityEngine', 'MonoBehaviour'],
                'unreal_engine': ['.uproject', 'Source/', 'UnrealEngine', 'UCLASS'],
                'godot': ['.godot', '.gd', '.tscn', 'extends Node'],
                'gamemaker': ['.gml', '.yy', 'instance_create'],
                'construct': ['.c3p', 'Construct 3'],
                'defold': ['.script', '.go', 'function init'],
                'cocos2d': ['cocos2d/', 'CCSprite', 'CCScene'],
                'love2d': ['main.lua', 'love.', 'function love.load'],
                'panda3d': ['panda3d/', 'ShowBase', 'from panda3d'],
                'irrlicht': ['irrlicht/', 'IrrlichtDevice', 'createDevice'],
                'ogre3d': ['Ogre/', 'Ogre::', 'SceneManager'],
                'cryengine': ['CryEngine/', 'IEntity', 'CRYENGINE'],

                # Rendering Libraries
                'pbrt': ['pbrt/', 'pbrt.h', 'Transform'],
                'cycles': ['cycles/', 'bpy.', 'import bpy'],
                'arnold': ['arnold/', 'ai.h', 'AiNode'],
                'renderman': ['prman/', 'ri.h', 'RiBegin'],

                # Web 3D
                'three_js': ['three.js', 'THREE.', 'new THREE.Scene'],
                'babylon_js': ['babylonjs', 'BABYLON.', 'new BABYLON.Scene'],
                'aframe': ['aframe', 'a-scene', '<a-box>'],
                'playcanvas': ['playcanvas', 'pc.Application']
            },

            # ========== SCIENTIFIC & ENGINEERING ==========
            'scientific': {
                # Mathematics Software
                'matlab': ['.m', '.mat', 'matlab', 'function main', 'addpath'],
                'mathematica': ['.nb', '.wl', 'Mathematica', 'Manipulate'],
                'maple': ['.mw', '.maple', 'main := proc'],
                'sage': ['.sage', 'sagemath', 'def main'],
                'octave': ['.m', 'octave', 'function main'],
                'scilab': ['.sci', '.sce', 'function main'],
                'r': ['.R', '.r', 'DESCRIPTION', 'main <- function', 'library('],
                'julia': ['.jl', 'Project.toml', 'function main', 'using'],

                # Simulation Software
                'ansys': ['.ans', '.mac', 'ANSYS', '/PREP7'],
                'abaqus': ['.inp', '.odb', 'Abaqus', '*HEADING'],
                'nastran': ['.bdf', '.nas', 'MSC Nastran', 'BEGIN BULK'],
                'openfoam': ['controlDict', 'fvSchemes', 'OpenFOAM', 'FoamFile'],
                'comsol': ['.mph', 'COMSOL', 'Multiphysics'],

                # CAD/CAE Libraries
                'freecad': ['.FCStd', '.py', 'FreeCAD', 'import FreeCAD'],
                'opencascade': ['opencascade/', 'TopoDS_', 'gp_Pnt'],
                'cgal': ['CGAL/', 'cgal', 'CGAL::'],
                'vtk': ['vtk/', 'vtkSmartPointer', 'vtkPolyData'],
                'itk': ['itk/', 'itkImage', 'itk::Image'],
                'pcl': ['pcl/', 'pcl::', 'pcl::PointCloud'],

                # Physics Simulation
                'geant4': ['G4', 'geant4/', 'G4RunManager'],
                'root': ['TH1', 'TTree', '.root', '#include <TApplication.h>'],
                'hep': ['fastjet/', 'pythia8/', 'CLHEP/'],

                # Numerical Libraries
                'eigen': ['Eigen/', 'Eigen::', 'Matrix3d'],
                'armadillo': ['armadillo', 'arma::', 'mat'],
                'blas': ['cblas.h', 'cblas_', 'BLAS'],
                'lapack': ['lapack.h', 'clapack_', 'LAPACK'],
                'mkl': ['mkl.h', 'MKL_', 'Intel MKL'],
                'gsl': ['gsl/', 'gsl_', 'GNU Scientific Library']
            },

            # ========== EMBEDDED & IoT ==========
            'embedded': {
                # Microcontroller Platforms
                'arduino': ['Arduino.h', '.ino', 'setup()', 'loop()', 'digitalWrite'],
                'esp32': ['esp_', 'ESP32', 'freertos/', 'esp_wifi.h'],
                'esp8266': ['ESP8266', 'esp8266/', 'ESP8266WiFi.h'],
                'stm32': ['stm32', 'HAL_', 'CMSIS/', 'stm32f4xx.h'],
                'pic': ['pic.h', '__CONFIG', 'TRIS', 'PORT'],
                'avr': ['avr/', 'DDRB', 'PORTB', '#include <avr/io.h>'],
                'msp430': ['msp430', 'wdt_', 'msp430.h'],
                'nordic': ['nrf5', 'nrf_', 'nrf52', 'softdevice'],
                'ti': ['driverlib/', 'TivaWare/', 'ti_drivers'],
                'cypress': ['cy_', 'PSoC', 'Cypress'],
                'microchip': ['pic32', 'harmony/', 'plib.h'],

                # Real-Time Operating Systems
                'freertos': ['FreeRTOS.h', 'xTaskCreate', 'vTaskDelay'],
                'zephyr': ['zephyr/', 'k_thread', 'CONFIG_'],
                'mbedos': ['mbed.h', 'mbed-os/', 'Thread'],
                'riot': ['RIOT/', 'thread_create', 'msg_t'],
                'contiki': ['contiki.h', 'PROCESS', 'AUTOSTART_PROCESSES'],
                'nuttx': ['nuttx/', 'CONFIG_', 'main()'],
                'tinyos': ['TinyOS', 'nesC', 'interface'],

                # Communication Protocols
                'can': ['can.h', 'CAN_', 'CanTxMsg'],
                'modbus': ['modbus.h', 'mb_', 'modbus_'],
                'mqtt': ['MQTTClient', 'paho', 'mosquitto'],
                'lorawan': ['lorawan/', 'lora_', 'LoRaWAN'],
                'bluetooth': ['bluetooth/', 'bt_', 'BluetoothSerial'],
                'zigbee': ['zigbee/', 'zb_', 'ZigBee'],
                'wifi': ['WiFi.h', 'wifi_', 'ESP8266WiFi'],
                'ethernet': ['Ethernet.h', 'eth_', 'EthernetClient'],

                # Industrial Protocols
                'profibus': ['profibus/', 'pb_', 'PROFIBUS'],
                'profinet': ['profinet/', 'pn_', 'PROFINET'],
                'ethercat': ['ethercat/', 'ec_', 'EtherCAT'],
                'devicenet': ['devicenet/', 'dn_', 'DeviceNet']
            },

            # ========== WEB FRONTEND (Extended) ==========
            'frontend': {
                # JavaScript Frameworks
                'react': ['package.json', 'react', 'jsx', 'tsx', 'React.Component'],
                'angular': ['angular.json', '@angular', 'component.ts', 'ng serve'],
                'vue': ['vue.config.js', 'vue', '.vue', 'Vue.component'],
                'svelte': ['svelte', '.svelte', 'svelte.config.js'],
                'ember': ['ember-cli', '.ember-cli', 'Ember.Component'],
                'backbone': ['backbone.js', 'Backbone.Model', 'Backbone.View'],
                'knockout': ['knockout.js', 'ko.observable', 'data-bind'],
                'polymer': ['polymer', 'PolymerElement', '@polymer'],
                'lit': ['lit-element', 'LitElement', 'lit-html'],
                'alpine': ['alpine.js', 'x-data', 'x-show'],
                'stimulus': ['stimulus', 'data-controller', 'Stimulus.register'],

                # CSS Frameworks
                'bootstrap': ['bootstrap', 'bootstrap.css', 'container', 'row'],
                'tailwind': ['tailwind.config.js', 'tailwindcss', '@apply'],
                'bulma': ['bulma', 'bulma.css', 'column', 'section'],
                'foundation': ['foundation', 'foundation.css', 'grid-x'],
                'materialize': ['materialize', 'materialize.css', 'waves-effect'],
                'semantic_ui': ['semantic-ui', 'semantic.css', 'ui segment'],
                'chakra_ui': ['@chakra-ui', 'ChakraProvider', 'Box'],
                'ant_design': ['antd', '@ant-design', 'import { Button }'],
                'material_ui': ['@mui/material', '@material-ui', 'makeStyles'],

                # Build Tools
                'webpack': ['webpack.config.js', 'webpack', 'module.exports'],
                'vite': ['vite.config.js', 'vite', 'import.meta.hot'],
                'parcel': ['parcel', '.parcelrc', 'parcel-bundler'],
                'rollup': ['rollup.config.js', 'rollup', 'export default'],
                'esbuild': ['esbuild', 'esbuild.js', 'build.js'],
                'snowpack': ['snowpack.config.js', 'snowpack', 'mount'],
                'turbopack': ['turbopack', 'next.config.js'],

                # TypeScript & Languages
                'typescript': ['tsconfig.json', '.ts', '.tsx', 'interface', 'type'],
                'javascript': ['package.json', '.js', '.jsx', 'function', 'const'],
                'coffeescript': ['.coffee', 'coffee-script', '->'],
                'purescript': ['.purs', 'purescript', 'module'],
                'elm': ['.elm', 'elm.json', 'main ='],
                'reasonml': ['.re', '.rei', 'reason', 'let'],
                'clojurescript': ['.cljs', 'clojurescript', 'defn'],

                # Static Site Generators
                'gatsby': ['gatsby-config.js', 'gatsby', 'export { graphql }'],
                'next': ['next.config.js', 'next', 'getStaticProps'],
                'nuxt': ['nuxt.config.js', 'nuxt', 'asyncData'],
                'gridsome': ['gridsome.config.js', 'gridsome'],
                'hugo': ['config.toml', 'hugo', 'content/'],
                'jekyll': ['_config.yml', '_posts/', 'jekyll'],
                'eleventy': ['.eleventy.js', '11ty', 'eleventy']
            },

            # ========== BACKEND (Extended) ==========
            'backend': {
                # Python Frameworks
                'python': ['.py', 'requirements.txt', 'setup.py', 'pyproject.toml'],
                'django': ['django', 'manage.py', 'settings.py', 'from django'],
                'flask': ['flask', 'app.py', 'from flask import'],
                'fastapi': ['fastapi', 'uvicorn', 'from fastapi import'],
                'tornado': ['tornado', 'tornado.web', 'RequestHandler'],
                'pyramid': ['pyramid', 'pyramid.config', 'Configurator'],
                'bottle': ['bottle', 'bottle.py', '@route'],
                'cherrypy': ['cherrypy', 'cherrypy.expose'],
                'falcon': ['falcon', 'falcon.API', 'on_get'],
                'sanic': ['sanic', 'Sanic', 'from sanic import'],
                'quart': ['quart', 'Quart', 'from quart import'],

                # Node.js Frameworks
                'nodejs': ['package.json', '.js', '.ts', 'require(', 'import'],
                'express': ['express', 'app.js', 'app.listen'],
                'koa': ['koa', 'Koa', 'ctx.body'],
                'hapi': ['@hapi/hapi', 'server.route'],
                'fastify': ['fastify', 'fastify()'],
                'nestjs': ['@nestjs', 'nest-cli.json', '@Controller'],
                'adonis': ['@adonisjs', 'ace', 'Route.get'],
                'meteor': ['meteor', '.meteor/', 'Meteor.methods'],
                'strapi': ['strapi', '@strapi/strapi'],
                'loopback': ['loopback', '@loopback/core'],

                # Java Frameworks
                'java': ['.java', 'pom.xml', 'build.gradle', 'public class'],
                'spring_boot': ['spring-boot', 'application.properties', '@SpringBootApplication'],
                'spring_mvc': ['spring-webmvc', '@Controller', '@RequestMapping'],
                'struts': ['struts', 'struts.xml', 'ActionSupport'],
                'jersey': ['jersey', 'javax.ws.rs', '@GET'],
                'play': ['play', 'application.conf', 'Action'],
                'dropwizard': ['dropwizard', 'Application'],
                'micronaut': ['micronaut', '@Controller'],
                'quarkus': ['quarkus', 'application.properties'],
                'helidon': ['helidon', 'io.helidon'],

                # C# Frameworks
                'csharp': ['.cs', '.csproj', 'appsettings.json', 'using System'],
                'aspnet_core': ['Microsoft.AspNetCore', 'Startup.cs', '[ApiController]'],
                'aspnet_mvc': ['System.Web.Mvc', '[Controller]', 'ActionResult'],
                'aspnet_webapi': ['System.Web.Http', '[HttpGet]', 'ApiController'],
                'nancy': ['Nancy', 'NancyModule'],
                'servicestack': ['ServiceStack', 'IService'],

                # Go Frameworks
                'go': ['.go', 'go.mod', 'go.sum', 'package main'],
                'gin': ['gin-gonic', 'gin.Default', 'router.GET'],
                'echo': ['labstack/echo', 'echo.New', 'GET'],
                'fiber': ['gofiber/fiber', 'fiber.New'],
                'beego': ['beego', 'beego.Router'],
                'revel': ['revel', 'revel.Controller'],
                'iris': ['kataras/iris', 'iris.New'],

                # Rust Frameworks
                'rust': ['.rs', 'Cargo.toml', 'Cargo.lock', 'fn main'],
                'actix_web': ['actix-web', 'HttpServer'],
                'rocket': ['rocket', '#[get]'],
                'warp': ['warp', 'warp::Filter'],
                'tide': ['tide', 'tide::Request'],
                'axum': ['axum', 'axum::Router'],

                # PHP Frameworks
                'php': ['.php', 'composer.json', '<?php'],
                'laravel': ['laravel', 'artisan', 'Illuminate\\'],
                'symfony': ['symfony', 'Symfony\\Component'],
                'codeigniter': ['CodeIgniter', 'CI_Controller'],
                'cakephp': ['cakephp', 'CakePHP'],
                'zend': ['zend', 'Zend\\Framework'],
                'yii': ['yii', 'CActiveRecord'],

                # Ruby Frameworks
                'ruby': ['.rb', 'Gemfile', 'require'],
                'rails': ['rails', 'config/routes.rb', 'ApplicationController'],
                'sinatra': ['sinatra', 'Sinatra::Base'],
                'padrino': ['padrino', 'Padrino::Application'],
                'hanami': ['hanami', 'Hanami::Action'],
                'grape': ['grape', 'Grape::API']
            },

            # ========== TESTING FRAMEWORKS ==========
            'testing': {
                # JavaScript Testing
                'jest': ['jest', 'jest.config.js', 'describe(', 'test('],
                'mocha': ['mocha', 'mocha.opts', 'describe(', 'it('],
                'jasmine': ['jasmine', 'jasmine.json', 'describe(', 'it('],
                'karma': ['karma', 'karma.conf.js', 'karma start'],
                'ava': ['ava', 'test(', 'import test from'],
                'tape': ['tape', 'test(', 'require("tape")'],
                'qunit': ['qunit', 'QUnit.test', 'QUnit.module'],

                # Python Testing
                'pytest': ['pytest', 'test_', '_test.py', 'def test_'],
                'unittest': ['unittest', 'TestCase', 'def test_'],
                'nose': ['nose', 'nosetests', '@with_setup'],
                'behave': ['behave', '.feature', 'Given', 'When', 'Then'],
                'robot': ['robot', '.robot', '*** Test Cases ***'],

                # Java Testing
                'junit': ['junit', 'test', '.java', '@Test'],
                'testng': ['testng', '@Test', 'TestNG'],
                'mockito': ['mockito', 'mock(', 'when('],
                'hamcrest': ['hamcrest', 'assertThat', 'is('],

                # C# Testing
                'nunit': ['NUnit', '[Test]', 'Assert.AreEqual'],
                'xunit': ['xUnit', '[Fact]', 'Assert.Equal'],
                'mstest': ['MSTest', '[TestMethod]', 'Assert.AreEqual'],

                # C++ Testing
                'gtest': ['gtest', 'googletest', 'TEST(', 'EXPECT_EQ'],
                'catch2': ['catch2', 'catch.hpp', 'TEST_CASE'],
                'boost_test': ['boost/test', 'BOOST_AUTO_TEST_CASE'],
                'cppunit': ['cppunit', 'CppUnit', 'CPPUNIT_TEST'],

                # Browser Testing
                'cypress': ['cypress', 'cypress.json', 'cy.visit'],
                'playwright': ['playwright', '@playwright', 'page.goto'],
                'selenium': ['selenium', 'webdriver', 'driver.get'],
                'puppeteer': ['puppeteer', 'puppeteer.launch'],
                'webdriverio': ['webdriverio', 'browser.url'],

                # Load Testing
                'jmeter': ['jmeter', '.jmx', 'TestPlan'],
                'k6': ['k6', 'import http from'],
                'locust': ['locust', 'HttpUser', '@task'],
                'gatling': ['gatling', '.scala', 'Simulation']
            },

            # ========== MOBILE DEVELOPMENT ==========
            'mobile': {
                # Native iOS
                'ios': ['ios', '.xcodeproj', 'Info.plist', 'UIViewController'],
                'swift': ['.swift', 'Package.swift', 'import UIKit'],
                'objective_c_ios': ['.m', '.mm', '@interface', 'UIKit/UIKit.h'],
                'swiftui': ['SwiftUI', '@State', '@ObservedObject'],

                # Native Android
                'android': ['android', 'build.gradle', 'AndroidManifest.xml', 'MainActivity'],
                'java_android': ['android', '.java', 'Activity', 'Intent'],
                'kotlin_android': ['android', '.kt', 'Activity', 'Intent'],
                'jetpack_compose': ['@Composable', 'androidx.compose'],

                # Cross-Platform
                'react_native': ['react-native', 'metro.config.js', 'React Native'],
                'flutter': ['flutter', 'pubspec.yaml', '.dart', 'StatelessWidget'],
                'xamarin': ['xamarin', '.xamarin', 'Xamarin.Forms'],
                'ionic': ['ionic', '@ionic', 'ion-content'],
                'cordova': ['cordova', 'config.xml', 'deviceready'],
                'phonegap': ['phonegap', 'pg-'],
                'nativescript': ['nativescript', 'tns-'],
                'unity_mobile': ['unity', 'Assets/', 'MonoBehaviour'],

                # Hybrid Frameworks
                'capacitor': ['capacitor', '@capacitor/core'],
                'quasar': ['quasar', 'quasar.conf.js'],
                'framework7': ['framework7', 'framework7-react'],
                'onsen_ui': ['onsen', 'onsenui']
            },

            # ========== AI & MACHINE LEARNING ==========
            'ai_ml': {
                # Deep Learning Frameworks
                'tensorflow': ['tensorflow', 'tf.', 'keras', 'import tensorflow'],
                'pytorch': ['pytorch', 'torch', 'torchvision', 'import torch'],
                'jax': ['jax', 'jax.numpy', 'import jax'],
                'mxnet': ['mxnet', 'mx.', 'import mxnet'],
                'caffe': ['caffe', 'caffe.proto', 'caffe/'],
                'theano': ['theano', 'theano.tensor'],
                'chainer': ['chainer', 'chainer.links'],
                'cntk': ['cntk', 'import cntk'],

                # ML Libraries
                'scikit_learn': ['sklearn', 'scikit-learn', 'from sklearn'],
                'pandas': ['pandas', 'pd.', 'import pandas'],
                'numpy': ['numpy', 'np.', 'import numpy'],
                'scipy': ['scipy', 'from scipy import'],
                'statsmodels': ['statsmodels', 'import statsmodels'],
                'xgboost': ['xgboost', 'xgb.', 'import xgboost'],
                'lightgbm': ['lightgbm', 'lgb.', 'import lightgbm'],
                'catboost': ['catboost', 'CatBoostRegressor'],

                # Computer Vision
                'opencv_ai': ['cv2', 'opencv-python', 'import cv2'],
                'pillow': ['PIL', 'Pillow', 'from PIL import'],
                'imageio': ['imageio', 'imread'],
                'skimage': ['skimage', 'from skimage import'],
                'albumentations': ['albumentations', 'import albumentations'],

                # NLP Libraries
                'nltk': ['nltk', 'import nltk'],
                'spacy': ['spacy', 'import spacy'],
                'gensim': ['gensim', 'from gensim import'],
                'transformers': ['transformers', 'huggingface', 'from transformers'],
                'bert': ['bert', 'BertModel'],
                'openai': ['openai', 'gpt-', 'import openai'],
                'anthropic': ['anthropic', 'claude', 'import anthropic'],

                # Jupyter & Notebooks
                'jupyter': ['jupyter', '.ipynb', 'nbconvert'],
                'ipython': ['ipython', 'IPython'],
                'google_colab': ['google.colab', 'from google.colab'],

                # Visualization
                'matplotlib': ['matplotlib', 'pyplot', 'import matplotlib'],
                'seaborn': ['seaborn', 'sns.', 'import seaborn'],
                'plotly': ['plotly', 'plotly.graph_objects'],
                'bokeh': ['bokeh', 'from bokeh import'],
                'altair': ['altair', 'import altair']
            },

            # ========== BLOCKCHAIN & WEB3 ==========
            'blockchain': {
                # Smart Contract Languages
                'solidity': ['.sol', 'pragma solidity', 'contract', 'function', 'mapping', 'address'],
                'vyper': ['.vy', 'vyper', '@public', '@internal', 'wei_value'],
                'move': ['.move', 'module', 'script', 'resource', 'Move.toml'],
                'ink': ['.rs', '#[ink::contract]', 'ink_lang', 'ink_storage'],
                'clarity': ['.clar', '(define-', 'stacks', 'clarity'],
                'cairo': ['.cairo', '%lang starknet', 'func', '@contract_interface'],
                'yul': ['.yul', 'object', 'code', 'datacopy'],

                # Blockchain Platforms
                'ethereum': ['ethereum', 'eth', 'web3.js', 'ethers.js', 'truffle', 'hardhat'],
                'bitcoin': ['bitcoin', 'btc', 'blockchain', 'satoshi', 'segwit'],
                'binance_smart_chain': ['bsc', 'binance', 'pancakeswap', 'bep20'],
                'polygon': ['polygon', 'matic', 'polygon-sdk'],
                'avalanche': ['avalanche', 'avax', 'subnet'],
                'solana': ['solana', 'sol', 'anchor', '@solana/web3.js'],
                'cardano': ['cardano', 'ada', 'plutus', 'marlowe'],
                'polkadot': ['polkadot', 'dot', 'substrate', 'kusama'],
                'cosmos': ['cosmos', 'atom', 'tendermint', 'cosmos-sdk'],
                'near': ['near', 'near-sdk', 'assemblyscript'],
                'starknet': ['starknet', 'cairo', 'starkware'],
                'tezos': ['tezos', 'xtz', 'ligo', 'michelson'],

                # Development Frameworks
                'truffle': ['truffle.js', 'truffle-config.js', 'migrations/', 'contracts/'],
                'hardhat': ['hardhat.config.js', 'hardhat.config.ts', '@nomiclabs/hardhat'],
                'foundry': ['foundry.toml', 'forge', 'cast', 'anvil'],
                'brownie': ['brownie-config.yaml', 'brownie', 'from brownie import'],
                'embark': ['embark.json', 'config/blockchain.js'],
                'waffle': ['@ethereum-waffle', 'waffle.json'],
                'ganache': ['ganache-cli', 'ganache', 'testrpc'],

                # Web3 Libraries
                'web3js': ['web3.js', 'web3', 'new Web3'],
                'ethersjs': ['ethers.js', 'ethers', 'ethers.provider'],
                'web3py': ['web3.py', 'from web3 import Web3'],
                'drizzle': ['drizzle', '@drizzle/store'],
                'moralis': ['moralis', 'Moralis.start'],

                # DeFi & dApps
                'defi': ['uniswap', 'compound', 'aave', 'yearn', 'dex', 'yield farming'],
                'nft': ['erc721', 'erc1155', 'opensea', 'nft', 'metadata'],
                'dao': ['dao', 'governance', 'voting', 'multisig'],
                'oracle': ['chainlink', 'oracle', 'price feed'],

                # Crypto Libraries
                'cryptography_blockchain': ['secp256k1', 'bip39', 'hdwallet', 'merkle tree'],
                'ipfs': ['ipfs', 'ipfs-api', 'pinata', 'filecoin']
            },

            # ========== CLOUD & INFRASTRUCTURE (Enhanced) ==========
            'cloud_infrastructure': {
                # Cloud Providers
                'aws': ['aws-cli', 'boto3', 'lambda', 's3', 'ec2', 'cloudformation', 'aws-sdk'],
                'azure': ['azure-cli', 'az', 'azure-functions', 'azure-storage', '@azure/'],
                'gcp': ['gcloud', 'google-cloud', 'app-engine', 'cloud-functions', 'firebase'],
                'alibaba_cloud': ['aliyun', 'alicloud', 'oss', 'ecs'],
                'oracle_cloud': ['oci', 'oracle-cloud', 'oci-cli'],
                'ibm_cloud': ['ibm-cloud', 'watson', 'cloudant'],
                'digitalocean': ['digitalocean', 'doctl', 'droplet'],
                'linode': ['linode', 'linode-cli'],
                'vultr': ['vultr', 'vultr-cli'],

                # Container Orchestration
                'kubernetes': ['kubernetes', 'kubectl', 'k8s', 'deployment.yaml', 'service.yaml'],
                'helm': ['helm', 'Chart.yaml', 'values.yaml', 'templates/'],
                'istio': ['istio', 'virtualservice', 'destinationrule', 'gateway'],
                'linkerd': ['linkerd', 'linkerd.io', 'l5d'],
                'consul': ['consul', 'consul-template', 'service mesh'],
                'nomad': ['nomad', 'nomad.hcl', 'job'],
                'rancher': ['rancher', 'cattle', 'rke'],
                'openshift': ['openshift', 'oc', 'red hat'],

                # Infrastructure as Code
                'terraform': ['terraform', '.tf', 'main.tf', 'provider', 'resource'],
                'pulumi': ['pulumi', 'Pulumi.yaml', '@pulumi/'],
                'cloudformation': ['cloudformation', '.yaml', 'AWSTemplateFormatVersion'],
                'arm_templates': ['azuredeploy.json', 'Microsoft.Resources'],
                'cdk': ['aws-cdk', '@aws-cdk/', 'cdk.json'],
                'ansible': ['ansible', 'playbook.yml', 'hosts', 'roles/'],
                'chef': ['chef', 'cookbook', 'recipe', 'Berksfile'],
                'puppet': ['puppet', '.pp', 'manifests/', 'Puppetfile'],
                'salt': ['salt', 'saltstack', '.sls', 'pillar/'],

                # Monitoring & Observability
                'prometheus': ['prometheus', 'prometheus.yml', 'metrics'],
                'grafana': ['grafana', 'dashboard.json', 'datasource'],
                'jaeger': ['jaeger', 'tracing', 'opentelemetry'],
                'zipkin': ['zipkin', 'zipkin-server'],
                'datadog': ['datadog', 'dd-agent', 'datadog.yaml'],
                'new_relic': ['newrelic', 'new-relic', 'nr-agent'],
                'elastic_stack': ['elasticsearch', 'logstash', 'kibana', 'beats'],
                'splunk': ['splunk', 'splunkd', 'splunk-forwarder'],
                'dynatrace': ['dynatrace', 'oneagent'],

                # CI/CD Platforms
                'jenkins': ['Jenkinsfile', 'jenkins', 'pipeline'],
                'gitlab_ci': ['.gitlab-ci.yml', 'gitlab-runner'],
                'github_actions': ['.github/workflows/', 'github-actions'],
                'azure_devops': ['azure-pipelines.yml', 'azure-devops'],
                'teamcity': ['teamcity', '.teamcity/'],
                'bamboo': ['bamboo', 'bamboo-specs'],
                'circleci': ['.circleci/config.yml', 'circleci'],
                'travis': ['.travis.yml', 'travis-ci'],

                # Serverless
                'serverless_framework': ['serverless.yml', 'serverless', 'sls'],
                'lambda': ['aws-lambda', 'lambda_function.py', 'handler'],
                'azure_functions': ['function.json', 'host.json', 'azure-functions'],
                'cloud_functions': ['functions-framework', 'cloud-functions'],
                'vercel': ['vercel.json', 'vercel', 'now.json'],
                'netlify': ['netlify.toml', '_redirects', 'netlify-lambda'],

                # Load Balancers & CDN
                'cloudflare': ['cloudflare', 'cf-', 'workers'],
                'fastly': ['fastly', 'vcl'],
                'cloudfront': ['cloudfront', 'distribution'],
                'nginx_plus': ['nginx-plus', 'nginx+'],
                'f5': ['f5', 'big-ip', 'ltm']
            },

            # ========== CYBERSECURITY TOOLS ==========
            'cybersecurity': {
                # Security Frameworks
                'owasp': ['owasp', 'owasp-zap', 'dependency-check'],
                'nist': ['nist', 'cybersecurity framework', 'csf'],
                'iso27001': ['iso27001', 'iso 27001', 'isms'],
                'cis': ['cis controls', 'cis benchmark'],
                'sans': ['sans', 'sans framework'],

                # Vulnerability Scanning
                'nessus': ['nessus', '.nessus', 'tenable'],
                'openvas': ['openvas', 'gvm', 'greenbone'],
                'qualys': ['qualys', 'vmdr', 'was'],
                'rapid7': ['nexpose', 'insightvm', 'metasploit'],
                'acunetix': ['acunetix', 'web vulnerability'],
                'checkmarx': ['checkmarx', 'sast', 'static analysis'],
                'veracode': ['veracode', 'static analysis'],
                'sonarqube': ['sonarqube', 'sonar-scanner', 'code quality'],

                # Penetration Testing
                'metasploit': ['metasploit', 'msfconsole', 'exploit'],
                'burp_suite': ['burp', 'burp suite', 'portswigger'],
                'nmap': ['nmap', 'nmap-scripts', 'port scan'],
                'wireshark': ['wireshark', 'tshark', 'packet capture'],
                'aircrack': ['aircrack-ng', 'wifi security'],
                'john_the_ripper': ['john', 'password cracking'],
                'hashcat': ['hashcat', 'hash cracking'],
                'hydra': ['hydra', 'brute force'],
                'sqlmap': ['sqlmap', 'sql injection'],
                'nikto': ['nikto', 'web scanner'],
                'gobuster': ['gobuster', 'directory brute'],
                'ffuf': ['ffuf', 'fuzzing'],

                # SIEM & Log Analysis
                'splunk_security': ['splunk', 'splunk enterprise security'],
                'elk_security': ['elasticsearch', 'elastic security'],
                'qradar': ['qradar', 'ibm security'],
                'sentinel': ['azure sentinel', 'microsoft sentinel'],
                'arcsight': ['arcsight', 'micro focus'],
                'logrhythm': ['logrhythm', 'siem'],
                'phantom': ['phantom', 'soar'],
                'demisto': ['demisto', 'cortex xsoar'],

                # Endpoint Security
                'antivirus': ['antivirus', 'endpoint protection'],
                'edr': ['edr', 'endpoint detection'],
                'crowdstrike': ['crowdstrike', 'falcon'],
                'carbon_black': ['carbon black', 'cb response'],
                'cylance': ['cylance', 'ai antivirus'],
                'symantec': ['symantec', 'norton'],
                'mcafee': ['mcafee', 'trellix'],

                # Cryptography & PKI
                'openssl': ['openssl', 'ssl', 'tls'],
                'libsodium': ['libsodium', 'nacl', 'crypto'],
                'bouncy_castle': ['bouncy castle', 'bc-java'],
                'let_encrypt': ['letsencrypt', 'certbot', 'acme'],
                'pki': ['pki', 'certificate authority', 'x509'],
                'pgp': ['pgp', 'gpg', 'gnupg'],
                'yubikey': ['yubikey', 'fido2', 'u2f'],

                # Network Security
                'firewall': ['iptables', 'pf', 'ufw', 'firewalld'],
                'ids_ips': ['snort', 'suricata', 'zeek', 'bro'],
                'vpn': ['openvpn', 'wireguard', 'ipsec'],
                'proxy': ['squid', 'haproxy', 'nginx proxy'],
                'waf': ['modsecurity', 'cloudflare waf', 'aws waf'],

                # Compliance & Audit
                'pci_dss': ['pci', 'payment card', 'compliance'],
                'gdpr': ['gdpr', 'data protection', 'privacy'],
                'hipaa': ['hipaa', 'healthcare', 'phi'],
                'sox': ['sarbanes oxley', 'sox', 'financial'],
                'audit': ['audit trail', 'compliance audit']
            },

            # ========== MULTIMEDIA & AUDIO/VIDEO ==========
            'multimedia': {
                # Audio Processing
                'fmod': ['fmod', 'fmod_studio', 'FMOD_System'],
                'openal': ['openal', 'AL_', 'alc', 'OpenAL32'],
                'portaudio': ['portaudio', 'Pa_', 'portaudio.h'],
                'jack': ['jack', 'jack_client', 'libjack'],
                'alsa': ['alsa', 'snd_', 'asoundlib.h'],
                'pulse_audio': ['pulseaudio', 'pa_', 'pulse/'],
                'coreaudio': ['coreaudio', 'AudioUnit', 'AudioToolbox'],
                'wasapi': ['wasapi', 'IAudioClient', 'mmdeviceapi'],
                'rtaudio': ['rtaudio', 'RtAudio', 'rtaudio.h'],
                'waveform': ['wave', 'wav', 'audio waveform'],

                # Audio Libraries & Formats
                'libsndfile': ['libsndfile', 'sndfile.h', 'sf_'],
                'flac': ['flac', 'libflac', 'FLAC__'],
                'ogg_vorbis': ['ogg', 'vorbis', 'oggvorbis'],
                'opus': ['opus', 'libopus', 'opus_'],
                'mp3lame': ['lame', 'mp3lame', 'lame_'],
                'aac': ['aac', 'faac', 'libfaac'],
                'speex': ['speex', 'libspeex'],

                # Video Processing
                'ffmpeg': ['ffmpeg', 'libav', 'avcodec', 'avformat'],
                'gstreamer': ['gstreamer', 'gst-', 'GstElement'],
                'opencv_video': ['opencv', 'cv2', 'VideoCapture', 'VideoWriter'],
                'directshow': ['directshow', 'IBaseFilter', 'IMediaControl'],
                'media_foundation': ['media foundation', 'IMFMediaSource'],
                'avfoundation': ['avfoundation', 'AVPlayer', 'AVCaptureSession'],
                'quicktime': ['quicktime', 'QTKit', 'QuickTime.h'],
                'vlc': ['vlc', 'libvlc', 'vlc_'],

                # Video Formats & Codecs
                'h264': ['h264', 'x264', 'avc'],
                'h265': ['h265', 'x265', 'hevc'],
                'vp8': ['vp8', 'libvpx'],
                'vp9': ['vp9', 'libvpx'],
                'av1': ['av1', 'libaom', 'dav1d'],
                'theora': ['theora', 'libtheora'],

                # Streaming & Broadcasting
                'webrtc': ['webrtc', 'peerconnection', 'mediastream'],
                'rtmp': ['rtmp', 'librtmp', 'live streaming'],
                'hls': ['hls', 'm3u8', 'http live streaming'],
                'dash': ['dash', 'mpeg-dash', 'mpd'],
                'rtp': ['rtp', 'rtcp', 'real-time protocol'],
                'srt': ['srt', 'secure reliable transport'],
                'obs': ['obs', 'obs studio', 'streaming'],
                'wowza': ['wowza', 'streaming engine'],

                # Image Processing (Extended)
                'imagemagick_extended': ['imagemagick', 'magick++', 'convert'],
                'graphicsmagick': ['graphicsmagick', 'gm'],
                'pil_extended': ['pillow', 'pil', 'image processing'],
                'gimp': ['gimp', 'xcf', 'gimp plugin'],
                'photoshop': ['photoshop', 'psd', 'adobe'],

                # 3D Audio
                'steam_audio': ['steam audio', 'phonon'],
                'oculus_audio': ['oculus audio', 'ovr audio'],
                'resonance_audio': ['resonance audio', 'google spatial'],
                'wwise': ['wwise', 'ak_', 'audiokinetic'],

                # Media Servers
                'plex': ['plex', 'plex media server'],
                'emby': ['emby', 'emby server'],
                'jellyfin': ['jellyfin', 'jellyfin server'],
                'kodi': ['kodi', 'xbmc'],

                # Multimedia Frameworks
                'unity_audio': ['unity', 'AudioSource', 'AudioClip'],
                'unreal_audio': ['unreal', 'USoundWave', 'FAudioDevice'],
                'cef': ['cef', 'chromium embedded'],
                'electron_media': ['electron', 'webcontents', 'media']
            },

            # ========== QUANTUM COMPUTING ==========
            'quantum': {
                # Quantum Languages
                'qsharp': ['.qs', 'qsharp', 'Q#', 'Microsoft.Quantum'],
                'qasm': ['.qasm', 'openqasm', 'qreg', 'creg'],
                'quipper': ['.quip', 'quipper', 'quantum lambda'],
                'silq': ['.slq', 'silq', 'quantum programming'],

                # Quantum Frameworks
                'qiskit': ['qiskit', 'from qiskit import', 'QuantumCircuit'],
                'cirq': ['cirq', 'import cirq', 'cirq.Circuit'],
                'pennylane': ['pennylane', 'import pennylane', '@qml.qnode'],
                'forest': ['pyquil', 'forest', 'rigetti'],
                'strawberry_fields': ['strawberryfields', 'photonic quantum'],
                'qutip': ['qutip', 'quantum toolbox', 'Qobj'],
                'quantum_inspire': ['quantuminspire', 'quantum inspire'],

                # Quantum Cloud Platforms
                'ibm_quantum': ['ibm quantum', 'qiskit-ibmq-provider'],
                'aws_braket': ['aws braket', 'braket', 'amazon quantum'],
                'google_quantum': ['google quantum', 'cirq-google'],
                'azure_quantum': ['azure quantum', 'microsoft quantum'],
                'rigetti_cloud': ['rigetti', 'qcs', 'quantum cloud'],
                'ionq': ['ionq', 'ionq quantum'],
                'xanadu': ['xanadu', 'pennylane-xanadu'],

                # Quantum Simulators
                'quantum_simulator': ['quantum simulator', 'state vector'],
                'noise_simulation': ['noise model', 'quantum noise'],
                'quantum_annealing': ['dwave', 'quantum annealing', 'qubo'],
                'adiabatic_quantum': ['adiabatic', 'quantum adiabatic'],

                # Quantum Algorithms
                'quantum_algorithms': ['shor', 'grover', 'quantum fourier'],
                'vqe': ['vqe', 'variational quantum eigensolver'],
                'qaoa': ['qaoa', 'quantum approximate optimization'],
                'quantum_ml': ['quantum machine learning', 'qml'],

                # Quantum Hardware
                'superconducting': ['superconducting', 'transmon', 'flux'],
                'trapped_ion': ['trapped ion', 'ion trap'],
                'photonic': ['photonic', 'linear optics'],
                'neutral_atom': ['neutral atom', 'cold atom'],
                'topological': ['topological', 'majorana'],

                # Quantum Development Tools
                'quantum_dev': ['quantum development kit', 'qdk'],
                'quantum_composer': ['quantum composer', 'circuit composer'],
                'quantum_lab': ['quantum lab', 'jupyter quantum'],
                'quantum_visualization': ['quantum visualization', 'bloch sphere']
            }
        }

    def detect_technology_stack(self, project_path: str) -> TechnologyStack:
        """
        Detect technology stack across all supported categories

        Args:
            project_path: Path to project directory

        Returns:
            TechnologyStack with detected technologies and confidence scores
        """
        logger.info(f"Detecting technology stack for project: {project_path}")

        # Initialize detection results for all comprehensive categories
        detected = {category: [] for category in self.technology_patterns.keys()}
        confidence_scores = []

        try:
            # Walk through project directory
            for root, dirs, files in os.walk(project_path):
                # Skip common ignore directories
                dirs[:] = [d for d in dirs if not d.startswith('.')
                          and d not in ['node_modules', '__pycache__', 'venv', 'env', 'target', 'build']]

                for file in files:
                    file_path = os.path.join(root, file)
                    self._analyze_file(file_path, file, detected)

            # Additional analysis methods
            self._analyze_package_files(project_path, detected)
            self._analyze_configuration_files(project_path, detected)
            self._analyze_directory_structure(project_path, detected)

            # Calculate confidence score based on detection strength
            total_detections = sum(len(techs) for techs in detected.values())
            confidence_score = min(1.0, total_detections / 20.0)  # Normalize to 0-1

            logger.info(f"Technology detection completed. Found {total_detections} technologies.")

            # Map new comprehensive categories to TechnologyStack structure
            return TechnologyStack(
                frontend=detected.get('frontend', []) + detected.get('gui_frameworks', [])[:5],
                backend=detected.get('backend', []) + detected.get('backend_architectures', [])[:5] + detected.get('languages', [])[:10],
                database=detected.get('database', []),
                infrastructure=detected.get('build_systems', []) + detected.get('backend_architectures', [])[:3] + detected.get('cloud_infrastructure', [])[:5],
                testing=detected.get('testing', []),
                mobile=detected.get('mobile', []),
                desktop=detected.get('gui_frameworks', []) + detected.get('desktop_specific', []) + detected.get('build_systems', [])[:3],
                graphics=detected.get('graphics', []) + detected.get('scientific', [])[:3],
                ai_ml=detected.get('ai_ml', []) + detected.get('scientific', [])[:5] + detected.get('quantum', [])[:3],
                blockchain=detected.get('blockchain', []),
                cloud_infrastructure=detected.get('cloud_infrastructure', []),
                cybersecurity=detected.get('cybersecurity', []),
                multimedia=detected.get('multimedia', []),
                quantum=detected.get('quantum', []),
                confidence_score=confidence_score
            )

        except Exception as e:
            logger.error(f"Error detecting technology stack: {e}")
            # Return empty stack with low confidence
            return TechnologyStack(
                frontend=[], backend=[], database=[], infrastructure=[],
                testing=[], mobile=[], desktop=[], graphics=[], ai_ml=[],
                blockchain=[], cloud_infrastructure=[], cybersecurity=[],
                multimedia=[], quantum=[], confidence_score=0.0
            )

    def _analyze_file(self, file_path: str, filename: str, detected: Dict[str, List[str]]):
        """Analyze individual file for technology indicators"""
        try:
            # Check file extension and name patterns
            for category, technologies in self.technology_patterns.items():
                for tech, patterns in technologies.items():
                    for pattern in patterns:
                        if pattern in filename.lower() or filename.lower().endswith(pattern):
                            if tech not in detected[category]:
                                detected[category].append(tech)
                                logger.debug(f"Detected {tech} from file: {filename}")

            # For text files, check content for technology keywords
            if filename.lower().endswith(('.py', '.js', '.ts', '.java', '.cs', '.go', '.rs', '.php', '.rb', '.cpp', '.c', '.h', '.hpp', '.cc', '.cxx')):
                self._analyze_file_content(file_path, detected)

        except Exception as e:
            logger.debug(f"Error analyzing file {filename}: {e}")

    def _analyze_file_content(self, file_path: str, detected: Dict[str, List[str]]):
        """Analyze file content for technology imports and usage"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()

                # Look for import statements and technology usage
                for category, technologies in self.technology_patterns.items():
                    for tech, patterns in technologies.items():
                        for pattern in patterns:
                            if pattern.lower() in content:
                                if tech not in detected[category]:
                                    detected[category].append(tech)
                                    logger.debug(f"Detected {tech} from content in: {file_path}")

        except Exception as e:
            logger.debug(f"Error reading file content {file_path}: {e}")

    def _analyze_package_files(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze package configuration files for dependencies"""
        package_files = {
            'package.json': 'nodejs',
            'requirements.txt': 'python',
            'Pipfile': 'python',
            'setup.py': 'python',
            'pyproject.toml': 'python',
            'pom.xml': 'java',
            'build.gradle': 'java',
            'Cargo.toml': 'rust',
            'go.mod': 'go',
            'composer.json': 'php',
            'Gemfile': 'ruby'
        }

        for filename, tech in package_files.items():
            file_path = os.path.join(project_path, filename)
            if os.path.exists(file_path):
                if tech not in detected['backend']:
                    detected['backend'].append(tech)
                    logger.debug(f"Detected {tech} from package file: {filename}")

                # Analyze package dependencies
                self._analyze_dependency_file(file_path, detected)

    def _analyze_dependency_file(self, file_path: str, detected: Dict[str, List[str]]):
        """Analyze dependency files for technology clues"""
        try:
            filename = os.path.basename(file_path)

            if filename == 'package.json':
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    dependencies = {**data.get('dependencies', {}), **data.get('devDependencies', {})}

                    # Map common npm packages to technologies
                    npm_tech_mapping = {
                        'react': 'react', 'angular': 'angular', 'vue': 'vue',
                        'express': 'express', 'fastify': 'fastify', 'koa': 'koa',
                        'typescript': 'typescript', 'webpack': 'webpack', 'vite': 'vite',
                        'jest': 'jest', 'cypress': 'cypress', 'playwright': 'playwright',
                        'electron': 'electron', 'react-native': 'react_native'
                    }

                    for dep in dependencies:
                        for pattern, tech in npm_tech_mapping.items():
                            if pattern in dep.lower():
                                category = self._get_tech_category(tech)
                                if category and tech not in detected[category]:
                                    detected[category].append(tech)

        except Exception as e:
            logger.debug(f"Error analyzing dependency file {file_path}: {e}")

    def _analyze_configuration_files(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze configuration files for technology indicators"""
        config_files = [
            'docker-compose.yml', 'Dockerfile', '.dockerignore',
            'kubernetes.yaml', 'k8s.yaml', 'deployment.yaml',
            'terraform.tf', 'main.tf',
            '.github/workflows/', '.gitlab-ci.yml',
            'nginx.conf', 'apache.conf',
            'jest.config.js', 'cypress.json', 'pytest.ini'
        ]

        for config_file in config_files:
            config_path = os.path.join(project_path, config_file)
            if os.path.exists(config_path) or os.path.isdir(config_path):
                # Map config files to technologies
                self._map_config_to_technology(config_file, detected)

    def _analyze_directory_structure(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze directory structure for technology patterns"""
        common_directories = {
            'src/main/java': 'java',
            'src/main/resources': 'java',
            'Assets/': 'unity',
            'Source/': 'unreal',
            'www/': 'php',
            'public/': 'frontend',
            'static/': 'frontend',
            'templates/': 'backend',
            'migrations/': 'database',
            'tests/': 'testing',
            '__tests__/': 'testing'
        }

        for root, dirs, files in os.walk(project_path):
            rel_path = os.path.relpath(root, project_path)
            for dir_pattern, tech in common_directories.items():
                if dir_pattern in rel_path:
                    category = self._get_tech_category(tech)
                    if category and tech not in detected[category]:
                        detected[category].append(tech)

    def _get_tech_category(self, tech: str) -> Optional[str]:
        """Get the category for a given technology - maps to TechnologyStack fields"""
        # Create mapping from comprehensive categories to TechnologyStack fields
        category_mapping = {
            'languages': 'backend',
            'gui_frameworks': 'desktop',
            'backend_architectures': 'infrastructure',
            'database': 'database',
            'desktop_specific': 'desktop',
            'build_systems': 'infrastructure',
            'graphics': 'graphics',
            'scientific': 'ai_ml',
            'embedded': 'infrastructure',
            'frontend': 'frontend',
            'backend': 'backend',
            'testing': 'testing',
            'mobile': 'mobile',
            'ai_ml': 'ai_ml'
        }

        for category, technologies in self.technology_patterns.items():
            if tech in technologies:
                return category_mapping.get(category, category)
        return None

    def _map_config_to_technology(self, config_file: str, detected: Dict[str, List[str]]):
        """Map configuration files to their corresponding technologies"""
        config_mapping = {
            'docker': 'docker',
            'kubernetes': 'kubernetes', 'k8s': 'kubernetes',
            'terraform': 'terraform',
            'github': 'github_actions',
            'gitlab': 'gitlab_ci',
            'nginx': 'nginx',
            'apache': 'apache',
            'jest': 'jest',
            'cypress': 'cypress',
            'pytest': 'pytest'
        }

        for pattern, tech in config_mapping.items():
            if pattern in config_file.lower():
                category = self._get_tech_category(tech)
                if category and tech not in detected[category]:
                    detected[category].append(tech)

class ProjectComplexityAnalyzer:
    """Analyze project complexity metrics"""

    def analyze_complexity(self, project_path: str) -> ProjectComplexity:
        """
        Analyze project complexity across multiple dimensions

        Args:
            project_path: Path to project directory

        Returns:
            ProjectComplexity with comprehensive complexity assessment
        """
        logger.info(f"Analyzing project complexity for: {project_path}")

        try:
            file_count = self._count_project_files(project_path)
            code_lines = self._count_code_lines(project_path)
            directory_depth = self._calculate_directory_depth(project_path)
            dependency_count = self._count_dependencies(project_path)

            # Calculate overall complexity score (0-1 scale)
            complexity_score = self._calculate_complexity_score(
                file_count, code_lines, directory_depth, dependency_count
            )

            # Determine complexity rating
            complexity_rating = self._determine_complexity_rating(complexity_score)

            logger.info(f"Complexity analysis complete: {complexity_rating} ({complexity_score:.2f})")

            return ProjectComplexity(
                file_count=file_count,
                code_lines=code_lines,
                directory_depth=directory_depth,
                dependency_count=dependency_count,
                complexity_rating=complexity_rating,
                complexity_score=complexity_score
            )

        except Exception as e:
            logger.error(f"Error analyzing project complexity: {e}")
            return ProjectComplexity(
                file_count=0, code_lines=0, directory_depth=0,
                dependency_count=0, complexity_rating="unknown", complexity_score=0.0
            )

    def _count_project_files(self, project_path: str) -> int:
        """Count relevant project files (excluding generated/cache files)"""
        count = 0
        exclude_patterns = {
            'node_modules', '__pycache__', '.git', 'venv', 'env',
            'target', 'build', 'dist', '.cache', 'coverage'
        }

        for root, dirs, files in os.walk(project_path):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_patterns]

            # Count relevant files
            for file in files:
                if not file.startswith('.') and not file.endswith(('.log', '.tmp')):
                    count += 1

        return count

    def _count_code_lines(self, project_path: str) -> int:
        """Count lines of code in relevant source files"""
        code_extensions = {
            '.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.cs', '.go',
            '.rs', '.php', '.rb', '.cpp', '.c', '.h', '.hpp', '.swift',
            '.kt', '.scala', '.clj', '.dart', '.vue', '.html', '.css',
            '.scss', '.sass', '.less', '.sql', '.yaml', '.yml', '.json'
        }

        total_lines = 0
        exclude_dirs = {'node_modules', '__pycache__', '.git', 'venv', 'target', 'build'}

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if any(file.lower().endswith(ext) for ext in code_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            total_lines += sum(1 for line in f if line.strip())
                    except Exception:
                        continue

        return total_lines

    def _calculate_directory_depth(self, project_path: str) -> int:
        """Calculate maximum directory depth"""
        max_depth = 0
        exclude_dirs = {'node_modules', '__pycache__', '.git', 'venv', 'target', 'build'}

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            relative_path = os.path.relpath(root, project_path)
            if relative_path != '.':
                depth = len(relative_path.split(os.sep))
                max_depth = max(max_depth, depth)

        return max_depth

    def _count_dependencies(self, project_path: str) -> int:
        """Count external dependencies from package files"""
        dependency_count = 0

        # Node.js dependencies
        package_json = os.path.join(project_path, 'package.json')
        if os.path.exists(package_json):
            try:
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    dependency_count += len(data.get('dependencies', {}))
                    dependency_count += len(data.get('devDependencies', {}))
            except Exception:
                pass

        # Python dependencies
        requirements_txt = os.path.join(project_path, 'requirements.txt')
        if os.path.exists(requirements_txt):
            try:
                with open(requirements_txt, 'r') as f:
                    dependency_count += len([line for line in f if line.strip() and not line.startswith('#')])
            except Exception:
                pass

        # Add other package managers as needed (Maven, Gradle, Cargo, etc.)

        return dependency_count

    def _calculate_complexity_score(self, file_count: int, code_lines: int,
                                  directory_depth: int, dependency_count: int) -> float:
        """Calculate normalized complexity score (0-1)"""
        # Normalize each metric to 0-1 scale
        file_score = min(1.0, file_count / 1000.0)  # 1000+ files = max
        lines_score = min(1.0, code_lines / 50000.0)  # 50k+ lines = max
        depth_score = min(1.0, directory_depth / 10.0)  # 10+ levels = max
        deps_score = min(1.0, dependency_count / 100.0)  # 100+ deps = max

        # Weighted combination
        return (file_score * 0.3 + lines_score * 0.4 +
                depth_score * 0.1 + deps_score * 0.2)

    def _determine_complexity_rating(self, complexity_score: float) -> str:
        """Determine complexity rating based on score"""
        if complexity_score < 0.3:
            return "startup"
        elif complexity_score < 0.7:
            return "sme"
        else:
            return "enterprise"

class BusinessDomainClassifier:
    """Classify project business domain and requirements"""

    def __init__(self):
        self.domain_keywords = {
            'fintech': ['bank', 'payment', 'finance', 'trading', 'crypto', 'wallet', 'loan'],
            'healthcare': ['medical', 'health', 'patient', 'clinic', 'hospital', 'pharma'],
            'ecommerce': ['shop', 'cart', 'product', 'order', 'inventory', 'payment'],
            'education': ['school', 'student', 'course', 'learn', 'university', 'grade'],
            'gaming': ['game', 'player', 'score', 'level', 'unity', 'unreal'],
            'social': ['social', 'chat', 'message', 'friend', 'post', 'feed'],
            'enterprise': ['crm', 'erp', 'workflow', 'business', 'employee', 'hr'],
            'api_integration': ['api', 'integration', 'webhook', 'service', 'microservice'],
            'data_analytics': ['analytics', 'dashboard', 'report', 'metric', 'bi', 'data'],
            'iot': ['sensor', 'device', 'iot', 'arduino', 'raspberry', 'embedded'],
            'ai_ml': ['ml', 'ai', 'model', 'training', 'neural', 'algorithm'],
            'devtools': ['tool', 'cli', 'framework', 'library', 'sdk', 'api']
        }

        self.compliance_indicators = {
            'gdpr': ['privacy', 'consent', 'gdpr', 'data protection'],
            'hipaa': ['hipaa', 'medical', 'health', 'patient'],
            'pci_dss': ['payment', 'card', 'pci', 'finance'],
            'sox': ['financial', 'audit', 'sox', 'sarbanes'],
            'iso27001': ['security', 'iso', 'information security']
        }

    def classify_domain(self, project_path: str) -> BusinessDomain:
        """
        Classify business domain based on project content analysis

        Args:
            project_path: Path to project directory

        Returns:
            BusinessDomain with classification and confidence score
        """
        logger.info(f"Classifying business domain for: {project_path}")

        try:
            # Analyze project content for domain indicators
            content_analysis = self._analyze_project_content(project_path)
            domain_scores = self._calculate_domain_scores(content_analysis)
            compliance_reqs = self._identify_compliance_requirements(content_analysis)

            # Determine primary and secondary domains
            primary_domain = max(domain_scores.items(), key=lambda x: x[1])[0] if domain_scores else 'general'
            secondary_domains = [domain for domain, score in domain_scores.items()
                               if score > 0.3 and domain != primary_domain]

            # Determine industry vertical
            industry_vertical = self._determine_industry_vertical(primary_domain, secondary_domains)

            # Calculate confidence score
            confidence_score = domain_scores.get(primary_domain, 0.0) if domain_scores else 0.1

            logger.info(f"Domain classification complete: {primary_domain} ({confidence_score:.2f})")

            return BusinessDomain(
                primary=primary_domain,
                secondary=secondary_domains,
                industry_vertical=industry_vertical,
                compliance_requirements=compliance_reqs,
                confidence_score=confidence_score
            )

        except Exception as e:
            logger.error(f"Error classifying business domain: {e}")
            return BusinessDomain(
                primary="general", secondary=[], industry_vertical="technology",
                compliance_requirements=[], confidence_score=0.1
            )

    def _analyze_project_content(self, project_path: str) -> Dict[str, int]:
        """Analyze project content for domain keywords"""
        keyword_counts = {}
        text_files = ['.md', '.txt', '.rst', '.json', '.yaml', '.yml']
        code_files = ['.py', '.js', '.ts', '.java', '.cs', '.go', '.rs', '.php', '.rb']

        for root, dirs, files in os.walk(project_path):
            # Skip common ignore directories
            dirs[:] = [d for d in dirs if not d.startswith('.')
                      and d not in ['node_modules', '__pycache__', 'venv']]

            for file in files:
                if any(file.lower().endswith(ext) for ext in text_files + code_files):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()

                            # Count domain keywords
                            for domain, keywords in self.domain_keywords.items():
                                for keyword in keywords:
                                    count = content.count(keyword)
                                    if count > 0:
                                        keyword_counts[keyword] = keyword_counts.get(keyword, 0) + count
                    except Exception:
                        continue

        return keyword_counts

    def _calculate_domain_scores(self, content_analysis: Dict[str, int]) -> Dict[str, float]:
        """Calculate domain scores based on keyword frequency"""
        domain_scores = {}

        for domain, keywords in self.domain_keywords.items():
            total_score = 0
            for keyword in keywords:
                if keyword in content_analysis:
                    # Weight score by keyword frequency and specificity
                    score = content_analysis[keyword] * (1.0 / len(keywords))
                    total_score += score

            # Normalize score (0-1 scale)
            if total_score > 0:
                domain_scores[domain] = min(1.0, total_score / 10.0)

        return domain_scores

    def _identify_compliance_requirements(self, content_analysis: Dict[str, int]) -> List[str]:
        """Identify compliance requirements based on content analysis"""
        compliance_reqs = []

        for compliance, indicators in self.compliance_indicators.items():
            for indicator in indicators:
                if indicator in content_analysis and content_analysis[indicator] > 0:
                    if compliance not in compliance_reqs:
                        compliance_reqs.append(compliance)
                    break

        return compliance_reqs

    def _determine_industry_vertical(self, primary_domain: str, secondary_domains: List[str]) -> str:
        """Determine industry vertical based on domain classification"""
        industry_mapping = {
            'fintech': 'financial_services',
            'healthcare': 'healthcare',
            'ecommerce': 'retail',
            'education': 'education',
            'gaming': 'entertainment',
            'social': 'social_media',
            'enterprise': 'enterprise_software',
            'api_integration': 'technology',
            'data_analytics': 'technology',
            'iot': 'manufacturing',
            'ai_ml': 'technology',
            'devtools': 'technology'
        }

        return industry_mapping.get(primary_domain, 'technology')

class TeamContextAnalyzer:
    """Analyze team and development context"""

    def analyze_team_context(self, project_path: str) -> TeamContext:
        """
        Analyze team context from project indicators with circuit breaker

        Args:
            project_path: Path to project directory

        Returns:
            TeamContext with team size, experience, and patterns
        """
        logger.info(f"Analyzing team context for: {project_path}")

        # Circuit breaker - maximum 30 seconds for entire team analysis
        import signal
        import time

        def timeout_handler(signum, frame):
            raise TimeoutError("Team context analysis timed out after 30 seconds")

        # Set up timeout circuit breaker
        start_time = time.time()
        original_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(30)  # 30 second timeout

        try:
            # Optimized analysis with early exit capabilities
            git_analysis = {}
            code_quality_indicators = []
            project_structure_analysis = {}

            # Phase 1: Quick git analysis (max 10s already handled in function)
            try:
                git_analysis = self._analyze_git_activity(project_path)
            except Exception as e:
                logger.warning(f"Git analysis failed, using defaults: {e}")
                git_analysis = {'commit_count': 0, 'contributor_count': 0, 'recent_activity': False}

            # Phase 2: Code quality analysis (optimized to single pass)
            try:
                code_quality_indicators = self._analyze_code_quality_indicators(project_path)
            except Exception as e:
                logger.warning(f"Code quality analysis failed, using basic fallback: {e}")
                code_quality_indicators = self._basic_quality_check(project_path)

            # Phase 3: Project structure (lightweight, no heavy operations)
            try:
                project_structure_analysis = self._analyze_project_structure(project_path)
            except Exception as e:
                logger.warning(f"Project structure analysis failed, using defaults: {e}")
                project_structure_analysis = {'modular_structure': False, 'separation_of_concerns': False}

            # Quick analysis without heavy operations
            estimated_team_size = self._estimate_team_size(git_analysis)
            experience_indicators = self._identify_experience_indicators(
                code_quality_indicators, project_structure_analysis
            )
            development_patterns = self._identify_development_patterns_fast(project_path)
            git_activity_level = self._assess_git_activity_level(git_analysis)
            collaboration_patterns = self._identify_collaboration_patterns(git_analysis)

            elapsed_time = time.time() - start_time
            logger.info(f"Team context analysis complete: {estimated_team_size} team ({elapsed_time:.2f}s)")

            return TeamContext(
                estimated_team_size=estimated_team_size,
                experience_indicators=experience_indicators,
                development_patterns=development_patterns,
                git_activity_level=git_activity_level,
                collaboration_patterns=collaboration_patterns
            )

        except TimeoutError:
            logger.warning(f"Team context analysis timed out for {project_path} - returning basic fallback")
            return self._get_basic_team_context(project_path)

        except Exception as e:
            logger.error(f"Error analyzing team context: {e}")
            return self._get_basic_team_context(project_path)

        finally:
            # Restore original signal handler and cancel alarm
            signal.alarm(0)
            signal.signal(signal.SIGALRM, original_handler)

    def _get_basic_team_context(self, project_path: str) -> TeamContext:
        """Fallback basic team context for when full analysis fails or times out"""
        try:
            # Very quick basic analysis - check if git repo exists
            has_git = os.path.exists(os.path.join(project_path, '.git'))
            has_readme = any(f.lower().startswith('readme') for f in os.listdir(project_path) if f)

            return TeamContext(
                estimated_team_size="small" if has_git else "unknown",
                experience_indicators=["documentation"] if has_readme else [],
                development_patterns=["git_workflow"] if has_git else [],
                git_activity_level="unknown",
                collaboration_patterns=[]
            )
        except:
            return TeamContext(
                estimated_team_size="unknown",
                experience_indicators=[],
                development_patterns=[],
                git_activity_level="unknown",
                collaboration_patterns=[]
            )

    def _analyze_git_activity(self, project_path: str) -> Dict[str, Any]:
        """Analyze git repository activity patterns with timeouts and error handling"""
        git_analysis = {
            'commit_count': 0,
            'contributor_count': 0,
            'recent_activity': False,
            'branch_count': 0,
            'has_issues': False,
            'has_pull_requests': False
        }

        try:
            if not os.path.exists(os.path.join(project_path, '.git')):
                logger.debug(f"No git repository found in {project_path}")
                return git_analysis

            # Set timeout for all git operations (10 seconds each)
            git_timeout = 10

            # Get commit count with timeout
            try:
                result = subprocess.run(
                    ['git', 'rev-list', '--count', 'HEAD'],
                    cwd=project_path, capture_output=True, text=True, timeout=git_timeout
                )
                if result.returncode == 0 and result.stdout.strip().isdigit():
                    git_analysis['commit_count'] = int(result.stdout.strip())
            except (subprocess.TimeoutExpired, ValueError) as e:
                logger.debug(f"Git commit count timeout/error: {e}")

            # Get contributor count with timeout
            try:
                result = subprocess.run(
                    ['git', 'shortlog', '-sn', '--all'],
                    cwd=project_path, capture_output=True, text=True, timeout=git_timeout
                )
                if result.returncode == 0 and result.stdout.strip():
                    contributors = [line for line in result.stdout.strip().split('\n') if line.strip()]
                    git_analysis['contributor_count'] = len(contributors)
            except subprocess.TimeoutExpired as e:
                logger.debug(f"Git contributor count timeout: {e}")

            # Check recent activity with timeout
            try:
                result = subprocess.run(
                    ['git', 'log', '--since="30 days ago"', '--oneline', '--max-count=10'],
                    cwd=project_path, capture_output=True, text=True, timeout=git_timeout
                )
                if result.returncode == 0:
                    recent_commits = [line for line in result.stdout.strip().split('\n') if line.strip()]
                    git_analysis['recent_activity'] = len(recent_commits) > 0
            except subprocess.TimeoutExpired as e:
                logger.debug(f"Git recent activity timeout: {e}")

            # Get branch count with timeout
            try:
                result = subprocess.run(
                    ['git', 'branch', '-a'],
                    cwd=project_path, capture_output=True, text=True, timeout=git_timeout
                )
                if result.returncode == 0 and result.stdout.strip():
                    branches = [line for line in result.stdout.strip().split('\n') if line.strip()]
                    git_analysis['branch_count'] = len(branches)
            except subprocess.TimeoutExpired as e:
                logger.debug(f"Git branch count timeout: {e}")

        except Exception as e:
            logger.warning(f"Git analysis error for {project_path}: {e}")

        return git_analysis

    def _analyze_code_quality_indicators(self, project_path: str) -> List[str]:
        """Identify code quality indicators with optimized single directory traversal"""
        quality_indicators = []

        quality_files = {
            'testing': ['test/', 'tests/', '__tests__/', '.test.', '.spec.'],
            'linting': ['.eslintrc', '.pylintrc', 'tslint.json', '.flake8'],
            'formatting': ['.prettierrc', '.editorconfig', 'black.toml'],
            'ci_cd': ['.github/workflows/', '.gitlab-ci.yml', 'Jenkinsfile'],
            'documentation': ['README.md', 'docs/', 'wiki/'],
            'type_checking': ['mypy.ini', 'tsconfig.json', 'types/'],
            'dependency_management': ['package-lock.json', 'poetry.lock', 'Pipfile.lock']
        }

        try:
            # Single optimized directory traversal with depth limit
            max_depth = 5  # Limit directory depth for performance
            found_indicators = set()

            for root, dirs, files in os.walk(project_path):
                # Calculate current depth and limit traversal
                depth = root[len(project_path):].count(os.sep)
                if depth >= max_depth:
                    dirs[:] = []  # Don't go deeper
                    continue

                # Skip common ignore directories for performance
                dirs[:] = [d for d in dirs if not d.startswith('.')
                          and d not in ['node_modules', '__pycache__', 'venv', 'env', 'target', 'build', 'dist', '.git']]

                # Check all patterns in single pass
                for indicator, patterns in quality_files.items():
                    if indicator in found_indicators:
                        continue  # Already found this indicator

                    for pattern in patterns:
                        # Check if pattern matches any file or directory
                        if (any(pattern in file for file in files) or
                            any(pattern in root for _ in [None]) or
                            any(pattern in d for d in dirs)):
                            found_indicators.add(indicator)
                            break

                # Early exit if all indicators found
                if len(found_indicators) == len(quality_files):
                    break

            quality_indicators = list(found_indicators)

        except Exception as e:
            logger.warning(f"Code quality analysis error for {project_path}: {e}")
            # Fallback to basic checks if traversal fails
            quality_indicators = self._basic_quality_check(project_path)

        return quality_indicators

    def _basic_quality_check(self, project_path: str) -> List[str]:
        """Fallback basic quality check for when full analysis fails"""
        basic_indicators = []

        # Quick checks for common files in root directory only
        try:
            root_files = os.listdir(project_path)

            if any(f.startswith('README') for f in root_files):
                basic_indicators.append('documentation')
            if any('test' in f.lower() for f in root_files):
                basic_indicators.append('testing')
            if any(f in ['.eslintrc', '.pylintrc', 'tslint.json'] for f in root_files):
                basic_indicators.append('linting')
            if 'package-lock.json' in root_files or 'poetry.lock' in root_files:
                basic_indicators.append('dependency_management')

        except Exception as e:
            logger.debug(f"Basic quality check error: {e}")

        return basic_indicators

    def _analyze_project_structure(self, project_path: str) -> Dict[str, bool]:
        """Analyze project structure for organization patterns"""
        structure_indicators = {
            'modular_structure': False,
            'separation_of_concerns': False,
            'configuration_management': False,
            'environment_setup': False
        }

        # Check for modular structure
        common_modules = ['src/', 'lib/', 'components/', 'modules/', 'services/']
        if any(os.path.exists(os.path.join(project_path, module)) for module in common_modules):
            structure_indicators['modular_structure'] = True

        # Check for separation of concerns
        separation_dirs = ['models/', 'views/', 'controllers/', 'api/', 'frontend/', 'backend/']
        if sum(os.path.exists(os.path.join(project_path, d)) for d in separation_dirs) >= 2:
            structure_indicators['separation_of_concerns'] = True

        # Check for configuration management
        config_files = ['config/', '.env', 'settings.py', 'appsettings.json']
        if any(os.path.exists(os.path.join(project_path, config)) for config in config_files):
            structure_indicators['configuration_management'] = True

        # Check for environment setup
        env_files = ['Dockerfile', 'docker-compose.yml', 'requirements.txt', 'package.json']
        if any(os.path.exists(os.path.join(project_path, env)) for env in env_files):
            structure_indicators['environment_setup'] = True

        return structure_indicators

    def _estimate_team_size(self, git_analysis: Dict[str, Any]) -> str:
        """Estimate team size based on git activity"""
        contributor_count = git_analysis.get('contributor_count', 0)

        if contributor_count <= 2:
            return "small"
        elif contributor_count <= 8:
            return "medium"
        else:
            return "large"

    def _identify_experience_indicators(self, quality_indicators: List[str],
                                      structure_analysis: Dict[str, bool]) -> List[str]:
        """Identify team experience level indicators"""
        experience_indicators = []

        # High experience indicators
        if 'testing' in quality_indicators:
            experience_indicators.append('test_driven_development')
        if 'ci_cd' in quality_indicators:
            experience_indicators.append('automated_deployment')
        if structure_analysis.get('modular_structure'):
            experience_indicators.append('architectural_discipline')
        if 'linting' in quality_indicators and 'formatting' in quality_indicators:
            experience_indicators.append('code_quality_focus')
        if 'type_checking' in quality_indicators:
            experience_indicators.append('type_safety_awareness')

        # Determine overall experience level
        if len(experience_indicators) >= 4:
            experience_indicators.append('senior_level')
        elif len(experience_indicators) >= 2:
            experience_indicators.append('intermediate_level')
        else:
            experience_indicators.append('junior_level')

        return experience_indicators

    def _identify_development_patterns(self, project_path: str) -> List[str]:
        """Identify development patterns and methodologies"""
        patterns = []

        # Check for specific patterns
        if os.path.exists(os.path.join(project_path, 'test')) or os.path.exists(os.path.join(project_path, 'tests')):
            patterns.append('test_driven')

        if os.path.exists(os.path.join(project_path, 'docker-compose.yml')):
            patterns.append('containerized_development')

        if os.path.exists(os.path.join(project_path, 'api')) or any('api' in f for f in os.listdir(project_path)):
            patterns.append('api_first')

        # Check for microservices pattern
        services_dirs = [d for d in os.listdir(project_path)
                        if os.path.isdir(os.path.join(project_path, d)) and 'service' in d.lower()]
        if len(services_dirs) > 1:
            patterns.append('microservices')

        return patterns

    def _identify_development_patterns_fast(self, project_path: str) -> List[str]:
        """Fast version of development patterns identification with timeout protection"""
        patterns = []

        try:
            # Quick checks with error handling - only check root directory for speed
            root_items = os.listdir(project_path)
            root_dirs = [item for item in root_items if os.path.isdir(os.path.join(project_path, item))]
            root_files = [item for item in root_items if os.path.isfile(os.path.join(project_path, item))]

            # Fast pattern detection
            if any(d in ['test', 'tests', '__tests__'] for d in root_dirs):
                patterns.append('test_driven')

            if 'docker-compose.yml' in root_files or 'Dockerfile' in root_files:
                patterns.append('containerized_development')

            if any('api' in item.lower() for item in root_dirs + root_files):
                patterns.append('api_first')

            # Quick microservices check (limit to avoid long operations)
            services_dirs = [d for d in root_dirs[:10] if 'service' in d.lower()]  # Limit to first 10 dirs
            if len(services_dirs) > 1:
                patterns.append('microservices')

            # Git workflow pattern (quick check)
            if '.git' in root_dirs:
                patterns.append('git_workflow')

        except Exception as e:
            logger.debug(f"Fast development patterns analysis error: {e}")
            # Return basic patterns if analysis fails
            patterns = ['git_workflow'] if os.path.exists(os.path.join(project_path, '.git')) else []

        return patterns

    def _assess_git_activity_level(self, git_analysis: Dict[str, Any]) -> str:
        """Assess overall git activity level"""
        commit_count = git_analysis.get('commit_count', 0)
        recent_activity = git_analysis.get('recent_activity', False)

        if commit_count > 100 and recent_activity:
            return "high"
        elif commit_count > 20:
            return "medium"
        else:
            return "low"

    def _identify_collaboration_patterns(self, git_analysis: Dict[str, Any]) -> List[str]:
        """Identify collaboration patterns from git analysis"""
        patterns = []

        contributor_count = git_analysis.get('contributor_count', 0)
        branch_count = git_analysis.get('branch_count', 0)

        if contributor_count > 1:
            patterns.append('collaborative_development')

        if branch_count > 3:
            patterns.append('feature_branch_workflow')

        if git_analysis.get('has_pull_requests'):
            patterns.append('code_review_process')

        return patterns

class MCPToolsIntegrator:
    """Integration layer for MCP tools (Serena, Context7, Playwright)"""

    def __init__(self):
        self.serena_available = self._check_serena_availability()
        self.context7_available = self._check_context7_availability()
        self.playwright_available = self._check_playwright_availability()

    def gather_mcp_insights(self, project_path: str) -> MCPToolsInsights:
        """
        Gather insights from available MCP tools

        Args:
            project_path: Path to project directory

        Returns:
            MCPToolsInsights with analysis from available tools
        """
        logger.info(f"Gathering MCP tools insights for: {project_path}")

        serena_analysis = None
        context7_patterns = None
        playwright_coverage = None

        # Serena project indexing and analysis
        if self.serena_available:
            serena_analysis = self._get_serena_analysis(project_path)

        # Context7 semantic analysis
        if self.context7_available:
            context7_patterns = self._get_context7_patterns(project_path)

        # Playwright automation analysis
        if self.playwright_available:
            playwright_coverage = self._get_playwright_coverage(project_path)

        # Calculate integration quality score
        integration_quality = self._calculate_integration_quality(
            serena_analysis, context7_patterns, playwright_coverage
        )

        logger.info(f"MCP insights gathering complete. Quality score: {integration_quality:.2f}")

        return MCPToolsInsights(
            serena_available=self.serena_available,
            serena_analysis=serena_analysis,
            context7_available=self.context7_available,
            context7_patterns=context7_patterns,
            playwright_available=self.playwright_available,
            playwright_coverage=playwright_coverage,
            integration_quality_score=integration_quality
        )

    def _check_serena_availability(self) -> bool:
        """Check if Serena MCP tool is available"""
        try:
            # Check for .serena directory or serena command
            result = subprocess.run(['which', 'serena'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _check_context7_availability(self) -> bool:
        """Check if Context7 MCP tool is available"""
        try:
            # Check for context7 installation
            result = subprocess.run(['which', 'context7'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _check_playwright_availability(self) -> bool:
        """Check if Playwright MCP tool is available"""
        try:
            # Check for playwright installation
            result = subprocess.run(['which', 'playwright'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _get_serena_analysis(self, project_path: str) -> Optional[str]:
        """Get Serena project analysis"""
        try:
            # Mock Serena analysis - replace with actual Serena MCP integration
            serena_index_path = os.path.join(project_path, '.serena')
            if os.path.exists(serena_index_path):
                return "Complex multi-service architecture with well-defined component boundaries"
            else:
                return "Single-service application with straightforward structure"
        except Exception as e:
            logger.debug(f"Serena analysis error: {e}")
            return None

    def _get_context7_patterns(self, project_path: str) -> Optional[str]:
        """Get Context7 semantic patterns analysis"""
        try:
            # Mock Context7 analysis - replace with actual Context7 MCP integration
            # This would use Context7's semantic analysis capabilities
            return "Heavy use of async patterns and event-driven architecture"
        except Exception as e:
            logger.debug(f"Context7 analysis error: {e}")
            return None

    def _get_playwright_coverage(self, project_path: str) -> Optional[str]:
        """Get Playwright test coverage analysis"""
        try:
            # Check for Playwright test files
            playwright_tests = []
            for root, dirs, files in os.walk(project_path):
                for file in files:
                    if 'playwright' in file.lower() or file.endswith('.spec.ts'):
                        playwright_tests.append(file)

            if playwright_tests:
                return f"Comprehensive E2E testing infrastructure with {len(playwright_tests)} test files"
            else:
                return "No Playwright test automation detected"
        except Exception as e:
            logger.debug(f"Playwright analysis error: {e}")
            return None

    def _calculate_integration_quality(self, serena_analysis: Optional[str],
                                     context7_patterns: Optional[str],
                                     playwright_coverage: Optional[str]) -> float:
        """Calculate overall integration quality score"""
        score = 0.0
        total_tools = 3.0

        if serena_analysis:
            score += 0.4  # Serena provides project structure insights
        if context7_patterns:
            score += 0.3  # Context7 provides semantic understanding
        if playwright_coverage:
            score += 0.3  # Playwright provides testing insights

        return score

class FrameworkUsageCollector:
    """Collect framework usage data for ML training"""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

        # Create subdirectories for different data types
        (self.data_dir / 'project_contexts').mkdir(exist_ok=True)
        (self.data_dir / 'agent_selections').mkdir(exist_ok=True)
        (self.data_dir / 'workflow_patterns').mkdir(exist_ok=True)
        (self.data_dir / 'success_metrics').mkdir(exist_ok=True)

    def collect_project_context(self, project_context: ProjectContext):
        """Store project context data for ML training"""
        try:
            context_file = self.data_dir / 'project_contexts' / f"{project_context.context_hash}.json"

            # Convert to serializable format
            context_dict = asdict(project_context)
            context_dict['timestamp'] = project_context.timestamp.isoformat()

            with open(context_file, 'w') as f:
                json.dump(context_dict, f, indent=2)

            logger.info(f"Project context collected: {project_context.context_hash}")

        except Exception as e:
            logger.error(f"Error collecting project context: {e}")

    def collect_agent_selection(self, project_hash: str, selected_agents: List[str],
                              selection_method: str, user_satisfaction: Optional[float] = None):
        """Store agent selection data for ML training"""
        try:
            selection_data = {
                'project_hash': project_hash,
                'selected_agents': selected_agents,
                'selection_method': selection_method,  # 'manual', 'ai', 'hybrid'
                'user_satisfaction': user_satisfaction,
                'timestamp': datetime.datetime.now().isoformat()
            }

            selection_file = self.data_dir / 'agent_selections' / f"{project_hash}_{int(datetime.datetime.now().timestamp())}.json"

            with open(selection_file, 'w') as f:
                json.dump(selection_data, f, indent=2)

            logger.info(f"Agent selection collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting agent selection: {e}")

    def collect_workflow_pattern(self, project_hash: str, workflow_data: Dict[str, Any]):
        """Store workflow pattern data for ML training"""
        try:
            workflow_data.update({
                'project_hash': project_hash,
                'timestamp': datetime.datetime.now().isoformat()
            })

            workflow_file = self.data_dir / 'workflow_patterns' / f"{project_hash}_workflow.json"

            with open(workflow_file, 'w') as f:
                json.dump(workflow_data, f, indent=2)

            logger.info(f"Workflow pattern collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting workflow pattern: {e}")

    def collect_success_metrics(self, project_hash: str, metrics: Dict[str, Any]):
        """Store project success metrics for ML training"""
        try:
            metrics_data = {
                'project_hash': project_hash,
                'metrics': metrics,
                'timestamp': datetime.datetime.now().isoformat()
            }

            metrics_file = self.data_dir / 'success_metrics' / f"{project_hash}_metrics.json"

            with open(metrics_file, 'w') as f:
                json.dump(metrics_data, f, indent=2)

            logger.info(f"Success metrics collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting success metrics: {e}")

class ProjectContextAnalyzer:
    """Main class for comprehensive project context analysis"""

    def __init__(self, data_collection_dir: str = "./.ai-tools/data"):
        self.technology_detector = TechnologyDetector()
        self.complexity_analyzer = ProjectComplexityAnalyzer()
        self.domain_classifier = BusinessDomainClassifier()
        self.team_analyzer = TeamContextAnalyzer()
        self.mcp_integrator = MCPToolsIntegrator()
        self.usage_collector = FrameworkUsageCollector(data_collection_dir)

    def analyze_project(self, project_path: str) -> ProjectContext:
        """
        Perform comprehensive project analysis for AI-powered agent selection

        Args:
            project_path: Path to project directory

        Returns:
            ProjectContext with complete analysis results
        """
        logger.info(f"Starting comprehensive project analysis: {project_path}")

        try:
            # Detect technology stack
            technology_stack = self.technology_detector.detect_technology_stack(project_path)

            # Analyze project complexity
            complexity = self.complexity_analyzer.analyze_complexity(project_path)

            # Classify business domain
            business_domain = self.domain_classifier.classify_domain(project_path)

            # Analyze team context
            team_context = self.team_analyzer.analyze_team_context(project_path)

            # Gather MCP tools insights
            mcp_insights = self.mcp_integrator.gather_mcp_insights(project_path)

            # Load framework configuration if available
            framework_config = self._load_framework_config(project_path)

            # Generate context hash for unique identification
            context_hash = self._generate_context_hash(
                project_path, technology_stack, complexity, business_domain
            )

            # Create complete project context
            project_context = ProjectContext(
                project_path=project_path,
                technology_stack=technology_stack,
                complexity=complexity,
                business_domain=business_domain,
                team_context=team_context,
                mcp_insights=mcp_insights,
                framework_config=framework_config,
                timestamp=datetime.datetime.now(),
                context_hash=context_hash
            )

            # Collect data for ML training
            self.usage_collector.collect_project_context(project_context)

            logger.info(f"Project analysis complete: {context_hash}")
            return project_context

        except Exception as e:
            logger.error(f"Error during project analysis: {e}")
            raise

    def _load_framework_config(self, project_path: str) -> Optional[Dict[str, Any]]:
        """Load CLAUDE.md framework configuration if available"""
        try:
            claude_md_path = os.path.join(project_path, 'CLAUDE.md')
            if os.path.exists(claude_md_path):
                with open(claude_md_path, 'r') as f:
                    content = f.read()

                # Extract configuration from CLAUDE.md
                # This is a simplified parser - could be enhanced
                config = {
                    'has_claude_md': True,
                    'content_length': len(content),
                    'has_todo_config': 'todo_management_enabled' in content.lower(),
                    'has_agent_config': 'agents and roles' in content.lower()
                }

                return config
            else:
                return {'has_claude_md': False}

        except Exception as e:
            logger.debug(f"Error loading framework config: {e}")
            return None

    def _generate_context_hash(self, project_path: str, technology_stack: TechnologyStack,
                             complexity: ProjectComplexity, business_domain: BusinessDomain) -> str:
        """Generate unique hash for project context"""
        context_str = (
            f"{project_path}|"
            f"{technology_stack.frontend}|{technology_stack.backend}|"
            f"{complexity.complexity_rating}|{business_domain.primary}"
        )

        return hashlib.md5(context_str.encode()).hexdigest()

def main():
    """Main function for testing the data collection system"""
    if len(sys.argv) != 2:
        print("Usage: python data_collection_system.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    # Initialize project analyzer
    analyzer = ProjectContextAnalyzer()

    try:
        # Analyze project
        context = analyzer.analyze_project(project_path)

        # Print analysis results
        print("\n" + "="*80)
        print("🎯 PROJECT ANALYSIS RESULTS")
        print("="*80)

        print(f"\n📁 Project: {context.project_path}")
        print(f"🔍 Context Hash: {context.context_hash}")
        print(f"⏰ Analysis Time: {context.timestamp}")

        print(f"\n💻 Technology Stack (Confidence: {context.technology_stack.confidence_score:.2f}):")
        for category in ['frontend', 'backend', 'database', 'infrastructure', 'testing']:
            techs = getattr(context.technology_stack, category)
            if techs:
                print(f"  {category.title()}: {', '.join(techs)}")

        print(f"\n📊 Project Complexity: {context.complexity.complexity_rating.upper()}")
        print(f"  Files: {context.complexity.file_count}")
        print(f"  Lines of Code: {context.complexity.code_lines}")
        print(f"  Directory Depth: {context.complexity.directory_depth}")
        print(f"  Dependencies: {context.complexity.dependency_count}")
        print(f"  Complexity Score: {context.complexity.complexity_score:.2f}")

        print(f"\n🏢 Business Domain: {context.business_domain.primary.upper()}")
        print(f"  Industry: {context.business_domain.industry_vertical}")
        print(f"  Confidence: {context.business_domain.confidence_score:.2f}")
        if context.business_domain.secondary:
            print(f"  Secondary: {', '.join(context.business_domain.secondary)}")
        if context.business_domain.compliance_requirements:
            print(f"  Compliance: {', '.join(context.business_domain.compliance_requirements)}")

        print(f"\n👥 Team Context: {context.team_context.estimated_team_size.upper()} team")
        print(f"  Git Activity: {context.team_context.git_activity_level}")
        if context.team_context.experience_indicators:
            print(f"  Experience: {', '.join(context.team_context.experience_indicators)}")
        if context.team_context.development_patterns:
            print(f"  Patterns: {', '.join(context.team_context.development_patterns)}")

        print(f"\n🔗 MCP Tools Integration (Quality: {context.mcp_insights.integration_quality_score:.2f}):")
        print(f"  Serena: {'✅' if context.mcp_insights.serena_available else '❌'}")
        if context.mcp_insights.serena_analysis:
            print(f"    Analysis: {context.mcp_insights.serena_analysis}")

        print(f"  Context7: {'✅' if context.mcp_insights.context7_available else '❌'}")
        if context.mcp_insights.context7_patterns:
            print(f"    Patterns: {context.mcp_insights.context7_patterns}")

        print(f"  Playwright: {'✅' if context.mcp_insights.playwright_available else '❌'}")
        if context.mcp_insights.playwright_coverage:
            print(f"    Coverage: {context.mcp_insights.playwright_coverage}")

        if context.framework_config:
            print(f"\n⚙️ Framework Configuration:")
            print(f"  CLAUDE.md: {'✅' if context.framework_config.get('has_claude_md') else '❌'}")
            if context.framework_config.get('has_todo_config'):
                print(f"  TODO Management: ✅")
            if context.framework_config.get('has_agent_config'):
                print(f"  Agent Configuration: ✅")

        print("\n" + "="*80)
        print("✅ Analysis complete! Data collected for ML training.")
        print("="*80)

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()