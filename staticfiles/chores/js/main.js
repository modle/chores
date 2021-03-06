$(document).ready( function() {
  $('.notSelectable').disableSelection();

  var mySwiper = new Swiper ('.swiper-container', {
      // Optional parameters
      direction: 'vertical',
      loop: true
    })
});


function mark_chore_done(chore_slug) {
    $.ajax({
        url : "/mark_chore_done/", // the endpoint
        type : "POST", // http method
        data : { chore : chore_slug }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            if (json.score) {
                $("#results_"+json.slug).prepend("<strong>DONE!</strong> <em style=\"color:red;\">"+json.score+" point(s)!</em>");
                $("#chore_details_"+json.slug).hide();
                $("#current_score").html(json.current_score);
            }
            else {
                $("#results_"+json.slug).html("<em>Too recently completed</em>");
//                $("#chore_details_"+json.slug).show();
//                $("#results_"+json.slug).prepend(json.last_completed_date);
            }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        }
    });
};



//mousedown(function(){
//    slug = this.id;
//}).

$(".chore_block").mousemove(function(){
    slug = this.id;
})

$(".chore_block").swipe({
  swipeRight:function(event, direction, distance, duration, fingerCount) {
    mark_chore_done(slug);
  },
  swipeLeft:function(event, direction, distance, duration, fingerCount) {
    window.location.href = "/chores/edit_chore/"+slug+".html";
  },
  threshold:50,
  allowPageScroll:"auto"
});



//
//function add_chore() {
//    $.ajax({
//        url : "/add_chore/", // the endpoint
//        type : "POST", // http method
//        data : { title : $('#title').val(),
//            category : $('#category').val(),
//            primary_assignee : $('#primary_assignee').val(),
//            secondary_assignee : $('#secondary_assignee').val(),
//            frequency_in_days : $('#frequency_in_days').val(),
//            priority : $('#priority').val(),
//            time_in_minutes : $('#time_in_minutes').val(),
//            effort : $('#effort').val()
//            }, // data sent with the post request
//
//        // handle a successful response
//        success : function(json) {
//            $('#title').val('');
//            $('#category').val('');
//            $('#primary_assignee').val('');
//            $('#secondary_assignee').val('');
//            $('#frequency_in_days').val('');
//            $('#priority').val('');
//            $('#time_in_minutes').val('');
//            $('#effort').val('');
//        },
//
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//        }
//    });
//};


//makes text non-selectable on mobile, and prevents the highlight on long-press function
$.fn.extend({
    disableSelection: function() {
        this.each(function() {
            this.onselectstart = function() {
                return false;
            };
            this.unselectable = "on";
            $(this).css('-moz-user-select', 'none');
            $(this).css('-webkit-user-select', 'none');
        });
        return this;
    }
});





// This function gets cookie with a given name
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
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
