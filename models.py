from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = '/static/Rocky.png'

"""Models for Pet Adoption"""

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column (db.Integer,
                    primary_key = True,
                    autoincrement = True)
    
    name = db.Column (db.Text,
                      nullable = False)
    
    species = db.Column (db.Text,
                         nullable = False)
    
    photo_url = db.Column (db.Text,
                           nullable = True, default=DEFAULT_IMAGE)
    
    age = db.Column (db.Integer,
                     nullable = True)
    
    notes = db.Column (db.Text,
                       nullable = True)
    
    available = db.Column (db.Boolean,
                          nullable = False,
                          default = True)
    
    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or DEFAULT_IMAGE

def connect_db(app):
    """Connect to app"""
    db.app = app
    db.init_app(app)