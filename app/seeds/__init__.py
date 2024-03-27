from flask.cli import AppGroup
from .users import seed_users, undo_users
from .character_sheets import seed_character_sheets, undo_character_sheets
from .contacts import seed_contacts, undo_contacts
from .talents import seed_talents, undo_talents

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo.
        # command, which will  truncate all tables prefixed with.
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below.
        undo_contacts()
        undo_character_sheets()
        undo_talents()
        undo_users()
    seed_users()
    seed_talents()
    seed_character_sheets()
    seed_contacts()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_contacts()
    undo_character_sheets()
    undo_talents()
    undo_users()
    # Add other undo functions here
