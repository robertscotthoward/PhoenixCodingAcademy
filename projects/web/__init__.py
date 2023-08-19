import os

from flask import Flask, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
      return 'You want path: %s' % path


    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    def has_no_empty_params(rule):
      defaults = rule.defaults if rule.defaults is not None else ()
      arguments = rule.arguments if rule.arguments is not None else ()
      return len(defaults) >= len(arguments)


    @app.route("/map")
    def site_map():
        links = []
        for rule in app.url_map.iter_rules():
            # Filter out rules we can't navigate to in a browser
            # and rules that require parameters
            if "GET" in rule.methods and has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
        # links is now a list of url, endpoint tuples
        s = '\n'.join([f'<li>{x}</li>' for x in links])
        return f'''
         SITE MAP
          <ul>
          {s}
          </ul>
        '''

    return app