#importing Flask modules and budilding a web based application + Panda - Excel for Python 
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

#now I am writing the code for the endpoints which will let me to use API
app = Flask(__name__)
api = Api(app)

class Members(Resource):
    def get(self):
        data = pd.read_csv('members.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200
#the function just reads information from my file
#I defined a new class Members which describes some of the implementing methods 

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('full_name', required=True)
        parser.add_argument('ranking', required=False)
        parser.add_argument('gta_city', required=True)
        args = parser.parse_args()
    # the 2above fields are reqruired, , in this case, ranking is not compulsory 
    #the function creates a new member

        data = pd.read_csv('members.csv') 
        #I am using a Comma-separated values file call members of the tennis club 

        new_data = pd.DataFrame({
            'full_name'      : [args['full_name']],
            'ranking'       : [args['ranking']],
            'gta_city'      : [args['gta_city']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('members.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('full_name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('members.csv')

        data = data[data['full_name'] != args['full_name']]

        data.to_csv('members.csv', index=False)
        return {'message' : 'The details have been deleted properly. Please update the table if necessary'}, 200
#this function deletes members and additional details from the file


# Providing endpoint for my www - I am using the local host 
api.add_resource(Members, '/members')
#running the application on the web 
if __name__ == '__main__':
    app.run()