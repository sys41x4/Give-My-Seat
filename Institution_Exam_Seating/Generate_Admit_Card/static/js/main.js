$(document).ready(function() {
    $('#generate-admitcard').on('submit', function(event) {
      $.ajax({
         data : JSON.stringify({
            roll: $('#roll').val(),
            aadhar: $('#aadhar').val(),
                }),
            type : 'POST',
            url : '/generate_admitcard',
            dataType: 'json',
            contentType: 'application/json',
            headers: {'roll':roll, 'aadhar':aadhar}
           })
       .done(function(data) {
         $('#roll_num').text(data.roll_num).show();
         $('#aadhar_num').text(data.aadhar_num).show();
        
     });
     event.preventDefault();
     });
});


document.getElementById("show_admit_card").onclick = function () {
    location.href = window.location.origin+'/'+$('#roll').val()
};

function gen_admitcard() {
  document.getElementById("preview_admit_card").src='/'+$('#aadhar').val()+'/'+$('#roll').val();
  document.getElementById("download_admit_card").href='/'+$('#aadhar').val()+'/'+$('#roll').val();

}