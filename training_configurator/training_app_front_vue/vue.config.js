const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})



const webpack = require('webpack')
module.exports = defineConfig({
    transpileDependencies: true,
    "publicPath": "/",
    "assetsDir": "static",
    "indexPath": "templates/index.html",
    configureWebpack: {
        plugins: [
            new webpack.IgnorePlugin({
                resourceRegExp: /^\.\/locale$/,
                contextRegExp: /moment$/
            }),
        ]
    },
    "filenameHashing": true,

    "devServer": {
        "proxy": {
            "^/api": {
                "target": "http://localhost:8000",
                "ws": true,
                "changeOrigin": true
            },
            "^/admin": {
                "target": "http://localhost:8000",
                "ws": true,
                "changeOrigin": true
            },

            "^/accounts": {
                "target": "http://localhost:8000",
                "ws": true,
                "changeOrigin": true
            },
        },
    }
})