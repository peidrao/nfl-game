$(".button-start-season").on("click", (e) => {
  e.preventDefault();

  const headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/season/start/",
    headers: headers,
    // data: { checked: checked },
    success: function (response) {
      window.location.reload();
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
