# example that aaron provided us
# creating a class called user  
class User(db.Model, SoftDeleteMixin):
    # The actual table name will be userinfo
    __tablename__ = 'userinfo'
    # Create a column named id that stores the integer primary key
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    station = Column(String(50))

#creating a volunteer class
class Volunteer(db.Model, SoftDeleteMixin):
    __tablename__ = "volunteers"
    id = Column(Integer, primary_key=True)
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))
    email = Column(String(50))
    station = Column(String(50))




