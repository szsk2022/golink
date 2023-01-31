const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
const path = require('path');
var JavaScriptObfuscator = require('webpack-obfuscator');