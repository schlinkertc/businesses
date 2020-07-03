from . import db

class Business(db.Model):
    """Data model for businesses"""
    
    __tablename__ = 'businesses'
    __table_args__ = {'extend_existing': True}
    
    # Columns
    id = db.Column(db.String(50),primary_key=True)
    alias = db.Column(db.String(50))
    name = db.Column(db.String(50))
    image_url = db.Column(db.String(50))
    url = db.Column(db.String(50))
    price = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    display_phone = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    address1 = db.Column(db.String(50))
    address2 = db.Column(db.String(50))
    address3 = db.Column(db.String(50))
    city = db.Column(db.String(50))
    zip_code = db.Column(db.String(50))
    country = db.Column(db.String(50))
    state = db.Column(db.String(50))
    display_address = db.Column(db.String(50))
    categories = db.Column(db.String(50))
    pickup = db.Column(db.Boolean)
    delivery = db.Column(db.Boolean)
    
    def __repr__(self):
        return '<Business {}>'.format(self.name)