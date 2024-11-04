from datetime import datetime

from ..extensions import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ind_or_group = db.Column(db.String(250))
    AnimalSpecies = db.Column(db.String(250))
    AnimalBreed = db.Column(db.String(250))
    AnimalColour = db.Column(db.String(250))
    AnimalGender = db.Column(db.String(250))
    Measure = db.Column(db.Integer)
    ComplexDate = db.Column(db.DateTime, default=datetime.utcnow)
    AnimalKeepingLocation = db.Column(db.String(250))
