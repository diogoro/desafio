from flask import Flask, jsonify
from flask_restful import Api
from src.util import validations
from src.util.error_handler import ErrorHandler
from src.handler.finance import FinanceEvent, FinanceEventId


app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)


@app.errorhandler(ErrorHandler)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


api.add_resource(FinanceEvent, '/financeEvent')
api.add_resource(FinanceEventId, '/financeEvent/<cpf>')
