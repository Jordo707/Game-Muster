from .db import db, environment, SCHEMA, add_prefix_for_prod

class Statsheet(db.Model):
    __tablename__ = 'statsheets'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    weapon_skill = db.Column(db.Integer, nullable=False)
    ballistic_skill = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    toughness = db.Column(db.Integer, nullable=False)
    agility = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    perception = db.Column(db.Integer, nullable=False)
    willpower = db.Column(db.Integer, nullable=False)
    fellowship = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id':self.id,
            'weapon_skill':self.weapon_skill,
            'ballistic_skill':self.ballistic_skill,
            'strength':self.strength,
            'toughness':self.toughness,
            'agility':self.agility,
            'intelligence':self.intelligence,
            'perception':self.perception,
            'willpower':self.willpower,
            'fellowship':self.fellowship
        }
