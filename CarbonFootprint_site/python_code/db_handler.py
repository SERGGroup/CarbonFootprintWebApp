from .form_definition_class import MainFormClass
from .support.constants import DATABASE_DIR, os
from flask_sqlalchemy import SQLAlchemy


class DatabaseHandler:

    def __init__(self, app):

        self.__init_databases(app)

    def __init_databases(self, app):

        self.app = app

        db_path = os.path.join(DATABASE_DIR, 'main_database.db')
        db_uri = 'sqlite:///{}'.format(db_path)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_BINDS'] = {

            'input_provided': 'sqlite:///{}'.format(os.path.join(DATABASE_DIR, 'input_provided.db'))

        }

        self.db = SQLAlchemy(app)

        self.form_class = MainFormClass()
        self.db_model = self.form_class.init_db_class(self.db, 'input_provided')

        with app.app_context():
            self.db.create_all()

    def append_to_db(self, form_class):

        db_entry = form_class.append_db_entry_to(self.db_model())

        try:

            self.db.session.add(db_entry)
            self.db.session.commit()

        except:

            pass

        return db_entry

    def clear_db(self):

        try:
            self.db.session.query(self.db_model).delete()
            self.db.session.commit()
            return True

        except:

            return False
