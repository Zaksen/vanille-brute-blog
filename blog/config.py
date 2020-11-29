class Config:
    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '011be109bf92fcc908ffe726389a8c24'
    MAIL_USERNAME = "vanille.brute.blog@gmail.com"
    MAIL_PASSWORD = "QB3gFtB3mzPRFQ!"