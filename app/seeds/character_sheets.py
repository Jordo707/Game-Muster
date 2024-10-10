from app.models import db, environment, SCHEMA
from app.models.character_sheet import CharacterSheet
from sqlalchemy.sql import text

def seed_character_sheets():
    sample = CharacterSheet(
        player_id = 1,
        stat_sheet_id = 1,
        xp_max = 500,
        xp_spent = 0
    )
    db.session.add(sample)
    db.session.commit()

def undo_character_sheets():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_sheets"))

    db.session.commit()
