var env = (process.env.ENV || 'local').toLowerCase();

// Source and destination dirs
var src = './betly/static/src/';
var dest = './betly/static/dest/';

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
    src: src + 'js/app.js',
    dest: dest + 'js/',
    debug: (env !== 'production'),
    inputName: 'app.js'
  },
}
