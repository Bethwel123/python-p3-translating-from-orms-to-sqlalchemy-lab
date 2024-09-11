from models import Dog

def create_table(base, engine):
    return base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    all_dogs = session.query(Dog).all()
    return all_dogs

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()
    return query


def find_by_id(session, id):
    get_by_id = session.get(Dog, id)
    return get_by_id

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return query

def update_breed(session, dog, breed):
    updated = session.query(Dog).update({
        Dog.breed: breed
    })
    return updated