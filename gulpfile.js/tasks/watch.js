var gulp = require('gulp');
var config = require('../config.js');

gulp.task('watch', function() {
  if(config.env.name === 'local') {
    gulp.watch(config.src + '**/*.js*', ['browserify']);
    gulp.watch(config.src + '**/*.sass', ['sass']);
  }
});
