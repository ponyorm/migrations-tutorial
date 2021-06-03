from pony.orm.migrations.operations import AddEntity
from pony.orm.migrations.virtuals import Required, VirtualEntity as Entity, PrimaryKey

dependencies = []

operations = [
    AddEntity(Entity('Student',  attrs=[
        PrimaryKey('id', int, auto=True), 
        Required('full_name', str), 
        Required('age', int)]))
]
