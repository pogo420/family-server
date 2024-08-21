
from flask import Blueprint, jsonify, current_app
from server_rest_api.models.responses import AppInfo

generic_bp = Blueprint("generic_bp", __name__)

@generic_bp.route("/")
def get_app_info() -> AppInfo:
    """Route for handling rest server information for clients"""
    # getting the global config
    app_name = current_app.config.get('APP_NAME')
    app_version = current_app.config.get('APP_VERSION')
    
    # generating response
    app_info = AppInfo(app_name, app_version)
    
    # returning response
    return jsonify(app_info.__dict__()), 200

