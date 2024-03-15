from .db import db, environment, SCHEMA, add_prefix_for_prod

class Session(db.Model):
    __tablename__ = 'sessions'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String)

    def to_dict(self):
        return {
            'id':self.id,
            'campaign_id':self.campaign_id,
            'date':self.date,
            'notes':self.notes
        }
