from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os

from config import Config
from routes import configure_routes

app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import *  # This import is placed here to avoid circular imports

# Configure routes
configure_routes(app)

# Custom error handlers can be added here
@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500

if __name__ == "__main__":
    # Determine port and host dynamically based on environment
    port = int(os.environ.get('PORT', 5000))
    # Run the application on all available interfaces
    app.run(host='0.0.0.0', port=port, debug=True)

