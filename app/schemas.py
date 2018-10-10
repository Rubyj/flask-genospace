from app import ma
from app.models import Drug, Mechanism, Drug_mechanism, Entity

# Marshmallow schemas used to JSON serialize models 

class DrugSchema(ma.ModelSchema):
    class Meta:
        model = Drug

class MechanismSchema(ma.ModelSchema):
    class Meta:
        model = Mechanism

class DrugMechanismSchema(ma.ModelSchema):
    class Meta:
        model = Drug_mechanism

class EntitySchema(ma.ModelSchema):
    class Meta:
        model = Entity
