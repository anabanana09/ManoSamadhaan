import os

class Config:
    # Core settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///mydb.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode
    DEBUG = False

    # Server settings
    SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost:5000')

    # Security settings
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'my_precious_two')

    # Session settings
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'my_app_session')
    PERMANENT_SESSION_LIFETIME = 3600  # 1 Hour

    # Email settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

    # Logging settings
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT', '1').lower() in ['true', 'on', '1']

    # Admin settings
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev_mydb.sqlite')
    SQLALCHEMY_ECHO = True  # Output SQL statements to the log for debugging

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'sqlite:///test_mydb.sqlite')
    SERVER_NAME = 'localhost:5000'
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the forms

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/prod_db')
    SERVER_NAME = 'myapp.com'

# How to use configurations in the Flask app
# app.config.from_object('config.DevelopmentConfig')  # Use development settings
# app.config.from_object('config.ProductionConfig')  # Use production settings

