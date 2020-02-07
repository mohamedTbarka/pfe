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
    // start statement
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    
    $("form[name='registration']").validate({
      // Specify validation rules
      rules: {
        // The key name on the left side is the name attribute
        // of an input field. Validation rules are defined
        // on the right side
        image: {
          required: true
        },
        fullname: "required",
        email: {
          required: true,
          // Specify that email should be validated
          // by the built-in "email" rule
          email: true
        },
        phone: {
          required: true
        }
      },
      // Specify validation error messages
      messages: {
        fullname: "Veuillez remplir ce champ",
        email: "Veuillez remplir ce champ",
        phone: "Veuillez remplir ce champ",
        image: "charger une image"
      },
      // Make sure the form is submitted to the destination defined
      // in the "action" attribute of the form when valid
      submitHandler: function(form) {
        form.submit();
        
      }
    });
    
    // end statement
    var current_url = document.location.href;
    $(".form").submit(function(e) {
      e.preventDefault();
    });
    $('a.start').on('click', function(){
      $('.content-one').slideUp();
      $('.content-one').addClass('hide');
      $('.content-one').removeClass('show');
      $('.content-two').slideDown();
      $('.content-two').removeClass('hide');
      $('.content-two').addClass('show');
    })
    $('a.to-step-3').on('click', function(){
      var fullname = $('input[name="fullname"').val();
      var email = $('input[name="email"').val();
      var phone = $('input[name="phone"').val();
      var img = $('#uploadlogo').val();

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
    // Radio Color Background
    $('.choice').on('click', function(){
      if($(this).find('input[type="radio"]').is(':checked')){
        $('.choice').removeClass('checked');
        $(this).addClass('checked');
      }
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