import os
from flask import Flask

#A creating the application factory function
def create_app(config_file='config.py'):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) # __name__ is current python module, instanc_relative_config=True configuration files are relative to the instance folder
    
    # set up the configurations that the app will use
    app.config.from_pyfile(config_file)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import db
    db.init_app(app)

    from . import dashboardapi
    app.register_blueprint(dashboardapi.bp)
    app.add_url_rule('/', endpoint='index')

    return app