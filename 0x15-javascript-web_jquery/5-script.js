#!/usr/bin/node
// a script that add a list element
const $ = window.$;
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});i
