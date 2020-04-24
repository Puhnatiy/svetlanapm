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
// Пример использования:


window.onload = function () {
let gorod;
gorod = getCookie('city');
//deleteCookie('city');
console.log(gorod);
if (gorod == undefined){
document.getElementById('city').style.display = 'block';

document.forms[0].elements[0].onchange = function () {
city = document.forms[0].elements[0].value;
setCookie('city', city, {secure: true, 'max-age': 7200});
}
}
else{

document.getElementsByClassName('city_cookie')[0].style.display = 'block';
let string1 = "Ваш город — " + gorod;
console.log(string1);
document.getElementsByClassName('city_cookie_p')[0].innerHTML = string1;
}
document.getElementsByClassName('clear')[0].onclick =  function(){
deleteCookie('city');
alert('Кука города удалена');
} 



}
