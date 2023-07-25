# from flask import Flask,render_template,redirect,request,jsonify,current_app,g
# from flask_marshmallow import Marshmallow
# from sqlalchemy import text, Column, String, Float, Integer
# from flask_sqlalchemy import SQLAlchemy
# from dbconn import engine, ApiDb
# from sqlalchemy import text
# from flask_restful import Resource, Api, abort,reqparse
# from dbconn import db

# app = Flask(__name__)

# ApiDb.metadata.create_all(bind=engine)

# with app.app_context():  #  code that needs the application context here

#     #create product model
#     class Product(ApiDb):

#         id = Column(Integer,primary_key=True)
#         name = Column(String(200),unique=True)
#         price = Column(Float)
#         description = Column(String(300))

#         def __init__(self, name,price,description):
#             self.id = id
#             self.name = name
#             self.price = price
#             self.description = description

#             def __rep__(self):
#                 return f"Product(name={self.name},description={self.description},price={self.price})"

#  # Define a Flask route for serving an HTML page
# @app.route('/')
# def index():
#     productList = []
#     conn = engine.connect()
#     result = conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
#     for row in result.fetchall():
#         productList.append({"id" :row[0], "name" :row[1],"price" :row[2],"description" :row[3]})

#         return render_template('index.html',productList = productList)
    
#     class Square(Resource):
#         def get(self, num):
#             return jsonify({'square': num**2})
        
#         # Create Flask-RESTful resource to interact with your database
#         @app.route('/products')
        
#         def productIndex():
#             productList = []
#             conn = engine.connect()
#             result= conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
#             for row in result.fetchall():
#                 productList.append({"id": row[0], "name": row[1], "price": row[2], "description": row[3]})
#                 return render_template('index.html', productList = productList)
            
#             class ProductResource(Resource):
#                 #Get a product by ID

#                 def get(self):
#                     conn =  engine.connect()
#                     result = conn.execute(text("SELECT * FROM dbo.ProductApiTable"))
#                     return jsonify(result)
                
#                  # Create a new product
#                 def post(self):
#                     data = request.form.to_dict()
#                     name = data["name"]
#                     price = data["price"]
#                     description = data["descrition"]

#                     conn = engine.connect()

#                     stmt = text('INSERT INTO dbo.ProductApiTable (name, price, description) VALUES (:name, :price, :description)')
#                     insert = conn.execute(stmt,{'name': name, 'price': price, 'description': description})

#                     conn.commit()
#                     response_data = {'message': 'Data received and stored successfully'}

#                     return response_data,201
                
#                 #update an existin product
#                 def put(self, product_id):
#                     parser = reqparse.RequestParser()
#                     parser.add_argument('name', type=str)
#                     parser.add_argument('description', type=str)
#                     parser.add_argument('price', type=float)
#                     args = parser.parse_args()

#                     product = Product.query.filter_by(id=product_id).first()
#                     if product is None:
#                         abort(404, message="Product not found")

#                         if args['name']:
#                             product.name = args['name']
#                             if args['description']:
#                                 product.description = args['description']
#                             if args['price']:
#                                 product.price = args['price']

#                                 ApiDb.session.commit()
#                                 return{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'message': 'product updated'}
                            
#                             #delete a product
#                             def delete(self,product_id):
#                                 product = Product.query.filter_by(id=product_id).first()
#                                 if product is None:
#                                     abort(404, message="Product not found")
#                                     ApiDb.session.delete(product)
#                                     ApiDb.session.commit()

#                                     return {'message': 'Product deleted successfully.'}
                                
#                                 #add te resource to API
#                                 api= Api(app)
#                                 api.add_resource(ProductResource,'/products')
#                                 api.add_resource(Square, '/square/<int:num>')  

#                                 #product Schema
#                                 class appSchema(ApiMa.Schema):
#                                     class Meta:
#                                         fields =('id', 'name', 'price', 'description')

#                                         #initliase Schema
#                                     product_Schema = appSchema()
#                                     app_Schema = appSchema(many=True)

#                                     #Creation of the database tables within the application context.
#                                     with app.app_context():
#                                         ApiDb.create_all()
#                                         app.run(debug=True)

# if __name__ == '__main__': 
#    app.run()
