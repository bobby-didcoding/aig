// Used to add a spinner to submit buttons
var temp_button_text;
function CustomFormSubmitPost(e) {
    var el = $(e);
    temp_button_text = el.text()
    el.attr('disabled', 'disabled').text("").append('<class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Loading...');
};
function CustomFormSubmitResponse(e) {
    var el = $(e);
    el.removeAttr('disabled').text(temp_button_text);
};

"use strict";
var FormControls = function () {

    var basicForm = function (){
        var form = $('#basicform')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#basicform button[type=submit]'));
            
            var formdata = form.serialize() 
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                success: function(json){
                    CustomFormSubmitResponse($('#basicform button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#basicform button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    var basicDataForm = function (){
        var form = $('#basicdataform')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#basicdataform button[type=submit]'));
            var formdata = new FormData(form[0]);

            //I would search for images in the form if I had more time but this will do for now
            formdata.append("FILE", $('#id_avatar')[0].files[0])

            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                processData: false,
                contentType: false,
                success: function(json){
                    console.log(json)
                    CustomFormSubmitResponse($('#basicdataform button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#basicdataform button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    var coordinateFormOne = function (){
        var form = $('#coordinateform1')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#coordinateform1 button[type=submit]'));
            
            var formdata = form.serialize() 
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                success: function(json){
                    CustomFormSubmitResponse($('#coordinateform1 button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#coordinateform1 button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    var coordinateFormTwo = function (){
        var form = $('#coordinateform2')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#coordinateform2 button[type=submit]'));
            
            var formdata = form.serialize() 
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                success: function(json){
                    CustomFormSubmitResponse($('#coordinateform2 button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#coordinateform2 button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    var coordinateFormThree = function (){
        var form = $('#coordinateform3')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#coordinateform3 button[type=submit]'));
            
            var formdata = form.serialize() 
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                success: function(json){
                    CustomFormSubmitResponse($('#coordinateform3 button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#coordinateform3 button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    var coordinateFormFour = function (){
        var form = $('#coordinateform4')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#coordinateform4 button[type=submit]'));
            
            var formdata = form.serialize() 
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                data: formdata,
                success: function(json){
                    CustomFormSubmitResponse($('#coordinateform4 button[type=submit]'));
                    ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
                },
                error: function(xhr){
                    CustomFormSubmitResponse($('#coordinateform4 button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            }) 
        });
    };

    return {
        init: function() { 
            basicForm();
            basicDataForm();
            coordinateFormOne();
            coordinateFormTwo();
            coordinateFormThree();
            coordinateFormFour();
        }
    };
}();

jQuery(document).ready(function () {
    // AJAXControls.init();
    // JCropControls.init();
    FormControls.init();
});


$(function() {
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
})
