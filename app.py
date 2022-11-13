import datetime

from database import db
from flask import Flask, render_template, session, redirect, url_for, request
from flask_migrate import Migrate
from helpful_funcions import encript, add_db_product
from amazonScrapper.amazon_scrapper import scrap_product, scrapp_only_price

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
        num_prod = len(all_products)
        app.logger.debug(f"{all_products}")
        return render_template("index.html", user=session.get("user"), products=all_products, num_prod=num_prod)


@app.route("/login", methods=["POST", "GET"])
def login():
    msg = ""
    if session.get("logged_in"):
        return redirect(url_for("index"))
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = encript(request.form["password"])
        try:
            account = user_.query.filter_by(username=username).one()
            app.logger.debug(f"Account: {account}")
            app.logger.debug(f"username: {username}")
            if account:
                if account.password == str(password):
                    session["logged_in"] = True
                    session["user"] = account.username
                    return redirect(url_for("index"))
                msg = "Incorrect user or password"
        except Exception as e:
            msg = "Incorrect user or password"

    return render_template("login.html", msg=msg)


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
    return render_template("register.html", msg=msg)


@app.route("/delete/<int:prod_id>")
def delete_product(prod_id):
    username = session.get("user")
    act_user = user_.query.filter_by(username=username).one()
    selected_product = product.query.get_or_404(prod_id)
    act_user.following.remove(selected_product)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        url = request.form["link"]
        try:
            ex_prod = product.query.filter_by(url=url).one()
        except Exception as ex:
            scraped_prod = scrap_product(url)
            added = add_db_product(scraped_prod)

            if not added:
                return render_template("add.html")  # TODO add error information
            else:
                ex_prod = product.query.filter_by(url=url).one()
        # TODO add the object to the user
        print(session.get("user"))
        act_user = user_.query.filter_by(username=session.get("user")).one()

        act_user.following.append(ex_prod)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/reload")
def reload_price():
    reload_user = user_.query.filter_by(username=session.get("user")).one()
    products_to_reload = reload_user.following

    if len(products_to_reload) <= 0:
        for product_ in products_to_reload:
            # TODO add custom function to get
            act_product = product.query.get_or_404(product_)
            product_.last_price = scrapp_only_price(act_product.url)
            product_.last_update = datetime.datetime.now()
            db.session.commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/exit")
def exit_login():
    session.pop("logged_in")
    session.pop("user")
    return redirect(url_for("index"))
