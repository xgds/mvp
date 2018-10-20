const CopyWebpackPlugin = require('copy-webpack-plugin')

// edit stuff here
const entry = {
  table: './src/pages/table/index.js',
  map:   './src/pages/map/index.js',
}
// end

var plugins = [];
for (i in entry) {
  plugins.push(
    new CopyWebpackPlugin([{
      from: './src/pages/html/index.html',
      to: './' + i + '/index.html',
    }])
  );
}

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        }
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ],
      },
      {
        test: /\.scss$/,
        use: [
          'style-loader', // creates style nodes from JS strings
          'css-loader',   // translates CSS into CommonJS
          'sass-loader'   // compiles Sass to CSS, using Node Sass by default
        ]
      }
    ]
  },
  plugins: plugins,
  entry: entry,
  output: {
    path: __dirname + '/dist',
    filename: '[name]/bundle.js',
  }
};
