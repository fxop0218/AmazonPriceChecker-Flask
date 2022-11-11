from database import db

# many to many table
user_product = db.Table("user_product",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                        db.Column("product_id", db.Integer, db.ForeignKey("product.id"))
                        )


# Class name in lowercase
class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(252), nullable=False)
    first_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    last_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    following = db.relationship("product", secondary=user_product, backref="followers")

    def __str__(self):
        return (f"Id: {self.id} "
                f"Name: {self.name} ")
