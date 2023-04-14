import '@babel/polyfill';

import gulp from 'gulp';
import env from 'gulp-env';
import gutil from 'gulp-util';
import MiniCssExtractPlugin from 'mini-css-extract-plugin';
import path from 'path';
import webpack from 'webpack';
import WebpackDevServer from 'webpack-dev-server';
import { WebpackManifestPlugin } from 'webpack-manifest-plugin';


/* Global variables */
const rootDir = `${__dirname}/`;
const staticDir = `${rootDir}main/static/`;
const PROD_ENV = gutil.env.production;
const WEBPACK_DEV_SERVER_PORT = (
  process.env.WEBPACK_DEV_SERVER_PORT ? process.env.WEBPACK_DEV_SERVER_PORT : 8080);
env.set({ NODE_ENV: PROD_ENV ? 'production' : 'debug' });

/* Directories */
const buildDir = PROD_ENV ? `${staticDir}build` : `${staticDir}build_dev`;
const sassDir = `${staticDir}sass`;
const jsDir = `${staticDir}js`;


/*
 * Global webpack config
 * ~~~~~~~~~~~~~~~~~~~~~
 */

const webpackConfig = {
  mode: PROD_ENV ? 'production' : 'development',
  entry: {
    App: [`${jsDir}/App.js`, `${sassDir}/App.scss`],
  },
  output: {
    filename: '[name].[chunkhash].js',
    path: buildDir,
    publicPath: PROD_ENV ? '/static/build/' : '/static/build_dev/',
  },
  resolve: {
    modules: ['node_modules'],
    extensions: ['.webpack.js', '.web.js', '.js', '.jsx', '.json', 'scss'],
  },
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: 'babel-loader' },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      },
      { test: /\.txt$/, use: 'raw-loader' },
      {
        test: /\.(png|jpg|jpeg|gif|svg|woff|woff2)([\?]?.*)$/,
        type: 'asset/resource'
      },
      { test: /\.(eot|ttf|wav|mp3|otf)([\?]?.*)$/, type: 'asset/resource' },
    ],
  },
  optimization: {
    minimize: PROD_ENV,
  },
  plugins: [
    new MiniCssExtractPlugin({ filename: '[name].[chunkhash].css' }),
    new WebpackManifestPlugin({
      fileName: 'manifest.json',
      publicPath: PROD_ENV ? 'build/' : 'build_dev/',
    }),
    ...(PROD_ENV ? [
      new webpack.LoaderOptionsPlugin({
        minimize: true,
      }),
    ] : []),
  ],
};


/*
 * Webpack task
 * ~~~~~~~~~~~~
 */

/* Task to build our JS and CSS applications. */
gulp.task('build-webpack-assets', gulp.series(() => (
  new Promise((resolve, reject) => {
    // eslint-disable-next-line consistent-return
    webpack(webpackConfig, (err, stats) => {
      if (err) {
        return reject(err);
      }
      if (stats.hasErrors()) {
        return reject(new Error(stats.compilation.errors.join('\n')));
      }
      console.log(stats.toString({
        chunks: false,
        colors: true,
      }));
      resolve();
    });
  })
)));


/*
 * Global tasks
 * ~~~~~~~~~~~~
 */

gulp.task('build', gulp.series('build-webpack-assets'));


/*
 * Development tasks
 * ~~~~~~~~~~~~~~~~~
 */

gulp.task('webpack-dev-server', gulp.series(() => {
  const devWebpackConfig = Object.create(webpackConfig);
  devWebpackConfig.mode = 'development';
  devWebpackConfig.devtool = 'eval';
  devWebpackConfig.devServer = { hot: true };
  devWebpackConfig.entry = {
    App: [
      `${jsDir}/App.js`, `${sassDir}/App.scss`,
      `webpack-dev-server/client?http://localhost:${WEBPACK_DEV_SERVER_PORT}`,
      'webpack/hot/only-dev-server',
    ],
  };
  devWebpackConfig.module = {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: 'babel-loader' },
      { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
      { test: /\.txt$/, use: 'raw-loader' },
      { test: /\.(png|jpg|jpeg|gif|svg|woff|woff2)([\?]?.*)$/, type: 'asset/inline' },
      { test: /\.(eot|ttf|wav|mp3|otf)([\?]?.*)$/, type: 'asset/resource' },
    ],
  };
  devWebpackConfig.output = {
    path: path.resolve(__dirname, staticDir),
    publicPath: `http://localhost:${WEBPACK_DEV_SERVER_PORT}/static/`,
    filename: '[name].js',
  };
  devWebpackConfig.plugins = [
    new webpack.LoaderOptionsPlugin({ debug: true }),
    new webpack.HotModuleReplacementPlugin(),
  ];

  // Start a webpack-dev-server
  new WebpackDevServer(webpack(devWebpackConfig), {
    static: {
      directory: path.resolve(__dirname, staticDir, '..'),
      publicPath: '/static/',
    },
    headers: { 'Access-Control-Allow-Origin': '*' },
    hot: true,
  }).listen(WEBPACK_DEV_SERVER_PORT, 'localhost', (err) => {
    if (err) throw new gutil.PluginError('webpack-dev-server', err);
    gutil.log(
      '[webpack-dev-server]',
      `http://localhost:${WEBPACK_DEV_SERVER_PORT}/webpack-dev-server/`,
    );
  });
}));
