
def create_uri(db_info):
    ENGINE=db_info.get('ENGINE') or 'mysql'
    DRIVER=db_info.get('DRIVER') or 'pymysql'
    USER=db_info.get('USER') or 'root'
    PASSWORD=db_info.get('PASSWORD') or 'root'
    HOST=db_info.get('HOST') or 'localhost'
    PORT=db_info.get('PORT') or '3306'
    NAME=db_info.get('NAME') or 'test'
    return f"{ENGINE}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"


class Config:
    SECRET_KEY = "13124FDGFDGDFGDSfdsfsf"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'song',
        'PASSWORD':'123456',
        'HOST':'192.168.8.11',
        'PORT':'3306',
        'NAME':'flaskprojectDev'
    }
    SQLALCHEMY_DATABASE_URI=create_uri(DATABASE)


class TestingConfig(Config):

    TESTING = True

    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'song',
        'PASSWORD':'123456',
        'HOST':'192.168.8.11',
        'PORT':'3306',
        'NAME':'flaskprojectTest'
    }
    SQLALCHEMY_DATABASE_URI=create_uri(DATABASE)


class OnlineConfig(Config):
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'song',
        'PASSWORD':'123456',
        'HOST':'192.168.8.11',
        'PORT':'3306',
        'NAME':'flaskproject'
    }
    SQLALCHEMY_DATABASE_URI=create_uri(DATABASE)


envs={
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'online':OnlineConfig
}


