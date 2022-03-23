from . import db

class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    number_of_bedrooms = db.Column(db.Integer)
    number_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(20))
    description = db.Column(db.String(1024))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, number_of_bedrooms, number_of_bathrooms, location, price, property_type, photo):
        self.title = title
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.photo = photo


