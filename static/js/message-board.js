"use strict";

// display new message on the board
function displayNewMessage(data) {
    // create divs for new message
    let newTimeStamp = $("<div class='row msg-timestamp'></div>").text(data['ts_readable']);
    let newMessage = $("<div class='row posted-msg'></div>").text(data['message_body']);
    // add them to the container
    $('#messages-container').append(newTimeStamp, newMessage);
    // if the welcome message is showing, hide it
    if ($('#first-visitor').css('visibility') == "visible") {
        $('#first-visitor').hide();
    }
}

// add a new message to the db
function addMessage(evt) {
    evt.preventDefault();

    let payload = {'message_body': $('#newMessageBody').val()};

    // send message body data to the backend to add to the db
    $.post('/add_message.json', payload, function(data) {
        $('#newMessageBody').val(''); // reset the new message text box
        displayNewMessage(data) // add the new message to messages
    });
}

// event handler for new message form submission
$('#newMessageForm').on('submit', addMessage)