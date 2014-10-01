from flask import Flask, render_template
from oslo.config import cfg

# initialization
app = Flask(__name__)

conf = cfg.CONF

# register options
conf(project='poppy')
conf.register_opts([
    cfg.BoolOpt('debug', default=True),
    cfg.StrOpt('host', default='127.0.0.1'),
    cfg.IntOpt('port', default=3031)
])

app.config['poppy'] = conf

app.debug = app.config['poppy']['debug']


# controllers
@app.route("/")
def index():
    return render_template('index.html')


def run():
    """
        This function starts the application.
        This allows the user to run the application
        using /env/bin/journey.
    """
    app.run(
        host=app.config['poppy']['host'],
        port=app.config['poppy']['port']
    )


if __name__ == '__main__':
    run()
