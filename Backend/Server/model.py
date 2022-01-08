from Server import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(20),nullable=False)
    review = db.Column(db.String(20),nullable=False)