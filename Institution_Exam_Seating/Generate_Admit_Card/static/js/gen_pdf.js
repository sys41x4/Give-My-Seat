$(document).ready(function() {
    $('#send-message').on('submit', function(event) {
        // roll = $('#roll').val()
        // document.getElementById('preview_admit_card')[0].src = window.location.origin+'/'+roll
      $.ajax({
         data : JSON.stringify({
            roll: $('#roll').val(),
            aadhar: $('#aadhar').val(),
                }),
            type : 'POST',
            url : '/get_admit_link',
            dataType: 'json',
            contentType: 'application/json',
            headers: {'roll':roll, 'aadhar':aadhar}
           })
       .done(function(data) {
         // $('#std_name').text(data.std_name).show();
         // $('#branch_name').text(data.branch_name).show();
         $('#roll_num').text(data.roll_num).show();
         $('#aadhar_num').text(data.aadhar_num).show();
         // $('#block_num').text(data.block_num).show();
         // $('#room_num').text(data.room_num).show();
         // $('#row').text(data.row).show();
         // $('#column').text(data.column).show();
         // $('#base64_qr_str').text(data.base64_qr_str).show();
         // $('#preview_admit_card').src(window.location.origin+'/'+data.roll_num).show();
         // document.getElementById("demo").innerHTML = "Paragraph changed.";
         // document.getElementsByTagName('iframe')[0].src = '/'+data.roll_num+'/'+data.aadhar_num
         // document.getElementsByTagName('admit_card')[0].src = window.location.origin+'/'+roll
         // iframe.attr('src', window.location.origin + '' + roll);
        //  window.setInterval(function() {
        //   document.querySelector('iframe.reload').setAttribute('src', '/'+data.roll_num+'/'+data.aadhar_num);
        // }, 5000);
        
     });
     // console.log('Receiver ='+$('#receiver').val())
     event.preventDefault();
     });
});

// function myFunction() {
//   document.getElementById("demo").innerHTML = "Paragraph changed.";
// }

function gen_admitcard() {
    document.getElementsByTagName('admit_card')[0].src = window.location.origin+'/'+roll
}

function iframeDidLoad() {
}

document.getElementById("show_admit_card").onclick = function () {
    location.href = window.location.origin+'/'+$('#roll').val()
};

function gen_admitcard() {
  // var e = document.getElementById("MySelectMenu");
  // var newSrc = e.options[e.selectedIndex].value;
  document.getElementById("preview_admit_card").src='/'+$('#aadhar').val()+'/'+$('#roll').val();
  document.getElementById("download_admit_card").href='/'+$('#aadhar').val()+'/'+$('#roll').val();

}