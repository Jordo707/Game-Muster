from .db import db, environment, SCHEMA, add_prefix_for_prod

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(40), nullable=False, unique=True)
    game_master_id = db.Column(db.Inteber, nullable = False)

    def to_dict(self):
        return {
            'id': self.id,
            'campaignName': self.campaign_name,
            'gameMasterId': self.game_master_id
        }
