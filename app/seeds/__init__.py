from flask.cli import AppGroup
from app.models.db import db, environment, SCHEMA
from .users import seed_users, undo_users
from .avatars import seed_avatars, undo_avatars
from .tasks import seed_tasks, undo_tasks
from .rewards import seed_rewards, undo_rewards
from .equipment import seed_equipment, undo_equipment
from .avatars_equipment import seed_avatars_equipment, undo_avatars_equipment
from .images import seed_images, undo_images


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other models' undo functions below
        undo_images()
        undo_avatars_equipment()
        undo_equipment()
        undo_rewards()
        undo_tasks()
        undo_avatars()
        undo_users()

    seed_users()
    seed_avatars()
    seed_tasks()
    seed_rewards()
    seed_equipment()
    seed_avatars_equipment()
    seed_images()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_images()
    undo_avatars_equipment()
    undo_equipment()
    undo_rewards()
    undo_tasks()
    undo_avatars()
    undo_users()
