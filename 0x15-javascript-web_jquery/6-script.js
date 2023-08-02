#!/usr/bin/node
// a script that update a header
const $ = window.$;
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
});
