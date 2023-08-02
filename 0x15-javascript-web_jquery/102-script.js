#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      type: 'GET',
      data: {
        lang: $('INPUT#language_code').val()
      },
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
