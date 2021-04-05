from pony.orm import *

db = Database()




class User(db.Entity):
    name = Required(str)
    password = Required(str)




@db_session
def add_user(name, password):
    User(name=name, password=password)

@db_session
def find_user_password_by_name(name):
    u = User.get(name=name)
    return u.password


