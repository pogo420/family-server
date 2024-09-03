from flask_swagger_ui import get_swaggerui_blueprint

API_DOCS_URL = '/docs'
DOCS_LOCATION = '/static/swagger.yaml'

# swagger ui configs 
# check this link: https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/configuration.md for list of other configs
swagger_config = {
    "tryItOutEnabled": False, # disables try it out feature
    "supportedSubmitMethods": [] # disables try it out feature
}

# swagger blueprint object
api_docs_bp = get_swaggerui_blueprint(
    API_DOCS_URL,
    DOCS_LOCATION,
    config=swagger_config
)
