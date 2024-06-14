from app.models import db, environment, SCHEMA
from app.models.talent import Talent
from sqlalchemy.sql import text

def seed_talents():
    try:
        airOfAuthority = Talent(
            talent_name='Air of Authority',
            talent_desc="You exude a natural aura of command, ..."
        )
        db.session.add(airOfAuthority)
        db.session.commit()
    except Exception as e:
        print('-------------------------------------------------------')
        print(f"Error seeding talents: {e}")
        print('-------------------------------------------------------')
        db.session.rollback()

def undo_talents():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM talents"))

    db.session.commit()
