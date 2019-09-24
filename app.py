from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import urllib
import pandas as pd
import datetime
from pymongo import MongoClient

pwd = urllib.parse.quote('MeetTeam@18')
connection_string = 'mongodb+srv://dev1:dev123@cluster0-5zaen.mongodb.net/prod-app?retryWrites=true&w=majority'
database = 'beta'
app = Flask(__name__)
app.config['MONGO_DBNAME'] = database
app.config['MONGO_URI'] = connection_string

mongo = PyMongo(app)
client = MongoClient(connection_string)
db = client[database]

rights = {
    'CanManageStudent': False,
    'CanViewStudent': False,
    '''       Class Rules'''
    'CanManageClass': False,

    '''       User Rules'''
    'CanModifyUsers': False,
    '''       Communication Rules'''
    'CanSeeUserMessage': False,
    'CanReceiveAdminMessages': False,
    'CanSendMessage': False,
    'CanCreateEvents': False,
    'CanViewReadReport': False,

    '''      Fees Rules'''
    'CanManageFee': False,

    '''      Attendance Rules'''
    'CanManageAttendance': False,
}

'''class for the model'''


class UserModel:
    def __init__(self, name, mob, email, school_id):
        self.Name = name
        self.CreatedAt = datetime.datetime.utcnow()
        self.UpdatedAt = datetime.datetime.utcnow()
        self.DeletedAt = ''
        self.DOB = ''
        self.Password = ''
        self.ActiveState = True
        self.MobileNumber = mob
        self.Email = email
        self.Role = [1]
        self.Rights = rights
        self.EmailVerified = False
        self.SpouceDOB = ''
        self.SpouceName = ''
        self.SchoolId = school_id
        self.UTCTimeOffSet = 0
        self.Country = ''
        self.Designation = ''
        self.CountryCode = ''


@app.route('/start', methods=['GET'])
def start():
    user = mongo.db.users
    email = request.json['Email']
    users = user.find_one({'Email': email})
    return jsonify(users['Gender'])


@app.route('/upload', methods=['POST'])
def upload():
    return 'uploaded successfully'


@app.route('/images', methods=['GET'])
def get_image():
    return 'image'


@app.route('/bulk/register', methods=['POST'])
def Bulk_Register():
    application_user = db.application_user
    if 'userFile' in request.files:
        file = request.files['userFile']
        df = pd.read_csv(file)
        to_add = []
        for row in df.iterrows():
            user = UserModel(row[1][1], row[1][2], row[1][4], '123')
            user_in_json = user.__dict__
            to_add.append(user_in_json)
        result = application_user.insert_many(to_add)
        return str(result.inserted_ids)
    else:
        return 'failed'


if __name__ == '__main__':
    app.run(debug=True)
