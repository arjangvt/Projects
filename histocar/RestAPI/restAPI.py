import sys
sys.path.insert(0, '../')

import logging
import json
from flask import Flask, request, render_template,Response
from flask import jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from Database.DBConn import DBConn
from Database.DBHelperRestAPI import DBHelperRestAPI
from datetime import date, datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/test')
def test():
    #result = {'carslist': 'test'}
    #result = [{"name":"John","age":"30","city":"New York"}]
    result = [{"id":"88682","employee_name":"pedramdivoone","employee_salary":"123","employee_age":"20","profile_image":""},
             {"id":"88683","employee_name":"iehknuy","employee_salary":"12352","employee_age":"25","profile_image":""},
             {"id":"88684","employee_name":"nzfai","employee_salary":"123","employee_age":"23","profile_image":""}]
    #print ("[" + json.dumps(result) + "]")
    return jsonify(result)

#https://damyanon.net/post/flask-series-logging/
@app.route('/')
def about():
    #app.logger.warning('Historide cars APIs')
    #app.logger.error('An error message is sent.')
    #app.logger.info('Information: 3 + 2 = %d', 5)
    app.logger.info('Historide cars APIs')
    return "about"

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return render_template('404.html'), 404

"""
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.html'), 500

"""
class CarBodyStyle(Resource):
    def get(self):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchCarBodyType() 
    
        #result = {'carslist': fields}
        return jsonify(fields)

class CarsDetail(Resource):
    def get(self, carid):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchCarDetail(carid) 
    
        #result = {'carslist': fields}
        return jsonify(fields)


class CarTrim(Resource):
    def get(self, model):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchCarTrim(model) 
        
        #result = {'carslist': fields}
        return jsonify(fields)

class MinMaxProductYear(Resource):
    def get(self, make, model, zipcode):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchMinMaxProductYear(make, model, zipcode) 
        
        #result = {'carslist': fields}
        return jsonify(fields)


class MinMaxPrice(Resource):
    def get(self, make, model, zipcode):
        
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchMinMaxPrice(make, model, zipcode) 

        #result = {'carslist': fields}
        return jsonify(fields)    

# This is the URL for the Hroku server
# http://127.0.0.1:5002/cars
# https://thawing-beach-68207.herokuapp.com/cars
class Cars(Resource):

    def get(self):
        
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchAllCarLists() 

        result = {'carslist': fields}
        return jsonify(result)
    
class CarsMakeModelZip(Resource):

    def get(self, make, model, zipcode):

        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchCarsMakeModelZip( make, model, zipcode)
        
        result = {'lists' : fields}
        return jsonify(result)

class CarMakes(Resource):

    def get(self):

        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchAllCarMakes()
        
        #result = {'lists' : fields}
        return jsonify(fields)

class CarModelMakes(Resource):

    def get(self, makeid):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchModelsMake(makeid)
        
        #result = {'lists' : fields}
        return jsonify(fields)

class RecentSearch(Resource):

    def get (self):
        _dbhelper = DBHelperRestAPI()
        fields = _dbhelper.FetchRecentSearches()

        result = {'lists' : fields}
        return jsonify(result)

#class CarsZip(Resource):

#    def get(self):
#        _dbhelper = DBHelperRestAPI()
#        fields = _dbhelper.FetchAllCarLists()
    
#        result = {'carslist': fields}
#        return jsonify(result)

###################### Inserting APIs ##############################

#class InsertMostRecent(Resource):

#    def get(self, makeid):
#        _dbhelper = DBHelperRestAPI()
#        fields = _dbhelper.FetchModelsMake(makeid)
        

#        return jsonify(fields)



# Query APIs
api.add_resource(Cars, '/cars') # Route_1
api.add_resource(CarsDetail, '/cars/<carid>')
api.add_resource(CarsMakeModelZip, '/cars/<make>/<model>/<zipcode>')
api.add_resource(CarMakes, '/carmakes')
api.add_resource(CarModelMakes, '/carmodelmakes/<makeid>')
api.add_resource(MinMaxPrice, '/carsprice/<make>/<model>/<zipcode>')
api.add_resource(MinMaxProductYear, '/carproductyear/<make>/<model>/<zipcode>')
api.add_resource(CarTrim, '/cartrim/<model>')
api.add_resource(CarBodyStyle,'/carbodystyle/')
 
api.add_resource(RecentSearch, '/recentsearches')

# Insert APIs


if __name__ == '__main__':
     app.run(port='5002', debug=True)

'''
Sample code
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
'''