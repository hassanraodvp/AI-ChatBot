$(document).ready(function () {
  $("#animated-text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });
});

// Siri Wave

document.addEventListener("DOMContentLoaded", function () {
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 900,
    height: 200,
    style: "ios9",
    amplitude: 1,
    speed: 0.3,
    autostart: true,
  });
  // Siri Message Animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });
  // Mic Button Click Event
  $("#mic_btn").click(function () { 
    eel.playAssistantSound()
    $(".Oval").attr("hidden", true);
    $(".SiriWave").attr("hidden", false);
  });
});
