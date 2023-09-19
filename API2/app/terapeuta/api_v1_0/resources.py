from flask import request, Blueprint
from flask_restful import Api, Resource

# Importar los modelos Paciente, Doctor, Enfermero, Camillero y Usuario
#from .models import Paciente, Doctor, Enfermero, Camillero, Usuario
#from .schemas import HumedadSchema, TemperaturaSchema
#from ..models import Humedad, Temperatura, Usuario

from .schemas import TerapeutaSchema
from ..models import Terapeuta

terapeuta_v1_0_bp = Blueprint('terapeuta_v1_0_bp', __name__)
api = Api(terapeuta_v1_0_bp)

#humedad_schema = HumedadSchema()
#temperatura_schema = TemperaturaSchema()

terapeuta_schema = TerapeutaSchema()
terapeuta_schema = TerapeutaSchema(many=True)
class TerapeutaListResource(Resource):
    def get(self):
        terapeutas = Terapeuta.query.all()
        result = terapeuta_schema.dump(terapeutas)
        return result

    def post(self):
        data = request.get_json()
        terapeuta_dict = terapeuta_schema.load(data)
        terapeuta = Terapeuta(**terapeuta_dict)
        terapeuta.save()
        resp = terapeuta_schema.dump(terapeuta)
        return resp, 201

class TerapeutaResource(Resource):
    def get(self, terapeuta_id):
        terapeuta = Terapeuta.query.get(terapeuta_id)
        if terapeuta is None:
            raise ObjectNotFound('El terapeuta no existe')
        resp = terapeuta_schema.dump(terapeuta)
        return resp

    def put(self, terapeuta_id):
        terapeuta = Terapeuta.query.get(terapeuta_id)
        data = request.get_json()
        terapeuta_dict = terapeuta_schema.load(data)
        for key, value in terapeuta_dict.items():
            setattr(terapeuta, key, value)
        terapeuta.save()
        resp = terapeuta_schema.dump(terapeuta)
        return resp, 200

    # def delete(self, terapeuta_id):
    #     terapeuta = Terapeuta.get_by_id(terapeuta_id)
    #     terapeuta.delete()
    #     return "", 204

    # Borrado Lógico
    def delete(self, terapeuta_id):
        terapeuta = Terapeuta.get_by_id(terapeuta_id)
        terapeuta.estado = 'Inactivo'
        terapeuta.save()
        resp = terapeuta_schema.dump(terapeuta)
        return resp, 200

class GerenteListResource(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

class GerenteResource(Resource):
    def get(self, temperatura_id):
        pass
    
    def put(self, temperatura_id):
        pass

    def delete(self, temperatura_id):
        pass

#api.add_resource(HumedadListResource, '/api/v1.0/humedad/', endpoint='humedad_list_resource')
#api.add_resource(HumedadResource, '/api/v1.0/humedad/<int:humedad_id>', endpoint='humedad_resource')
#api.add_resource(TemperaturaListResource, '/api/v1.0/temperatura/', endpoint='temperatura_list_resource')
#api.add_resource(TemperaturaResource, '/api/v1.0/temperatura/<int:temperatura_id>', endpoint='temperatura_resource')
api.add_resource(TerapeutaListResource, '/api/v1.0/terapeuta/', endpoint='terapeuta_list_resource')
api.add_resource(TerapeutaResource, '/api/v1.0/terapeuta/<int:terapeuta_id>', endpoint='terapeuta_resource')