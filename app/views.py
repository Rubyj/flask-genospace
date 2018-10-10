from flask import jsonify, render_template, request
from app import app, db
from app.models import Drug_mechanism, Drug, Entity, Mechanism
from app.schemas import DrugSchema, EntitySchema, MechanismSchema

# Manages routing and return data to client

# Entity endpoint - return json entity list
@app.route('/entity')
def get_entities():
    key = request.args.get('key')
    if key is not None:
        entities = Entity.query.filter(Entity.name.like(key + "%")).all()
    else:
        entities = Entity.query.all()
    entity_schema = EntitySchema(many=True)
    result = entity_schema.dump(entities)
    return jsonify({"entities": result})


# Homepage - return template home.html
@app.route('/')
def get_home_page():
    return render_template('home.html')
