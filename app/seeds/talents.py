from app.models import db, talent, environment, SCHEMA
from sqlalchemy.sql import text

def seed_talents():
    airOfAuthority = talent(
        talent_name = 'Air of Authority',
        talent_desc = "You exude a natural aura of command, instilling subservience in all around you. On a successful command test, you may affect a number of targets equal to 1d10 times your fellowship bonus. Such is the authority in your voice that even those who are not in your service jump to attention when you speak. You may attempt to get non-servants to follow your commands by making a command test with a -10 penalty."
    )
    db.session.add(airOfAuthority)
    db.session.commit()

def undo_talents():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM talents"))

    db.session.commit()
