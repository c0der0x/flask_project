from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")

@flask_app.route("/admin/")
def view_admin():
    return render_template("admin.jinja")

@flask_app.route("/articles/")
def view_articles():
    return render_template("articles.jinja")

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
    return render_template("article.jinja")
