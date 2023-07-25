

from dbconn import ApiDb, appConn
from sqlalchemy import Column, Integer, Float, String,text
class AppProduct(ApiDb):

    __tablename__ = "appproducts"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer,primary_key=True)
    name = Column(String(200),unique=True)
    price = Column(Float)
    description = Column(String(300))

    def save(self) ->int:
        # db = getDatabase()
        # print(db.ACTIVE)
        appConn.add(self)
        appConn.commit()

        return self.id
        

    def getById(self, id):
       result = appConn.query(AppProduct).filter(AppProduct.id == id).first()

       if hasattr(result, 'name'):
           return {'name':result.name, 'description':result.description, 'price':result.price, 'id':result.id}
       
       return None
    
    def search(self, name): 
    #    sql = text("select * from appproducts where name like '%:pn%'").params(pn=name)
    #    result = appConn.query(AppProduct).from_statement(sql).all()

       ### USE PREPARED STATEMENT HERE, BAD PRACTICE ON MY SIDE
       result = appConn.query(AppProduct).from_statement(
            text(f"""SELECT * FROM appproducts where name like '%{name}%'""")
        ).all()
       if len(result) > 0:
           return [{'name':data.name, 'description':data.description, 'price':data.price, 'id':data.id} for data in result]
       
       return None
    
    def getAll(self):
       result = appConn.query(AppProduct).all()

       if len(result) > 0:
           return [{'name':data.name, 'description':data.description, 'price':data.price, 'id':data.id} for data in result]
       
       return None
       