module.exports = {
  devServer: {
    host:'127.0.0.1',
    port:'3333',
    proxy: {
      '/api': {
        target: 'https://store.jddj.com',
        changeOrigin: true, //是否跨域
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
}
