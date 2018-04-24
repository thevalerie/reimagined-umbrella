import time
from flask import session
from model import Message, db

def query_db_for_messages():
    """Get all messages from the db in order"""

    all_messages = db.session.query(Message).order_by(Message.message_id).all()

    messages_data = [{'message_id': message.message_id,
                      'ts_readable': message.ts_readable(),
                      'message_body': message.message_body} for message in all_messages]

    return messages_data


def add_message_to_db(message_body):
    """Create new message object, add to the db, return the object"""

    new_message = Message(message_ts=int(time.time()), message_body=message_body)

    db.session.add(new_message)
    db.session.commit()

    print "Added to DB:", new_message

    new_message_data = {
                        'message_id': new_message.message_id,
                        'ts_readable': new_message.ts_readable(),
                        'message_body': new_message.message_body
                        }

    return new_message_data
