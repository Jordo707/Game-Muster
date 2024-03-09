from app.models import db, User, contact, environment, SCHEMA
from sqlalchemy.sql import text

def seed_contacts():
    demo_contact = contact(
        name="demo contact",
        description = "demo description",
        is_group = False,
        cost = 10,
        pc = 1
    )

    db.session.add(demo_contact)
    db.session.commit()

def undo_contacts():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text('DELETE FROM contacts'))

    db.session.commit()
