import datetime
import pandas as pd


class FilesHandler:
    content_type: str
    filename: str
    mime_type: str
    new_name: str

    def __init__(self, file):
        self.current_file = None
        self.content_type = file.content_type
        self.filename = file.filename
        self.mime_type = self.filename.rsplit('.', 1)[1].lower()
        self.timestamp = str(datetime.datetime.now().timestamp())
        self.new_name = self.give_that_file_a_name()

    valid_sheet_types = ['csv', 'xlsx', 'xls']
    valid_doc_types = ['doc', 'docx', 'txt']
    valid_image_types = ['png', 'jpg', 'jpeg', 'gif']

    def check_file_extension_is_valid(self, valid_types=None) -> bool:
        if valid_types is None:
            valid_types = self.valid_sheet_types
        return '.' in self.filename and \
               self.mime_type in valid_types

    def give_that_file_a_name(self) -> str:
        new_name = '{0}{1}'.format(self.timestamp, str(self.filename))
        return new_name

    def read_file(self, current_file):
        print(self.mime_type)
        if self.mime_type == 'csv':
            return pd.read_csv(current_file)
        else:
            return pd.read_excel(current_file)
