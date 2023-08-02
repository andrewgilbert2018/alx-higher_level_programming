#!/usr/bin/node
// a script that toggles a class
const $ = window.$;
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
