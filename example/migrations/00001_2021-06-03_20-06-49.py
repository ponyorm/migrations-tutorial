from pony.orm.migrations.operations import AddEntity
from pony.orm.migrations.virtuals import Required, Set, VirtualEntity as Entity, PrimaryKey

dependencies = [
    '00000_initial'
]

operations = [
    AddEntity(Entity('Group',  attrs=[
        PrimaryKey('id', int, auto=True), 
        Required('name', str), 
        Set('students', 'Student', reverse=Required('group', 'Group'))]))
]
