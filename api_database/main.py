


from dbconn import ApiDb, engine
from flask import Flask, request, jsonify, make_response
import json
from dtos import AppProductDto
from models import AppProduct
app = Flask(__name__)

ApiDb.metadata.create_all(bind=engine)
# session = getDatabase()

@app.route('/api/products', methods=['POST'])
def create_todo():
   data = request.get_json()
   print(type(data), data)
#    python_obj = json.loads(data)
#    dto = AppProductDto()
#    pdtDto  = dto.load(data, session=session)

   product = AppProduct()
   product.name  = data['name']
   product.description  = data['description']
   product.price  = data['price']
   
   id = product.save()
#    result = todo_schema.dump(todo.create())
   return make_response(jsonify({"id": id}), 200)

@app.route('/api/products/all', methods=['GET'])
def getAll():
    product = AppProduct()
    data = product.getAll()
    print('getAll')
    if data == None:
        return make_response({'errorCode':'EO01', 'errorDesc':'NOT FOUND'}, 404)

    return make_response(jsonify(data), 200)

@app.route('/api/products/<id>', methods=['GET'])
def getProductById(id):
    product = AppProduct()
    data = product.getById(id)
    
    if data == None:
        return make_response({'errorCode':'EO01', 'errorDesc':'NOT FOUND'}, 404)

    return make_response(jsonify(data), 200)


@app.route('/api/products/search/<name>', methods=['GET'])
def getProductByName(name):
    product = AppProduct()
    data = product.search(name)
    
    if data == None:
        return make_response({'errorCode':'EO01', 'errorDesc':'NOT FOUND'}, 404)

    return make_response(jsonify(data), 200)

if __name__ == '__main__':
   app.run(debug=True,port=4040)