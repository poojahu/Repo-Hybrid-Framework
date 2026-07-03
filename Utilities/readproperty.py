import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def get_url():
        return config.get("portal login",'url')

    @staticmethod
    def get_username():
        return config.get("portal login",'username')

    @staticmethod
    def get_password():
        return config.get("portal login",'password')

    @staticmethod
    def get_file():
        return config.get("portal login",'file')


    @staticmethod
    def get_sheetname():
        return config.get("portal login",'sheetname')


    @staticmethod
    def get_emp_firstname():
        return config.get("portal login",'empfirstname')

    @staticmethod
    def get_emp_lastname():
        return config.get("portal login",'emplastname')

    @staticmethod
    def get_emp_id():
        return config.get("portal login",'emp_id')

    @staticmethod
    def get_emp_user():
        return config.get("portal login",'emp_user')

    @staticmethod
    def get_emp_pass():
        return config.get("portal login",'emp_pass')