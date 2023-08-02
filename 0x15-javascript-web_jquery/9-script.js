#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
