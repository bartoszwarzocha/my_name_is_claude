# Build Tools and Bundler Optimization

## Context and Purpose
You are architecting and optimizing advanced build pipelines for modern frontend applications. This prompt focuses on implementing high-performance build systems, optimizing bundle sizes, configuring advanced webpack/Vite setups, and establishing CI/CD integration with comprehensive build optimization strategies.

## Expertise Areas
- Advanced Webpack configuration and optimization strategies
- Vite build system with advanced plugin architecture
- Bundle analysis and optimization techniques
- Code splitting and dynamic imports
- Asset optimization and compression
- Development environment optimization
- Production build performance tuning

## Implementation Framework

### Phase 1: Advanced Build System Architecture

**Comprehensive Build Configuration Framework:**
```typescript
// Advanced build system architecture
interface BuildSystemArchitecture {
  bundlers: {
    webpack: {
      optimization: 'tree_shaking_dead_code_elimination_scope_hoisting';
      splitting: 'chunk_splitting_vendor_commons_async_imports';
      caching: 'persistent_cache_filesystem_cache_optimization';
      performance: 'parallel_processing_worker_threads_build_acceleration';
    };
    vite: {
      performance: 'esbuild_rollup_native_esm_hot_reload';
      optimization: 'dependency_pre_bundling_selective_hmr';
      plugins: 'custom_plugin_development_build_pipeline_extension';
      deployment: 'static_generation_preview_builds_cloud_integration';
    };
  };
  
  optimization: {
    bundleAnalysis: 'webpack_bundle_analyzer_source_map_explorer';
    assetOptimization: 'image_compression_font_subsetting_css_optimization';
    codeOptimization: 'minification_obfuscation_compression_strategies';
    loadingStrategies: 'preloading_prefetching_resource_hints_priority';
  };
}

// Advanced Webpack configuration with performance optimization
const createWebpackConfig = (env: BuildEnvironment): webpack.Configuration => {
  const isDevelopment = env === 'development';
  const isProduction = env === 'production';

  return {
    mode: env,
    entry: {
      main: './src/index.tsx',
      // Separate vendor chunk for better caching
      vendor: ['react', 'react-dom', 'react-router-dom']
    },

    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: isProduction 
        ? 'static/js/[name].[contenthash:8].js'
        : 'static/js/[name].bundle.js',
      chunkFilename: isProduction
        ? 'static/js/[name].[contenthash:8].chunk.js'
        : 'static/js/[name].chunk.js',
      publicPath: process.env.PUBLIC_URL || '/',
      clean: true,
      // Enable modern JavaScript features in output
      environment: {
        arrowFunction: true,
        bigIntLiteral: true,
        const: true,
        destructuring: true,
        dynamicImport: true,
        forOf: true,
        module: true
      }
    },

    resolve: {
      extensions: ['.tsx', '.ts', '.jsx', '.js', '.json'],
      alias: {
        '@': path.resolve(__dirname, 'src'),
        '@components': path.resolve(__dirname, 'src/components'),
        '@utils': path.resolve(__dirname, 'src/utils'),
        '@assets': path.resolve(__dirname, 'src/assets'),
        '@hooks': path.resolve(__dirname, 'src/hooks'),
        '@services': path.resolve(__dirname, 'src/services'),
        '@types': path.resolve(__dirname, 'src/types')
      },
      // Optimize module resolution
      modules: ['node_modules', path.resolve(__dirname, 'src')],
      // Reduce resolve attempts
      symlinks: false
    },

    optimization: {
      minimize: isProduction,
      minimizer: [
        // Advanced JavaScript minification
        new TerserPlugin({
          terserOptions: {
            parse: { ecma: 8 },
            compress: {
              ecma: 5,
              warnings: false,
              comparisons: false,
              inline: 2,
              drop_console: isProduction,
              drop_debugger: isProduction,
              pure_funcs: isProduction ? ['console.log', 'console.info'] : []
            },
            mangle: { safari10: true },
            output: { ecma: 5, comments: false, ascii_only: true }
          },
          parallel: true,
          extractComments: false
        }),
        
        // CSS optimization
        new CssMinimizerPlugin({
          minimizerOptions: {
            preset: ['default', {
              discardComments: { removeAll: true },
              normalizeUnicode: false,
              minifySelectors: true,
              minifyParams: true,
              minifyFontValues: true
            }]
          }
        })
      ],

      // Advanced chunk splitting strategy
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          // Vendor libraries
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: 'vendors',
            priority: 10,
            chunks: 'all',
            enforce: true
          },
          
          // React ecosystem
          react: {
            test: /[\\/]node_modules[\\/](react|react-dom|react-router)[\\/]/,
            name: 'react',
            priority: 20,
            chunks: 'all',
            enforce: true
          },
          
          // UI libraries
          ui: {
            test: /[\\/]node_modules[\\/](@mui|@chakra-ui|antd)[\\/]/,
            name: 'ui',
            priority: 15,
            chunks: 'all',
            enforce: true
          },
          
          // Utility libraries
          utils: {
            test: /[\\/]node_modules[\\/](lodash|ramda|date-fns|moment)[\\/]/,
            name: 'utils',
            priority: 12,
            chunks: 'all',
            enforce: true
          },
          
          // Common modules used across components
          common: {
            name: 'common',
            minChunks: 2,
            priority: 5,
            chunks: 'all',
            enforce: true
          }
        }
      },

      // Runtime chunk optimization
      runtimeChunk: {
        name: (entrypoint: { name: string }) => `runtime-${entrypoint.name}`
      },

      // Module IDs optimization
      moduleIds: 'deterministic',
      chunkIds: 'deterministic',

      // Advanced caching strategy
      cache: {
        type: 'filesystem',
        buildDependencies: {
          config: [__filename]
        },
        cacheDirectory: path.resolve(__dirname, 'node_modules/.cache/webpack'),
        // Invalidate cache when dependencies change
        version: createEnvironmentHash(env)
      }
    },

    module: {
      rules: [
        // TypeScript/JavaScript processing with SWC for speed
        {
          test: /\.(ts|tsx|js|jsx)$/,
          exclude: /node_modules/,
          use: {
            loader: '@swc/loader',
            options: {
              jsc: {
                parser: {
                  syntax: 'typescript',
                  tsx: true,
                  decorators: true,
                  dynamicImport: true
                },
                transform: {
                  react: {
                    runtime: 'automatic',
                    development: isDevelopment,
                    refresh: isDevelopment
                  }
                },
                target: 'es2020',
                loose: false,
                minify: {
                  compress: isProduction,
                  mangle: isProduction
                }
              },
              module: {
                type: 'es6'
              },
              minify: isProduction
            }
          }
        },

        // Advanced CSS processing
        {
          test: /\.css$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
            {
              loader: 'css-loader',
              options: {
                modules: {
                  auto: true,
                  localIdentName: isProduction 
                    ? '[hash:base64:8]' 
                    : '[name]__[local]__[hash:base64:5]'
                },
                importLoaders: 1,
                sourceMap: !isProduction
              }
            },
            {
              loader: 'postcss-loader',
              options: {
                postcssOptions: {
                  plugins: [
                    'autoprefixer',
                    'cssnano',
                    ...(isProduction ? ['purgecss'] : [])
                  ]
                }
              }
            }
          ]
        },

        // Advanced asset processing
        {
          test: /\.(png|jpe?g|gif|webp|avif)$/i,
          type: 'asset',
          generator: {
            filename: 'static/media/[name].[hash:8][ext]'
          },
          parser: {
            dataUrlCondition: {
              maxSize: 8192 // 8kb
            }
          },
          use: [
            {
              loader: 'image-webpack-loader',
              options: {
                mozjpeg: { progressive: true, quality: 80 },
                optipng: { enabled: false },
                pngquant: { quality: [0.7, 0.9], speed: 4 },
                gifsicle: { interlaced: false },
                webp: { quality: 80 }
              }
            }
          ]
        },

        // SVG optimization and processing
        {
          test: /\.svg$/,
          oneOf: [
            // SVG as React component
            {
              resourceQuery: /component/,
              use: ['@svgr/webpack']
            },
            // SVG as asset
            {
              type: 'asset/resource',
              generator: {
                filename: 'static/media/[name].[hash:8][ext]'
              }
            }
          ]
        }
      ]
    },

    plugins: [
      // HTML generation with optimization
      new HtmlWebpackPlugin({
        template: 'public/index.html',
        minify: isProduction ? {
          removeComments: true,
          collapseWhitespace: true,
          removeRedundantAttributes: true,
          useShortDoctype: true,
          removeEmptyAttributes: true,
          removeStyleLinkTypeAttributes: true,
          keepClosingSlash: true,
          minifyJS: true,
          minifyCSS: true,
          minifyURLs: true
        } : false,
        inject: 'body',
        scriptLoading: 'defer'
      }),

      // CSS extraction for production
      ...(isProduction ? [
        new MiniCssExtractPlugin({
          filename: 'static/css/[name].[contenthash:8].css',
          chunkFilename: 'static/css/[name].[contenthash:8].chunk.css'
        })
      ] : []),

      // Progressive Web App features
      new WebpackPwaManifest({
        name: 'Application Name',
        short_name: 'App',
        description: 'Application Description',
        background_color: '#ffffff',
        theme_color: '#000000',
        inject: true,
        ios: true,
        icons: [
          {
            src: path.resolve('src/assets/icon.png'),
            sizes: [96, 128, 192, 256, 384, 512],
            destination: 'static/icons'
          }
        ]
      }),

      // Bundle analysis
      ...(process.env.ANALYZE === 'true' ? [
        new BundleAnalyzerPlugin({
          analyzerMode: 'static',
          openAnalyzer: false,
          reportFilename: 'bundle-report.html'
        })
      ] : []),

      // Development enhancements
      ...(isDevelopment ? [
        new webpack.HotModuleReplacementPlugin(),
        new ForkTsCheckerWebpackPlugin({
          async: true,
          typescript: {
            diagnosticOptions: {
              semantic: true,
              syntactic: true
            }
          }
        })
      ] : [])
    ],

    // Development server configuration
    devServer: isDevelopment ? {
      hot: true,
      open: true,
      port: 3000,
      historyApiFallback: true,
      compress: true,
      client: {
        overlay: { errors: true, warnings: false }
      },
      static: {
        directory: path.join(__dirname, 'public')
      }
    } : undefined,

    // Performance budgets
    performance: {
      maxAssetSize: 512000, // 500kb
      maxEntrypointSize: 512000,
      hints: isProduction ? 'error' : 'warning'
    },

    // Source maps optimization
    devtool: isDevelopment 
      ? 'eval-cheap-module-source-map' 
      : 'source-map'
  };
};
```

**Advanced Vite Configuration with Plugin Ecosystem:**
```typescript
// Comprehensive Vite configuration
export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  const isDevelopment = command === 'serve';
  const isProduction = command === 'build';

  return {
    plugins: [
      // React plugin with advanced options
      react({
        jsxImportSource: '@emotion/react',
        babel: {
          plugins: [
            ['@emotion/babel-plugin', { sourceMap: isDevelopment }]
          ]
        },
        // Fast refresh configuration
        fastRefresh: isDevelopment,
        // Include .mdx files
        include: /\.(mdx|js|jsx|ts|tsx)$/
      }),

      // TypeScript path resolution
      tsconfigPaths(),

      // Advanced ESLint integration
      eslint({
        cache: false,
        include: ['src/**/*.{ts,tsx,js,jsx}'],
        exclude: ['node_modules', 'dist']
      }),

      // Bundle analyzer
      ...(process.env.ANALYZE ? [visualizer({
        filename: 'dist/bundle-analysis.html',
        open: true,
        gzipSize: true,
        brotliSize: true
      })] : []),

      // PWA capabilities
      VitePWA({
        registerType: 'autoUpdate',
        workbox: {
          globPatterns: ['**/*.{js,css,html,ico,png,svg,webp}'],
          runtimeCaching: [
            {
              urlPattern: /^https:\/\/api\.example\.com\/.*/i,
              handler: 'NetworkFirst',
              options: {
                cacheName: 'api-cache',
                expiration: {
                  maxEntries: 100,
                  maxAgeSeconds: 60 * 60 * 24 // 24 hours
                },
                cacheableResponse: {
                  statuses: [0, 200]
                }
              }
            }
          ]
        },
        devOptions: {
          enabled: true
        },
        manifest: {
          name: 'Application Name',
          short_name: 'App',
          description: 'Application Description',
          theme_color: '#ffffff',
          icons: [
            {
              src: 'pwa-192x192.png',
              sizes: '192x192',
              type: 'image/png'
            }
          ]
        }
      }),

      // Custom plugin for advanced optimizations
      {
        name: 'advanced-optimizations',
        generateBundle(options, bundle) {
          // Custom chunk optimization logic
          Object.keys(bundle).forEach(fileName => {
            const chunk = bundle[fileName];
            if (chunk.type === 'chunk' && chunk.isEntry) {
              // Optimize entry chunks
              this.emitFile({
                type: 'asset',
                fileName: `preload-${fileName}`,
                source: this.generatePreloadScript(chunk)
              });
            }
          });
        }
      }
    ],

    // Advanced build options
    build: {
      target: ['es2020', 'edge88', 'firefox78', 'chrome87', 'safari14'],
      outDir: 'dist',
      assetsDir: 'static',
      sourcemap: isProduction ? 'hidden' : 'inline',
      
      // Advanced minification
      minify: 'esbuild',
      
      // Rollup options for fine-tuned control
      rollupOptions: {
        input: {
          main: resolve(__dirname, 'index.html'),
          // Additional entry points for micro-frontends
          admin: resolve(__dirname, 'admin.html')
        },
        
        output: {
          // Advanced chunking strategy
          manualChunks: (id) => {
            // Vendor chunks
            if (id.includes('node_modules')) {
              if (id.includes('react') || id.includes('react-dom')) {
                return 'react-vendor';
              }
              if (id.includes('@mui') || id.includes('@emotion')) {
                return 'ui-vendor';
              }
              if (id.includes('lodash') || id.includes('date-fns')) {
                return 'utils-vendor';
              }
              return 'vendor';
            }
            
            // Feature-based chunks
            if (id.includes('src/features/')) {
              const feature = id.split('src/features/')[1].split('/')[0];
              return `feature-${feature}`;
            }
          },
          
          // Asset naming
          chunkFileNames: 'static/js/[name]-[hash].js',
          entryFileNames: 'static/js/[name]-[hash].js',
          assetFileNames: (assetInfo) => {
            const info = assetInfo.name.split('.');
            const ext = info[info.length - 1];
            if (/\.(png|jpe?g|gif|svg|webp|avif)$/.test(assetInfo.name)) {
              return `static/images/[name]-[hash][extname]`;
            }
            if (/\.(woff2?|eot|ttf|otf)$/.test(assetInfo.name)) {
              return `static/fonts/[name]-[hash][extname]`;
            }
            return `static/[ext]/[name]-[hash][extname]`;
          }
        },
        
        // External dependencies for micro-frontend architecture
        external: (id) => {
          return id.startsWith('@shared/') && isProduction;
        }
      },

      // Performance optimization
      reportCompressedSize: true,
      chunkSizeWarningLimit: 1000,
      
      // Advanced asset handling
      assetsInlineLimit: 8192, // 8kb
      
      // CSS code splitting
      cssCodeSplit: true,
      
      // Library mode for component libraries
      lib: env.BUILD_MODE === 'lib' ? {
        entry: resolve(__dirname, 'src/lib/index.ts'),
        name: 'MyLibrary',
        formats: ['es', 'umd'],
        fileName: (format) => `my-library.${format}.js`
      } : undefined
    },

    // Development server enhancements
    server: {
      port: 3000,
      open: true,
      cors: true,
      
      // Advanced proxy configuration
      proxy: {
        '/api': {
          target: env.VITE_API_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ''),
          configure: (proxy) => {
            proxy.on('proxyReq', (proxyReq, req) => {
              // Add custom headers
              proxyReq.setHeader('X-Development-Mode', 'true');
            });
          }
        },
        
        // WebSocket proxy for real-time features
        '/socket.io': {
          target: env.VITE_WS_URL,
          ws: true,
          changeOrigin: true
        }
      },

      // Custom middleware
      middlewares: [
        // Security headers
        (req, res, next) => {
          res.setHeader('X-Content-Type-Options', 'nosniff');
          res.setHeader('X-Frame-Options', 'DENY');
          res.setHeader('X-XSS-Protection', '1; mode=block');
          next();
        }
      ]
    },

    // Optimizations
    optimizeDeps: {
      // Include dependencies that should be pre-bundled
      include: [
        'react',
        'react-dom',
        'react-router-dom',
        '@emotion/react',
        '@emotion/styled'
      ],
      
      // Exclude dependencies from pre-bundling
      exclude: ['@shared/components'],
      
      // Force specific versions
      force: env.FORCE_OPTIMIZE === 'true'
    },

    // Environment variables
    define: {
      __DEV__: isDevelopment,
      __VERSION__: JSON.stringify(process.env.npm_package_version),
      'process.env.NODE_ENV': JSON.stringify(mode)
    },

    // CSS preprocessing
    css: {
      modules: {
        localsConvention: 'camelCaseOnly',
        generateScopedName: isDevelopment 
          ? '[name]__[local]__[hash:base64:5]'
          : '[hash:base64:8]'
      },
      
      preprocessorOptions: {
        scss: {
          additionalData: '@import "@/styles/variables.scss";',
          charset: false
        }
      },
      
      postcss: {
        plugins: [
          autoprefixer(),
          ...(isProduction ? [cssnano()] : [])
        ]
      }
    }
  };
});
```

### Phase 2: Bundle Analysis and Optimization

**Comprehensive Bundle Analysis Framework:**
```typescript
// Advanced bundle analysis and optimization
class BundleOptimizationAnalyzer {
  private analyzer: WebpackBundleAnalyzer;
  private metrics: BundleMetrics;
  private optimizer: BundleOptimizer;

  async analyzeBundlePerformance(): Promise<OptimizationReport> {
    const bundleStats = await this.analyzer.generateStats();
    
    const analysis: OptimizationReport = {
      // Bundle size analysis
      bundleSizes: this.analyzeBundleSizes(bundleStats),
      
      // Dependency analysis
      dependencies: await this.analyzeDependencies(bundleStats),
      
      // Chunk analysis
      chunks: this.analyzeChunkEfficiency(bundleStats),
      
      // Asset analysis
      assets: this.analyzeAssetOptimization(bundleStats),
      
      // Performance metrics
      performance: await this.calculatePerformanceMetrics(bundleStats),
      
      // Optimization recommendations
      recommendations: this.generateOptimizationRecommendations(bundleStats)
    };

    return analysis;
  }

  private analyzeDependencies(stats: WebpackStats): DependencyAnalysis {
    const dependencies = stats.chunks
      .flatMap(chunk => chunk.modules)
      .filter(module => module.name.includes('node_modules'))
      .reduce((acc, module) => {
        const packageName = this.extractPackageName(module.name);
        const size = module.size || 0;
        
        if (!acc[packageName]) {
          acc[packageName] = {
            name: packageName,
            totalSize: 0,
            gzippedSize: 0,
            usageCount: 0,
            versions: new Set(),
            importPaths: []
          };
        }
        
        acc[packageName].totalSize += size;
        acc[packageName].usageCount += 1;
        acc[packageName].importPaths.push(module.name);
        
        return acc;
      }, {} as Record<string, DependencyInfo>);

    // Calculate optimization opportunities
    const optimizationOpportunities = Object.values(dependencies)
      .map(dep => {
        const opportunities: OptimizationOpportunity[] = [];
        
        // Large dependency check
        if (dep.totalSize > 100000) { // 100KB
          opportunities.push({
            type: 'LARGE_DEPENDENCY',
            impact: 'high',
            description: `${dep.name} is ${(dep.totalSize / 1024).toFixed(2)}KB - consider alternatives or lazy loading`,
            estimatedSavings: dep.totalSize * 0.3 // Estimated 30% reduction
          });
        }
        
        // Duplicate version check
        if (dep.versions.size > 1) {
          opportunities.push({
            type: 'DUPLICATE_DEPENDENCY',
            impact: 'medium',
            description: `Multiple versions of ${dep.name} detected - consolidate to single version`,
            estimatedSavings: dep.totalSize * (dep.versions.size - 1) / dep.versions.size
          });
        }
        
        // Unused imports check
        const unusedImports = this.detectUnusedImports(dep);
        if (unusedImports.length > 0) {
          opportunities.push({
            type: 'UNUSED_IMPORTS',
            impact: 'medium',
            description: `Unused imports detected in ${dep.name}: ${unusedImports.join(', ')}`,
            estimatedSavings: dep.totalSize * 0.2 // Estimated 20% reduction
          });
        }
        
        return { dependency: dep, opportunities };
      })
      .filter(item => item.opportunities.length > 0);

    return {
      dependencies: Object.values(dependencies),
      optimizationOpportunities,
      totalDependencySize: Object.values(dependencies).reduce((sum, dep) => sum + dep.totalSize, 0),
      duplicatePackages: Object.values(dependencies).filter(dep => dep.versions.size > 1)
    };
  }

  // Tree shaking effectiveness analysis
  private analyzeTreeShakingEffectiveness(stats: WebpackStats): TreeShakingAnalysis {
    const analysis: TreeShakingAnalysis = {
      totalModules: 0,
      eliminatedModules: 0,
      potentialSavings: 0,
      ineffectivePackages: []
    };

    stats.chunks.forEach(chunk => {
      chunk.modules.forEach(module => {
        analysis.totalModules++;
        
        // Check if module was eliminated by tree shaking
        if (module.reasons && module.reasons.length === 0) {
          analysis.eliminatedModules++;
        }
        
        // Check for packages that don't support tree shaking effectively
        if (module.name.includes('node_modules')) {
          const packageName = this.extractPackageName(module.name);
          if (this.isIneffectiveTreeShaking(module)) {
            const existingPackage = analysis.ineffectivePackages.find(p => p.name === packageName);
            if (existingPackage) {
              existingPackage.wastedSize += module.size || 0;
            } else {
              analysis.ineffectivePackages.push({
                name: packageName,
                wastedSize: module.size || 0,
                recommendation: this.getTreeShakingRecommendation(packageName)
              });
            }
          }
        }
      });
    });

    analysis.effectiveness = (analysis.eliminatedModules / analysis.totalModules) * 100;
    analysis.potentialSavings = analysis.ineffectivePackages.reduce((sum, pkg) => sum + pkg.wastedSize, 0);

    return analysis;
  }

  // Advanced code splitting analysis
  private analyzeCodeSplittingOpportunities(stats: WebpackStats): CodeSplittingAnalysis {
    const routeChunks = new Map<string, ChunkInfo>();
    const sharedModules = new Map<string, SharedModuleInfo>();
    
    stats.chunks.forEach(chunk => {
      // Analyze route-based chunks
      if (this.isRouteChunk(chunk)) {
        routeChunks.set(chunk.name, {
          name: chunk.name,
          size: chunk.size,
          modules: chunk.modules.length,
          route: this.extractRouteName(chunk.name)
        });
      }
      
      // Analyze shared modules across chunks
      chunk.modules.forEach(module => {
        const moduleId = module.identifier;
        if (sharedModules.has(moduleId)) {
          sharedModules.get(moduleId)!.chunks.add(chunk.name);
          sharedModules.get(moduleId)!.usage++;
        } else {
          sharedModules.set(moduleId, {
            id: moduleId,
            name: module.name,
            size: module.size || 0,
            chunks: new Set([chunk.name]),
            usage: 1
          });
        }
      });
    });

    // Identify optimization opportunities
    const splittingOpportunities: SplittingOpportunity[] = [];
    
    // Large route chunks that could be further split
    Array.from(routeChunks.values())
      .filter(chunk => chunk.size > 250000) // 250KB threshold
      .forEach(chunk => {
        splittingOpportunities.push({
          type: 'LARGE_ROUTE_CHUNK',
          target: chunk.name,
          currentSize: chunk.size,
          recommendation: 'Consider splitting into feature-based chunks or lazy loading components',
          estimatedImprovement: chunk.size * 0.4 // 40% size reduction
        });
      });

    // Highly shared modules that could be extracted
    Array.from(sharedModules.values())
      .filter(module => module.usage > 3 && module.size > 10000) // Used in 3+ chunks, >10KB
      .forEach(module => {
        splittingOpportunities.push({
          type: 'SHARED_MODULE_EXTRACTION',
          target: module.name,
          currentSize: module.size,
          usageCount: module.usage,
          recommendation: 'Extract into shared vendor chunk',
          estimatedImprovement: module.size * (module.usage - 1) / module.usage
        });
      });

    return {
      routeChunks: Array.from(routeChunks.values()),
      sharedModules: Array.from(sharedModules.values()),
      splittingOpportunities,
      totalChunks: stats.chunks.length,
      averageChunkSize: stats.chunks.reduce((sum, chunk) => sum + chunk.size, 0) / stats.chunks.length
    };
  }
}

// Performance budget enforcement
class PerformanceBudgetEnforcer {
  private budgets: PerformanceBudget[];
  private validator: BudgetValidator;

  constructor(budgets: PerformanceBudget[]) {
    this.budgets = budgets;
    this.validator = new BudgetValidator();
  }

  validateBuildAgainstBudgets(buildStats: BuildStats): BudgetValidationResult {
    const results: BudgetValidationResult = {
      passed: true,
      violations: [],
      warnings: [],
      metrics: {}
    };

    this.budgets.forEach(budget => {
      const validation = this.validator.validate(buildStats, budget);
      
      if (!validation.passed) {
        results.passed = false;
        
        if (budget.severity === 'error') {
          results.violations.push({
            type: budget.type,
            threshold: budget.threshold,
            actual: validation.actual,
            message: validation.message,
            recommendation: validation.recommendation
          });
        } else {
          results.warnings.push({
            type: budget.type,
            threshold: budget.threshold,
            actual: validation.actual,
            message: validation.message,
            recommendation: validation.recommendation
          });
        }
      }
      
      results.metrics[budget.type] = validation.actual;
    });

    return results;
  }

  // Generate performance budget configuration
  generateRecommendedBudgets(baselineStats: BuildStats): PerformanceBudget[] {
    return [
      {
        type: 'bundle-size',
        threshold: Math.max(baselineStats.totalSize * 1.1, 512000), // 10% increase or 500KB max
        severity: 'error'
      },
      {
        type: 'initial-chunk-size',
        threshold: Math.max(baselineStats.initialChunkSize * 1.05, 256000), // 5% increase or 250KB max
        severity: 'warning'
      },
      {
        type: 'asset-count',
        threshold: Math.max(baselineStats.assetCount * 1.2, 100), // 20% increase or 100 assets max
        severity: 'warning'
      },
      {
        type: 'chunk-count',
        threshold: Math.max(baselineStats.chunkCount * 1.3, 50), // 30% increase or 50 chunks max
        severity: 'warning'
      }
    ];
  }
}
```

### Phase 3: Development Environment Optimization

**Advanced Development Server Configuration:**
```typescript
// Comprehensive development environment optimization
class DevelopmentOptimizer {
  private hmrManager: HMRManager;
  private buildCache: BuildCacheManager;
  private assetProcessor: AssetProcessor;

  setupOptimizedDevEnvironment(): DevEnvironmentConfig {
    return {
      // Fast refresh configuration
      fastRefresh: {
        enabled: true,
        // Advanced options for better HMR
        overlay: {
          entry: path.resolve(__dirname, 'src/dev/error-overlay.tsx'),
          sockPath: '/sockjs-node'
        },
        // Custom HMR accept patterns
        acceptPatterns: [
          /\.module\.(css|scss)$/,
          /\.(ts|tsx|js|jsx)$/
        ],
        // HMR optimization rules
        optimizations: {
          skipUnchangedComponents: true,
          batchUpdates: true,
          preserveLocalState: true
        }
      },

      // Development server enhancements
      devServer: {
        // Advanced compression
        compress: true,
        
        // HTTP/2 support for better performance
        http2: true,
        https: {
          key: fs.readFileSync(path.join(__dirname, 'dev-server.key')),
          cert: fs.readFileSync(path.join(__dirname, 'dev-server.cert'))
        },

        // Advanced proxy configuration with load balancing
        proxy: this.setupAdvancedProxy(),

        // Custom middleware for development enhancements
        onBeforeSetupMiddleware: (devServer) => {
          // Development API mocking
          devServer.app.use('/api/mock', this.createMockApiMiddleware());
          
          // Performance monitoring
          devServer.app.use(this.createPerformanceMiddleware());
          
          // Bundle analysis endpoint
          devServer.app.get('/dev/bundle-analysis', this.handleBundleAnalysis);
        },

        // Watch options optimization
        watchOptions: {
          ignored: /node_modules/,
          aggregateTimeout: 300,
          poll: false, // Use native file watching for better performance
        },

        // Static file serving optimization
        static: [
          {
            directory: path.join(__dirname, 'public'),
            publicPath: '/',
            serveIndex: false,
            watch: {
              ignored: ['**/*.map', '**/node_modules/**']
            }
          }
        ],

        // Advanced client configuration
        client: {
          overlay: {
            errors: true,
            warnings: false,
            runtimeErrors: true
          },
          progress: true,
          reconnect: 5,
          webSocketTransport: 'ws'
        }
      },

      // Build caching strategy
      cache: {
        type: 'filesystem',
        cacheDirectory: path.resolve(__dirname, 'node_modules/.cache/dev-build'),
        buildDependencies: {
          config: [
            __filename,
            path.resolve(__dirname, 'package.json'),
            path.resolve(__dirname, 'tsconfig.json')
          ]
        },
        // Advanced cache invalidation
        version: this.generateCacheVersion(),
        
        // Memory cache for faster rebuilds
        memory: {
          maxGenerations: 5,
          cacheUnaffected: true
        }
      },

      // Source map optimization for development
      sourceMaps: {
        development: 'eval-cheap-module-source-map', // Fastest for development
        columns: false, // Disable column mappings for speed
        module: true,   // Include original source
        cheap: true     // Skip loader source maps for performance
      },

      // Development-specific optimizations
      optimizations: {
        removeAvailableModules: false,
        removeEmptyChunks: false,
        splitChunks: false, // Disable for faster builds
        usedExports: false, // Skip for development speed
        sideEffects: false  // Skip for development speed
      }
    };
  }

  // Advanced proxy setup with load balancing and failover
  private setupAdvancedProxy(): ProxyConfigArrayItem[] {
    const apiServers = [
      'http://localhost:8001',
      'http://localhost:8002',
      'http://localhost:8003'
    ];
    
    let currentServerIndex = 0;

    return [
      {
        context: ['/api', '/graphql'],
        target: () => {
          // Simple round-robin load balancing
          const server = apiServers[currentServerIndex];
          currentServerIndex = (currentServerIndex + 1) % apiServers.length;
          return server;
        },
        changeOrigin: true,
        logLevel: 'debug',
        
        // Advanced error handling and retry logic
        onError: (err, req, res) => {
          console.error('Proxy error:', err);
          // Attempt failover to next server
          if (currentServerIndex < apiServers.length - 1) {
            currentServerIndex++;
            // Retry the request
            req.url = req.originalUrl;
            this.retryProxyRequest(req, res, apiServers[currentServerIndex]);
          }
        },

        // Request/response interceptors
        onProxyReq: (proxyReq, req) => {
          proxyReq.setHeader('X-Development-Mode', 'true');
          proxyReq.setHeader('X-Request-ID', this.generateRequestId());
          
          // Add authentication headers for development
          if (process.env.DEV_AUTH_TOKEN) {
            proxyReq.setHeader('Authorization', `Bearer ${process.env.DEV_AUTH_TOKEN}`);
          }
        },

        onProxyRes: (proxyRes, req, res) => {
          // Add CORS headers for development
          proxyRes.headers['Access-Control-Allow-Origin'] = '*';
          proxyRes.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS';
          proxyRes.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization';
          
          // Log response time
          const responseTime = Date.now() - req.startTime;
          console.log(`API Response: ${req.method} ${req.url} - ${proxyRes.statusCode} (${responseTime}ms)`);
        }
      }
    ];
  }

  // Development performance monitoring
  private createPerformanceMiddleware(): express.RequestHandler {
    return (req, res, next) => {
      const startTime = Date.now();
      
      res.on('finish', () => {
        const duration = Date.now() - startTime;
        const stats = {
          method: req.method,
          url: req.url,
          statusCode: res.statusCode,
          duration,
          userAgent: req.get('User-Agent'),
          timestamp: new Date().toISOString()
        };
        
        // Log slow requests
        if (duration > 100) {
          console.warn(`Slow request detected:`, stats);
        }
        
        // Store metrics for analysis
        this.storePerformanceMetrics(stats);
      });
      
      next();
    };
  }
}
```

### Phase 4: CI/CD Integration and Deployment Optimization

**Advanced CI/CD Build Pipeline:**
```yaml
# Comprehensive GitHub Actions workflow for optimized builds
name: Advanced Build and Deploy

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '18'
  CACHE_NAME: build-cache-v2

jobs:
  analyze-changes:
    runs-on: ubuntu-latest
    outputs:
      should-build: ${{ steps.changes.outputs.build }}
      should-test: ${{ steps.changes.outputs.test }}
      affected-packages: ${{ steps.changes.outputs.packages }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Analyze Changes
        id: changes
        uses: dorny/paths-filter@v2
        with:
          filters: |
            build:
              - 'src/**'
              - 'package.json'
              - 'package-lock.json'
              - 'webpack.config.js'
              - 'vite.config.ts'
              - 'tsconfig.json'
            test:
              - 'src/**'
              - '**/*.test.*'
              - 'jest.config.js'

  build-and-analyze:
    needs: analyze-changes
    if: needs.analyze-changes.outputs.should-build == 'true'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        build-type: [development, production, analyze]
        
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          
      - name: Setup Build Cache
        uses: actions/cache@v3
        with:
          path: |
            node_modules/.cache
            .next/cache
            dist
          key: ${{ runner.os }}-${{ env.CACHE_NAME }}-${{ hashFiles('**/package-lock.json') }}-${{ matrix.build-type }}
          restore-keys: |
            ${{ runner.os }}-${{ env.CACHE_NAME }}-${{ hashFiles('**/package-lock.json') }}-
            ${{ runner.os }}-${{ env.CACHE_NAME }}-

      - name: Install Dependencies
        run: |
          npm ci --prefer-offline --no-audit
          # Install additional tools for analysis builds
          if [ "${{ matrix.build-type }}" == "analyze" ]; then
            npm install --no-save webpack-bundle-analyzer source-map-explorer
          fi

      - name: Build Application
        run: |
          case "${{ matrix.build-type }}" in
            "development")
              npm run build:dev
              ;;
            "production")
              npm run build:prod
              ;;
            "analyze")
              npm run build:analyze
              ;;
          esac
        env:
          NODE_ENV: ${{ matrix.build-type == 'development' && 'development' || 'production' }}
          ANALYZE: ${{ matrix.build-type == 'analyze' && 'true' || 'false' }}

      - name: Performance Budget Check
        if: matrix.build-type == 'production'
        run: |
          npm run budget-check
          echo "::group::Bundle Size Report"
          npx bundlesize
          echo "::endgroup::"

      - name: Bundle Analysis
        if: matrix.build-type == 'analyze'
        run: |
          # Generate detailed bundle analysis
          npm run analyze:bundle
          npm run analyze:source-map
          
          # Upload analysis reports
          echo "::group::Bundle Analysis Results"
          if [ -f "bundle-report.html" ]; then
            echo "Bundle analysis report generated"
            # Could upload to S3 or artifact storage here
          fi
          echo "::endgroup::"

      - name: Upload Build Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-${{ matrix.build-type }}-${{ github.sha }}
          path: |
            dist/
            bundle-report.html
            source-map-report.html
          retention-days: 7

      - name: Security Scan
        if: matrix.build-type == 'production'
        run: |
          # Scan for vulnerabilities in dependencies
          npm audit --audit-level high
          
          # Scan built assets for security issues
          npx safety-check dist/

  performance-testing:
    needs: [analyze-changes, build-and-analyze]
    if: needs.analyze-changes.outputs.should-build == 'true'
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Download Build Artifacts
        uses: actions/download-artifact@v3
        with:
          name: build-production-${{ github.sha }}
          path: dist/

      - name: Setup Lighthouse CI
        run: |
          npm install -g @lhci/cli@0.12.x
          
      - name: Run Lighthouse Performance Tests
        run: |
          lhci autorun \
            --collect.staticDistDir=./dist \
            --collect.numberOfRuns=3 \
            --assert.preset=lighthouse:recommended \
            --assert.assertions.speed-index=5000 \
            --assert.assertions.first-contentful-paint=3000 \
            --assert.assertions.largest-contentful-paint=4000 \
            --assert.assertions.cumulative-layout-shift=0.1
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}

      - name: Bundle Size Regression Testing
        run: |
          # Compare bundle sizes with baseline
          npm run bundle-size-compare
          
          # Generate size regression report
          echo "::group::Bundle Size Comparison"
          if [ -f "size-comparison.json" ]; then
            cat size-comparison.json | jq '.'
          fi
          echo "::endgroup::"

  deploy:
    needs: [build-and-analyze, performance-testing]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    
    steps:
      - name: Download Production Build
        uses: actions/download-artifact@v3
        with:
          name: build-production-${{ github.sha }}
          path: dist/

      - name: Deploy to CDN
        run: |
          # Advanced deployment with CDN optimization
          aws s3 sync dist/ s3://${{ secrets.S3_BUCKET }} \
            --delete \
            --cache-control "public,max-age=31536000,immutable" \
            --exclude "*.html" \
            --exclude "service-worker.js"
          
          # Deploy HTML files with shorter cache
          aws s3 sync dist/ s3://${{ secrets.S3_BUCKET }} \
            --cache-control "public,max-age=300" \
            --include "*.html" \
            --include "service-worker.js"

      - name: Invalidate CDN Cache
        run: |
          # Invalidate CloudFront cache for updated files
          aws cloudfront create-invalidation \
            --distribution-id ${{ secrets.CLOUDFRONT_DISTRIBUTION_ID }} \
            --paths "/*"

      - name: Post-deployment Verification
        run: |
          # Verify deployment success
          curl -f ${{ secrets.PRODUCTION_URL }}/health-check
          
          # Run smoke tests
          npm run test:smoke:production
```

## Success Criteria

1. **Build Performance Excellence:**
   - Development build times under 3 seconds for incremental changes
   - Production build times under 5 minutes for full builds
   - Bundle sizes optimized with <500KB initial load and effective code splitting

2. **Development Experience:**
   - Sub-100ms Hot Module Replacement for component changes
   - Comprehensive error overlay with source mapping
   - Advanced proxy configuration with failover and load balancing

3. **Production Optimization:**
   - Automated performance budget enforcement
   - Tree shaking effectiveness >80% for unused code elimination
   - Asset optimization with >70% compression ratios

4. **CI/CD Integration:**
   - Parallel build strategies with matrix optimization
   - Automated bundle analysis and regression detection
   - Zero-downtime deployment with CDN optimization

## Deliverables

- **Build System Configuration:** Complete Webpack/Vite setup with all optimizations
- **Bundle Analysis Framework:** Comprehensive analysis and optimization tools
- **Development Environment:** Optimized dev server with advanced features
- **CI/CD Pipeline:** Production-ready deployment automation
- **Performance Monitoring:** Real-time build performance tracking and alerting
- **Documentation:** Complete guide for build system maintenance and optimization