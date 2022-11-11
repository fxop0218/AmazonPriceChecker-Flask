from database import db
from flask import Flask, render_template
from flask_migrate import Migrate
from models import user, product

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
    app.logger.debug(f"List")
    return render_template("index.html")