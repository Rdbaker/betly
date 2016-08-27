var env = (process.env.ENV || 'local').toLowerCase();

// front end code source dir
var src = './apio/static/src/';
var dest = './apio/static/dest/';

module.exports = {
  env: {
    name: env
  },
  src: src,
  dest: dest,

  sass: {
    src: src + 'sass/app.sass',
    dest: dest + 'css/',
    settings: {
      includePaths: [
        src + 'sass/',
        './node_modules/'
      ]
    }
  },

  browserify: {
    src: src + 'coffee/app.coffee',
    dest: dest + 'js/',
    debug: (env !== 'production'),
    outputName: 'app.js'
  },
}
