from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_name):
    from src.models import User, Event, Message, EventInvitee, MessageRecipient, Invitee

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # db.drop_all(app=app)
    # db.create_all(app=app)

    from src.routes import user, database, event, twilio_sms, event_invitee, invitee, message, message_recipient
    user.add_routes(app)
    database.add_routes(app)
    event.add_routes(app)
    twilio_sms.add_routes(app)
    event_invitee.add_routes(app)
    invitee.add_routes(app)
    message.add_routes(app)
    message_recipient.add_routes(app)

    return app
