$(document).ready(function () {
  eel.expose(displaySpeakMsg);
  // Display Speak Msg
  function displaySpeakMsg(msg) {
    $(".siri-message li:first").text(msg);
    $(".siri-message").textillate("start");
  }
  // Auto Hide Siri Wave after speak
  eel.expose(showHood);
  function showHood() {
    $(".Oval").attr("hidden", false);
    $(".SiriWave").attr("hidden", true);
  }
});
