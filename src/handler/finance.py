import json
from flask_restful import Resource, request
from src.util import validations
from src.util.error_handler import ErrorHandler
from src.services.redis import save, get, delete


class FinanceEventId(Resource):
    def get(self, cpf):
        if cpf and validations.validate_cpf(cpf):
            try:
                objet = get(cpf)
                if objet:
                    print(objet)
                    resp = json.loads(objet)
                    return resp
                else:
                    return '', 404
            except Exception as e:
                raise ErrorHandler(e.args)
        else:
            raise ErrorHandler(message="CPF isn't valid", status_code=400)

    def delete(self, cpf):
        if cpf and validations.validate_cpf(cpf):
            try:
                delete(cpf)
            except Exception as e:
                raise ErrorHandler(message="Not found", status_code=404)
            return '', 204
        else:
            raise ErrorHandler(message="CPF isn't valid", status_code=400)

    def put(self, cpf):
        if cpf and validations.validate_cpf(cpf):
            if not get(cpf):
                raise ErrorHandler(message="Not found", status_code=404)
            try:
                param = request.get_json()
                validations.validate_event_put(param)
                event = param.get('event')
                json_str = json.dumps(event)
                save(cpf, json_str)
            except Exception as e:
                raise ErrorHandler(e.args)
        else:
            raise ErrorHandler(message="CPF isn't valid", status_code=400)

        return '', 201


class FinanceEvent(Resource):

    def post(self):
        try:
            param = request.get_json()
            validations.validate_json(param)
            cpf = param.get('cpf')
            event = param.get('event')
            json_str = json.dumps(event)
            save(cpf, json_str)
        except Exception as e:
            raise ErrorHandler(e.args)
        # cadastrar eventos para um cpf
        return '', 201