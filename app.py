from database import db
from flask import Flask, render_template, session, redirect, url_for, request
from flask_migrate import Migrate
from helpful_funcions import encript

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
        user = user_.query.filter_by(username=session.get("user")).one()
        all_products = user.following
        app.logger.debug(f"{all_products}")
        return render_template("index.html", user=session.get("user"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("index"))
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = encript(request.form["password"])
        account = user_.query.filter_by(username=username).one()
        app.logger.debug(f"Account: {account}")
        app.logger.debug(f"username: {username}")
        if account:
            if account.password == str(password):
                session["logged_in"] = True
                session["user"] = account.username
                return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    msg = ""
    if session.get("logged_in"):
        return redirect(url_for("index"))

    if request.method == "POST":
        if len(request.form["password"]) == 0 or len(request.form["username"]) == 0:
            msg = "Introduce correct values"
        else:
            try:
                username = request.form["username"]
                password = encript(request.form["password"])
                new_user = user_(username=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                app.logger.debug("User created correctly")
                session["logged_in"] = True
                session["user"] = new_user.username
                return redirect(url_for("index"))
            except Exception as e:
                msg = "This username its also used"

    # if request.method == "GET":
    #     if len(request.form["password"]) == 0 or len(request.form["username"]) == 0:
    #         msg = "Incorrect"
    #     else:
    #         try:
    #             username = request.form["username"]
    #             password = encript(request.form["password"])
    #             new_user = user_(username=username, password=password)
    #             db.session.add(new_user)
    #             db.session.commit()
    #             app.logger.debug("User created correctly")
    #         except Exception as e:
    #             msg = "This username is used"
    #             return render_template("register.html", msg=msg)
    #         return redirect(url_for("index"))

    return render_template("register.html", msg=msg)


@app.route("/add_product")
def add_product():
    return render_template("add.html")


@app.route("/exit")
def exit():
    session.pop("logged_in")
    session.pop("user")
    return redirect(url_for("index"))
