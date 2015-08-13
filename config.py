import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Flask Application Key (optional)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # File Upload Setting
    UPLOAD_FOLDER = 'app/static/uploaded_sudokus'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'PNG', 'JPG'])

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Add settings for development here.
    DEBUG = True


class ProductionConfig(Config):
    # Add settings for production here.
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
