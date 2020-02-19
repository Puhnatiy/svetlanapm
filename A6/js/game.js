const numDivs = 36;
const maxHits = 10;

let hits = 0;
let miss_hits = 0;
let firstHitTime = 0;
let hitstemp = 0;

function round() {
  if(hits===0){ 
     firstHitTime = getTimestamp();
  }

  $(".target").text("");
  $(".target").removeClass("target");
  let divSelector = randomDivId();
     if ($(divSelector).hasClass("miss")) { 
       $(divSelector).removeClass("miss");
     }
  $(divSelector).addClass("target");
  hitstemp = hits + 1;
  $(divSelector).text(hitstemp);


  if (hits === maxHits) {
  $(".target").text("");
	$(".target").removeClass("target");
  $(".miss").removeClass("miss");
    endGame();
  }
}

function endGame() {
  $(".game").hide();
  let totalPlayedMillis = getTimestamp() - firstHitTime;
  let totalPlayedSeconds = Number(totalPlayedMillis / 1000).toPrecision(3);
  let totalGreen = 10 - miss_hits;
  $("#total-time-played").text(totalPlayedSeconds);
  $("#total-green").text(totalGreen);


  $("#win-message").removeClass("d-none");
}

function handleClick(event) {
  if ($(event.target).hasClass("target")) {
    hits = hits + 1;
    $(".miss").removeClass("miss");  

  
    round();
      
  }
  else{
     $(event.target).addClass("miss");
	   miss_hits = miss_hits + 1;
     hits = hits + 1;
	   round();
  }

}

function startGame(){
  $('#button-start').attr('disabled', true);
   round();
  $(".game-field").click(handleClick);
 }

function init() {
  
  $("#button-start").click(startGame);
 //round();
  //$(".game-field").click(handleClick);
  $("#button-reload").click(function() {
    location.reload();
	
  });
}



$(document).ready(init);
