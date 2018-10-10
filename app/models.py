from app import db

# All the models which map to existing database tables and columns of the same name
# Define relationships using foreign keys and relationships

class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_name = db.Column(db.String)

    def __init__(self, main_name):
        self.main_name = main_name


class Mechanism(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name


class Drug_mechanism(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey("drug.id"))
    drug = db.relationship(Drug, primaryjoin=drug_id == Drug.id, backref="drug_mechanism")
    mechanism_id = db.Column(db.Integer, db.ForeignKey("mechanism.id"))
    mechanism = db.relationship(Mechanism, primaryjoin=mechanism_id == Mechanism.id, backref="drug_mechanism")


class Entity_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String)

    def __init__(self, type_name):
        self.type_name = type_name


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("entity_type.id"))
    entity_type = db.relationship(Entity_type, primaryjoin=type_id == Entity_type.id, backref="entity")
    entity_id = db.Column(db.Integer)
    name = db.Column(db.String)

    def __init__(self, type_id, entity_type, entity_id, name):
        self.type_id = type_id
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.name = name
