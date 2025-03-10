from flask import Flask
from flask import render_template

from .models import db
from .mod_main import main
from .mod_blog import blog
from .mod_admin import admin


import os

flask_app = Flask(__name__)
flask_app.config.from_pyfile("/vagrant/configs/default.py")
if "MDBLOG_CONFIG" in os.environ:
    flask_app.config.from_envvar("MDBLOG_CONFIG")
db.init_app(flask_app)

flask_app.register_blueprint(main)
flask_app.register_blueprint(blog)
flask_app.register_blueprint(admin)
@flask_app.errorhandler(500)
def internal_server_error(error):
    return render_template("errors/500.jinja"), 500

@flask_app.errorhandler(404)
def internal_server_error(error):
    return render_template("errors/404.jinja"), 404

## CLI COMMAND
def init_db(app):
    with app.app_context():
        db.create_all()
        print("database inicialized")

        default_user = User(username="admin")
        default_user.set_password("admin")

        db.session.add(default_user)
        db.session.commit()
        print("default user was created")