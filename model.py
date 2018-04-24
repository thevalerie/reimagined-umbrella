import os
import time
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    """Messages table"""

    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    message_ts = db.Column(db.Integer, nullable=False)
    message_body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """Show relevant info for debugging"""

        return "\n<Message {}: {}>".format(self.message_id, self.message_body)

    def ts_readable(self):
        """Return the timestamp as a human readable date in local time"""

        return time.ctime(self.message_ts)


def connect_to_db(app, db_uri='postgresql:///umbrella'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."