from .db import db, environment, SCHEMA, add_prefix_for_prod

class Contact(db.Model):
    __tablename__ = 'contacts'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    is_group = db.Column(db.Boolean)
    cost = db.Column(db.Integer)
    pc = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'is_group':self.is_group,
            'cost':self.cost,
            'pc':self.pc
        }
