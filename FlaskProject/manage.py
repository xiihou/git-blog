from flask_script import Manager
from App import create_app
from flask_migrate import MigrateCommand

app=create_app()

manger=Manager(app)
manger.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manger.run()