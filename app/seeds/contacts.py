from app.models import db, environment, SCHEMA
from app.models.user import User
from app.models.contact import Contact
from sqlalchemy.sql import text

def seed_contacts():
    demo_contact = Contact(
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
