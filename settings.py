

SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'peefer66'
DB_PASSWORD = '' # not required for cloud9
BLOG_DATABASE_NAME = 'sales_orders'
DB_HOST = '127.0.0.1'
DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False