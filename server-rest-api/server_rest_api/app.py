# Flask rest server entry point 

from flask import Flask
from os import environ
from dotenv import load_dotenv
from server_rest_api.config import configs
from server_rest_api.generic.generic import generic_bp
from server_rest_api.open_api_spec.open_api_spec import api_docs_bp

# App initializing
app = Flask(__name__)

# Loading environment variables from .env file
load_dotenv()

# Setting application config
config_type = environ.get("CONFIG_TYPE", "default")
app.config.from_object(configs.get(config_type))

# Registering blueprints 
app.register_blueprint(generic_bp)
app.register_blueprint(api_docs_bp)

if __name__ == "__main__":
    app.run()
