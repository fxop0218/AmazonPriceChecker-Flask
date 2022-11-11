from database import db
from flask import Flask, render_template, session, redirect, url_for, request
from flask_migrate import Migrate

from forms import UserFrom
from models import user_, product

app = Flask(__name__)

USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "amazon_flask_db"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# If separate the classes in other files need this
db.init_app(app)

# Configurate flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# Configuration of flask-wtf
app.config["SECRET_KEY"] = "SECRET_KEY"  # Change in production service


@app.route("/")
def index():
    app.logger.debug(f"List {session.get('logged_in')}")
    if not session.get("logged_in"):
        # Set cookies
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


@app.route("/login")
def login():
    if session.get("logged_in"):
        return redirect(url_for("index"))
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        account = user_.query.get_or_404(username)
        if account:
            session["logged_in"] = True
            return redirect(url_for("index"))

            # add cookie
    return render_template("login.html")


@app.route("/register", methods=["POST","GET"])
def register():
    register_user = user_()
    user_form = UserFrom(obj=register_user)
    if request.method == "POST":
        if user_form.validate_on_submit():
            user_form.populate_obj(register_user)
            db.session.add(register_user)
            db.session.commit()
            session["logged_id"] = True
            return redirect(url_for("index"))
    return render_template("register.html", user_form = user_form)


@app.route("/add_product")
def add_product():
    return render_template("add.html")
