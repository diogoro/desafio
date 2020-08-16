# import json
# import os
# from datetime import datetime, timedelta
#
# class EventosFinanceiros(object):
#     def __init__(self, ultima_consulta):
#         self.ultima_consulta = ultima_consulta
#
#
#
# eventosFinaceiros = EventosFinanceiros()
#
# from flask_restful import fields, marshal_with, Resource
#
# resource_fields = {
#     'task':   fields.String,
#     'uri':    fields.Url('todo_ep')
# }
#
# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#
#         # This field will not be sent in the response
#         self.status = 'active'
#
# class Todo(Resource):
#     @marshal_with(resource_fields)
#     def get(self, **kwargs):
#         return TodoDao(todo_id='my_todo', task='Remember the milk')