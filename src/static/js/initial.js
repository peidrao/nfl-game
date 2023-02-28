$(".initial-option").on("click", function () {
  let conferenceID = this.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  window.location.href = `http://localhost:8000/conferences/${conferenceID}/teams/`;
});

$(".team-item").on("click", function () {
  let teamID = this.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "POST",
    dataType: "json",
    headers: headers,
    data: { teamID: teamID },
    url: "/api/select_team/",
    success: function (response) {
      window.location.href = `http://localhost:8000/account/`;
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
