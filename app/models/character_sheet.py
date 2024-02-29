from .db import db, environment, SCHEMA, add_prefix_for_prod

class CharacterSheet(db.Model):
    __tablename__ = 'character_sheets'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    stat_sheet_id = db.Column(db.Integer)
    xp_max = db.Column(db.Integer, nullable = False)
    xp_spent = db.Column(db.Integer, nullable = False)

    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'stat_sheet_id': self.stat_sheet_id,
            'xp_max': self.xp_max,
            'xp_spent': self.xp_spent
        }
