from flask_swagger_ui import get_swaggerui_blueprint

API_DOCS_URL = '/docs'
DOCS_LOCATION = '/static/swagger.yaml'

# swagger blueprint object
api_docs_bp = get_swaggerui_blueprint(
    API_DOCS_URL,
    DOCS_LOCATION
)
