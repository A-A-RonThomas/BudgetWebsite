from flask import Flask, current_app
from flask_cors import CORS
from flask_migrate import Migrate
from services.config import Config, db
from services.routes import *
from services.models import *
from services.controllers import *

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

account_controller = AccountController()
# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()
    account_controller.populate_accounts()
    BACKEND_HOST = current_app.config['BACKEND_HOST']
    BACKEND_PORT = current_app.config['BACKEND_PORT']

# Register blueprints
app.register_blueprint(transaction_bp, url_prefix='/transaction')
app.register_blueprint(account_bp, url_prefix='/account')
app.register_blueprint(fun_bp, url_prefix='/fun')
app.register_blueprint(budget_bp, prefix='/budget')

if __name__ == '__main__':
    app.run(host=BACKEND_HOST, port=BACKEND_PORT, debug=True, use_reloader=True)