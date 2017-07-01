const {resolve} = require('path');
const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: {
    app: resolve('./src/app.js')
  },

  devtool: 'source-maps',

  output: {
    path: path.join(__dirname, 'public'),
    filename: 'bundle.js',
    publicPath: '/public/'
  },

  module: {
    rules: [{
      test: /\.js$/,
      loader: 'buble-loader',
      include: [resolve('.')],
      exclude: [/node_modules/],
      options: {
        objectAssign: 'Object.assign'
      }
    }]
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ]
};
