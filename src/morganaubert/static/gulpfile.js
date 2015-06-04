/* Gulp packages */
'use strict';

/* Include Gulp & Tools we'll use */
var gulp = require('gulp'),
    path = require('path'),
    watch = require('gulp-watch'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
	less = require('gulp-less'),
    minifyCSS = require('gulp-minify-css'),
    browserSync = require('browser-sync');
var reload = browserSync.reload;

/* Global variables */
var application_name = 'application';

/* DIRS */
var build_dir = '_build';
var bower_dir = 'bower_components';
var less_dir = 'less';
var js_dir = 'js';


/* Include all needed javascript packages here. */
var packages_includes = [
    bower_dir + '/jquery/dist/jquery.js',
    bower_dir + '/jquery.easing/js/jquery.easing.js',
    bower_dir + '/bootstrap/dist/js/bootstrap.js',
];

/* Include all application related files here. */
var application_includes = [
    js_dir + '/**/*.js',
];

/* Include all of the project styling here.
 * Third-party less files coul be included here or they could
 * be included on a main 'theme' LESS file. */
var style_includes = [
    less_dir + '/theme.less',
];

/* Task to build our javascript packages. */
gulp.task('build-js-packages', function () {
    gulp.src(packages_includes)
        .pipe(concat(application_name + '.packages.js'))
        .pipe(rename({suffix: '.min'}))
        .pipe(uglify())
        .pipe(gulp.dest(build_dir + '/js'))
});

/* Task to build our javascript application. */
gulp.task('build-js-application', function () {
    gulp.src(application_includes)
        .pipe(concat(application_name + '.js'))
        .pipe(gulp.dest(build_dir + '/js'))
});

/* Task to build our application style. */
gulp.task('build-css', function () {
	gulp.src(style_includes)
		.pipe(less())
        .pipe(rename({suffix: '.min'}))
        .pipe(minifyCSS())
		.pipe(gulp.dest(build_dir + '/css'));
});

/* Task to build our production javascript application. */
gulp.task('build-js-production', ['build-css'], function () {
    gulp.src(packages_includes.concat(application_includes))
        .pipe(concat(application_name + '.production.js'))
        .pipe(rename({suffix: '.min'}))
        .pipe(uglify())
        .pipe(gulp.dest(build_dir + '/js'))
});

/* Task to build our application. */
gulp.task('build-application', ['build-js-packages', 'build-js-application', 'build-css']);

/* Default task to use during development.
 * It provides livereloading by using BrowserSync. */
gulp.task('default', ['build-application', ], function () {
    browserSync({
        notify: false,
        proxy: "127.0.0.1:8000"
    });
 
    gulp.watch(packages_includes, ['build-js-packages', reload]);
    gulp.watch(application_includes, ['build-js-application', reload]);
    gulp.watch([less_dir + '/**/*.less',], ['build-css', reload]);
    gulp.watch(['../templates/**/*.html',], [reload]);  // Django templates
});
