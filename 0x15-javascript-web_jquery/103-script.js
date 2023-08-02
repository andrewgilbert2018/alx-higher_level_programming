#!/usr/bin/node
const $ = window.$;
function GetHello () {
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
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    GetHello();
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      GetHello();
    }
  });
});
