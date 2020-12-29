"""
__init__.py
- this file will contain the application factory ( inside which Flask instance will be created)
- this file tells python that "flaskblog" directory should be treated as a package
"""
import os
from flask import Flask


def create_app(test_config=None):
    """
    create_app is the application factory function.
    :param test_config: 테스트용 configuration 파일
    :return: Flask instance
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskblog.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    return app
