var gulp = require('gulp');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');
var config = require('../config.js').browserify;

gulp.task('browserify', function() {
  return gulp.src(config.src, { read: false })
    .pipe(browserify({ transform: ['coffeeify'], extensions: ['.coffee'], debug: config.debug }))
    .on('error', function(err) {console.log(err);})
    .pipe(concat(config.outputName))
    .pipe(gulp.dest(config.dest));
});
