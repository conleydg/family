//For getting CSRF token
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
           }
        }
    }
return cookieValue;
}


//For doing AJAX post

//When submit is clicked
$("#submit").click(function(e) {

//Prevent default submit. Must for Ajax post.Beginner's pit.
e.preventDefault();


var video = $('#id_url').val();

var title = $('#id_title').val();

//Prepare csrf token
var csrftoken = getCookie('csrftoken');
  $("#id_url").change(function () {
    console.log( $(this).val() );
  });
  $.ajax({
    url:'/api/Movie/',
    type: "POST",
    data: {video: video, title: title, csrfmiddlewaretoken : csrftoken},
    success:function(response){window.location.reload();},
    complete:function(){},
    error:function (xhr, textStatus, thrownError){}
});
});
