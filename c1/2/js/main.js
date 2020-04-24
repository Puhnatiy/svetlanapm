function setCookie(name, value, options = {}) {

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}

function is_checked(name){
let a  = -1;
if ($(name).is(':checked')){
	a=1;
} else {
	a=0;
}
return a
}

$(document).ready(function () {
//deleteCookie('checkbox1');
let cook = 0;
ch1 = getCookie('checkbox1');
ch2 = getCookie('checkbox2');
ch3 = getCookie('checkbox3');
ch4 = getCookie('checkbox4');
ch5 = getCookie('checkbox5');
ch6 = getCookie('checkbox6');
if (ch1 != undefined){
  if(ch1==1){  $("#checkbox1").attr("checked", true);  }
  if(ch2==1){  $("#checkbox2").attr("checked", true);  }
  if(ch3==1){  $("#checkbox3").attr("checked", true);  }
  if(ch4==1){  $("#checkbox4").attr("checked", true);  }
  if(ch5==1){  $("#checkbox5").attr("checked", true);  }
  if(ch6==1){  $("#checkbox6").attr("checked", true);  }
$("input.group1").attr("disabled", true);
$("#save").attr("disabled", true);

//$("#save").attr("disabled", true);

}

let a = 0;
    //$("input.group1").attr("disabled", true);
$("#save").click(function(){ 
//if ($('#checkbox1').is(':checked')){
//	a=1;
//} else {
//	a=0;
//}
setCookie('checkbox1', is_checked('#checkbox1'), {secure: true, 'max-age': 7200});
setCookie('checkbox2', is_checked('#checkbox2'), {secure: true, 'max-age': 7200});
setCookie('checkbox3', is_checked('#checkbox3'), {secure: true, 'max-age': 7200});
setCookie('checkbox4', is_checked('#checkbox4'), {secure: true, 'max-age': 7200});
setCookie('checkbox5', is_checked('#checkbox5'), {secure: true, 'max-age': 7200});
setCookie('checkbox6', is_checked('#checkbox6'), {secure: true, 'max-age': 7200});
alert("Cookies сохранены");
$("input.group1").attr("disabled", true);
$("#save").attr("disabled", true);
});
});