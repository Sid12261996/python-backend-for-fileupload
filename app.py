from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient

import models.UserModel as UserModel
from FilesHandler import FilesHandler as Fh

# pwd = urllib.parse.quote('MeetTeam@18')
database = 'beta-app'
connection_string = 'mongodb+srv://dev1:dev123@cluster0-5zaen.mongodb.net/' + database + '?retryWrites=true&w=majority'

app = Flask(__name__)
app.config['MONGO_DBNAME'] = database
app.config['MONGO_URI'] = connection_string

mongo = PyMongo(app)
client = MongoClient(connection_string)
db = client[database]


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No files been uploaded'
    file = request.files['file']
    current_file = Fh(file)
    if current_file.check_file_extension_is_valid(['jpeg', 'png', 'jpg']):
        filename = current_file.new_name
        mongo.save_file(filename, file)
        return 'uploaded successfully file name: ' + filename
    else:
        return 'File extension should be .jpg or .png or .jpeg current type is ' + str(
            current_file.mime_type)


@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    return mongo.send_file(filename)


@app.route('/bulk/register', methods=['POST'])
def bulk_register():
    application_user = db.application_user
    if 'userFile' in request.files:
        file = request.files['userFile']
        currentFile = Fh(file)
        isFileValid = currentFile.check_file_extension_is_valid()
        if isFileValid:
            df = currentFile.read_file(file)
            to_add = []
            for row in df.iterrows():
                user = UserModel.UserModel(row[1][1], row[1][2], row[1][4], '123')
                user_in_json = user.__dict__
                to_add.append(user_in_json)
            result = application_user.insert_many(to_add)
            return 'Inserted Ids: ' + str(result.inserted_ids)
        else:
            return 'File extension should be .csv or .xls or .xlsx current type is ' + str(
                currentFile.mime_type)
    else:
        return 'failed! No files got uploaded'


if __name__ == '__main__':
    app.run(debug=True)
