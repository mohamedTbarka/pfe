/*function autoBg(){
  var current_w = $(window).width();
  var current_h = $(window).height();
  $('.bg_img').css('height',current_h+'px');
  $('.bg_img').css('width',current_w+'px');
}  
autoBg();
$(window).resize(function(){
  autoBg();
});
*/
$(document).ready(function($) {

  function readFile() {
  
    if (this.files && this.files[0]) {
      
      var FR= new FileReader();
      
      FR.addEventListener("load", function(e) {
        document.getElementById("uploadlogo").src = e.target.result;
        document.getElementById("ticker_value").value = e.target.result;
      }); 
      
      FR.readAsDataURL( this.files[0] );
    }
    
  }
  document.getElementById("uploadlogo").addEventListener("change", readFile);

    
    // end statement
    var current_url = document.location.href;
    $('form[name="registration"').submit(function(e) {
      $('.msg_error').hide();
      e.preventDefault();
      var fullname = $('input[name="fullname"').val();
      var email = $('input[name="email"').val();
      var phone = $('input[name="phone"').val();
      var img = $('#ticker_value').val();
      $.ajax({
        method: "POST",
        url: "/concours-saintvalentin/sinscrire/",
        data: {
          'full_name': fullname,
          'email': email,
          'telephone':phone,
          'ticket_base64': img.split("base64,")[1],
        },
        statusCode: {
          406: function(error){
            $('.msg_error').show();
            $('.msg_error').text('Attendez 24H pour reparticiper');
          },
          200: function(response){
            console.log('Inscription correcte');
            localStorage.setItem('quiz',JSON.stringify(response));
            window.location = '/concours-saintvalentin/quiz/';
          },
          500: function(message){
            console.log('Erreur 500', message.responseText);
          }
        }
      });
    });
    
    $('a.to-step-3').on('click', function(){
      

      // $.ajax({
      //   url: "sinscrire/",
      //   data: [
      //     'id':1,
      //     'name':
      //   ]
      // }).done(function() {
      //   $( this ).addClass( "done" );
      // });
      // GET DATA

      // $('.content-two').slideUp();
      // $('.content-two').addClass('hide');
      // $('.content-two').removeClass('show');
      // $('.content-three').slideDown();
      // $('.content-three').removeClass('hide');
      // $('.content-three').addClass('show');
    })
    $('a.to-step-4').on('click', function(){
      $('.content-three').slideUp();
      $('.content-three').addClass('hide');
      $('.content-three').removeClass('show');
      $('.content-four').slideDown();
      $('.content-four').removeClass('hide');
      $('.content-four').addClass('show');
    })
  
    // Upload btn on change call function
    $(".uploadlogo").change(function() {
      var filename = readURL(this);
      $(this).parent().children('span').html(filename);
    });
  
    // Read File and return value  
    function readURL(input) {
      var url = input.value;
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0] && (
        ext == "png" || ext == "jpeg" || ext == "jpg"
        )) {
        var path = $(input).val();
        var filename = path.replace(/^.*\\/, "");
        // $('.fileUpload span').html('Uploaded Proof : ' + filename);
        return "Ticket Téléchargé : "+filename;
      } else {
        $(input).val("");
        return "Seuls les formats d'image sont autorisés!";
      }
    }
    // Upload btn end
  
  });