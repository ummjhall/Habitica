from .db import db, environment, SCHEMA, add_prefix_for_prod


class Reward(db.Model):
    __tablename__ = 'rewards'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    type = db.Column(db.Enum('custom', 'item', name='types'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    cost = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='rewards')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'cost': self.cost
        }
