from flask_script import Manager
from coursebase import app, db, Professor

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    bambach = Professor(name='Mark Bambach', department='Marketing')
    sharma = Professor(name='Pratyush Sharma', department='Accounting & MIS')
    wang = Professor(name='Gang Wang', department='Accounting & MIS')
    db.session.add(bambach)
    db.session.add(sharma)
    db.session.add(wang)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
