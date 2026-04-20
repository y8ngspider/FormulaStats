$(document).ready(function() {
  let drivers = $(".drivers");
  const data = window.data || [];

  function display_top3(){
    data.slice(0,3).forEach((s) => {
      let summary = s.summary.substring(0, 100) + '...';
      let newdriver = $(`
        <div class="col-md-4">
          <div class="card h-100 driver-card">
            <a href="/view/${s.id}">
              <img class="card-img-top driver_image" src="${s.media_link}" alt="${s.name}">
            </a>
            <div class="card-body">
              <h5 class="card-title"><a href="/view/${s.id}" class="text-decoration-none text-dark">${s.name}</a></h5>
              <p class="text-muted small">${s.championships} championships • ${s.career_start_year}–${s.career_end_year}</p>
              <p class="card-text">${summary}</p>
              <a href="/view/${s.id}" class="btn btn-sm btn-primary">View Profile</a>
            </div>
          </div>
        </div>`);
      drivers.append(newdriver);
    });
  };
  display_top3();

  $("#submission").on("submit", function(e){
    let query = $('input[name="q"]').val();
    if(query.trim() === ''){
      e.preventDefault();
      $('input[name="q"]').val('').focus();
    }
  });

  $("#add-form").on("submit", function(e) {
    e.preventDefault();

    $(".text-danger").text('');
    $(".form-control").removeClass('is-invalid');
    $("#success-msg").addClass('d-none');

    let formData = {
      name:              $("#name").val(),
      media_link:        $("#media_link").val(),
      career_start_year: $("#career_start_year").val(),
      career_end_year:   $("#career_end_year").val(),
      championships:     $("#championships").val(),
      wins:              $("#wins").val(),
      pole_positions:    $("#pole_positions").val(),
      podiums:           $("#podiums").val(),
      teams:             $("#teams").val(),
      notable_races:     $("#notable_races").val(),
      summary:           $("#summary").val()
    };

    let hasError = false;
    for (let field in formData) {
      if (formData[field].trim() === '') {
        $(`#err-${field}`).text('This field is required');
        $(`#${field}`).addClass('is-invalid');
        hasError = true;
      }
    }
    if (hasError) return;

    $.ajax({
      type: "POST",
      url: "/add-driver",
      contentType: "application/json",
      data: JSON.stringify(formData),
      success: function(response) {
        $("#success-msg").removeClass('d-none');
        $("#see-it-link").attr('href', `/view/${response.id}`);

        $("#add-form")[0].reset();
        $("#name").focus();
      },
      error: function(xhr) {
        let errors = xhr.responseJSON.errors;
        for (let field in errors) {
          $(`#err-${field}`).text(errors[field]);
          $(`#${field}`).addClass('is-invalid');
        }
      }
    });
  });

  $("#edit-form").on("submit", function(e) {
    e.preventDefault();


    $(".text-danger").text('');
    $(".form-control").removeClass('is-invalid');

    let driverId = $("#driver-id").val();

    let formData = {
      name:              $("#name").val(),
      media_link:        $("#media_link").val(),
      career_start_year: $("#career_start_year").val(),
      career_end_year:   $("#career_end_year").val(),
      championships:     $("#championships").val(),
      wins:              $("#wins").val(),
      pole_positions:    $("#pole_positions").val(),
      podiums:           $("#podiums").val(),
      teams:             $("#teams").val(),
      notable_races:     $("#notable_races").val(),
      summary:           $("#summary").val()
    };


    let hasError = false;
    for (let field in formData) {
      if (formData[field].trim() === '') {
        $(`#err-${field}`).text('This field is required');
        $(`#${field}`).addClass('is-invalid');
        hasError = true;
      }
    }
    if (hasError) return;

    // send update to server then go to view page
    $.ajax({
      type: "POST",
      url: `/update-driver/${driverId}`,
      contentType: "application/json",
      data: JSON.stringify(formData),
      success: function(response) {
        window.location.href = `/view/${driverId}`;
      },
      error: function(xhr) {
        let errors = xhr.responseJSON.errors;
        for (let field in errors) {
          $(`#err-${field}`).text(errors[field]);
          $(`#${field}`).addClass('is-invalid');
        }
      }
    });
  });


  $("#discard-btn").on("click", function() {
    let driverId = $("#driver-id").val();
    let confirmed = confirm("Are you sure you want to discard your changes?");
    if (confirmed) {
      window.location.href = `/view/${driverId}`;
    }

  });

});