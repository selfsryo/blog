if (process.env.NODE_ENV === 'production') {
  module.exports = {
    outputDir: '../static',
    assetsDir: '../static/blog',
    indexPath: '../templates/blog/index.html',
    publicPath: '/',
  }
}
