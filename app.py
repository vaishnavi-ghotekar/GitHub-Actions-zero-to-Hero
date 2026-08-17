from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'


if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '0.0.0.0')  # nosec B104
    port = int(os.environ.get('FLASK_PORT', '80'))
    app.run(debug=debug_mode, host=host, port=port)
