# encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from labmanager import app
from exts import db
from models import Testline,Module


manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)


if __name__=="__main__":
    manager.run()