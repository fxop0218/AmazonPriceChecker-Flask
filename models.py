from database import db

# many to many table
user_product = db.Table("user_product",
                        db.Column("user_id", db.Integer, db.ForeignKey("user_.id")),
                        db.Column("product_id", db.Integer, db.ForeignKey("product.id"))
                        )


# Class name in lowercase
class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False, unique=True)
    name = db.Column(db.String(252), nullable=False)
    first_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    last_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)

    def __str__(self):
        return (f"Id: {self.id} "
                f"Url: {self.url[:30]} "
                f"name {self.name[:20]} "
                f"first price: {self.first_price[:30]} "
                f"last price: {self.last_price[:30]} "
                f"last update: {self.last_update[:30]} "
                )


class user_(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    following = db.relationship("product", secondary=user_product, backref="followers")

    def __str__(self):
        return (f"Id: {self.id} "
                f"Name: {self.username} ")

    # def __int__(self, username, password):
    #     self.username = username
    #     self.password = password
