import datetime

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
