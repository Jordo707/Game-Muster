from .db import db, environment, SCHEMA, add_prefix_for_prod

class Talent(db.Model):
    __tablename__ = 'talents'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    talent_name = db.Column(db.String, nullable=False, unique=True)
    talent_desc = db.Column(db.String, nullable=False, unique=True)

    def to_dict(self):
        return {
            'id':self.id,
            'talent_name':self.talent_name,
            'talent_desc':self.talent_desc
        }
