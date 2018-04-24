from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, request, jsonify
from model import Message, connect_to_db, db
import helper

app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def message_board():
    """Message board homepage"""

    messages = helper.query_db_for_messages()

    return render_template("message-board.html", messages=messages)


@app.route('/add_message.json', methods=['POST'])
def add_new_message():
    """Add a new Message object to the database and send it back to be displayed"""

    # get the message body from the front end
    message_body = request.form.get('message_body')

    # add new message to the db
    new_message = helper.add_message_to_db(message_body)

    return jsonify(new_message)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
