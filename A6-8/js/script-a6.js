function dummy(arg) {
  console.log(arg);
}
let wpb=0;


function plusProgressbar1() {
	wpb=wpb+1;
	wpbpercent=wpb+"%";
	console.log(wpbpercent);	
$(".progress-bar").width(wpbpercent);

}
function plusProgressbar3() {
	wpb=wpb+3;
	wpbpercent=wpb+"%";
	console.log(wpbpercent);	
$(".progress-bar").width(wpbpercent);

}
function plusProgressbar7() {
	wpb=wpb+7;
	wpbpercent=wpb+"%";
	console.log(wpbpercent);	
$(".progress-bar").width(wpbpercent);

}

function init() {

  console.log("скрипт подгрузился");
  $(".btn-primary").on('click', plusProgressbar1);
  $(".btn-secondary").on('click', plusProgressbar3);
  $(".btn-success").on('click', plusProgressbar7);
}

$(document).ready(init);