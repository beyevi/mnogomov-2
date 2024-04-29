from app import db

class EnglishToFrenchDictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String(80), unique=True, nullable=False)
    english_word_ipa = db.Column(db.String(80), unique=True, nullable=False)
    french_word = db.Column(db.String(80), unique=True, nullable=False)


class FrenchToEnglishDictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    french_word = db.Column(db.String(80), unique=True, nullable=False)
    french_word_ipa = db.Column(db.String(80), unique=True, nullable=False)
    english_word = db.Column(db.String(80), unique=True, nullable=False)
