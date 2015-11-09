
function mark_chore_done(chore_slug) {
    $.ajax({
        url : "/mark_chore_done/", // the endpoint
        type : "POST", // http method
        data : { chore : chore_slug }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $("#results_"+json.slug).prepend("<strong>DONE!</strong><br><em style=\"color:red; font-size:2em;\">"+json.score+" point(s)!</em>");
            $("#mark_done_"+json.slug).hide();
            $("#chore_details_"+json.slug).hide();
            $("#current_score").html(json.current_score);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        }
    });
};



$('#post-form').on('submit', function(event){
    event.preventDefault();
    alert("form submitted!")
    add_chore();
});


function add_chore() {
    $.ajax({
        url : "/add_chore/", // the endpoint
        type : "POST", // http method
        data : { title : $('#title').val(),
            category : $('#category').val(),
            primary_assignee : $('#primary_assignee').val(),
            secondary_assignee : $('#secondary_assignee').val(),
            frequency_in_days : $('#frequency_in_days').val(),
            priority : $('#priority').val(),
            time_in_minutes : $('#time_in_minutes').val(),
            effort : $('#effort').val()
            }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#title').val('');
            $('#category').val('');
            $('#primary_assignee').val('');
            $('#secondary_assignee').val('');
            $('#frequency_in_days').val('');
            $('#priority').val('');
            $('#time_in_minutes').val('');
            $('#effort').val('');
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        }
    });
};









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
