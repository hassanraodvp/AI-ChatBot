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
