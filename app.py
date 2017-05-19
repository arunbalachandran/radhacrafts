from waitress import serve
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def show_index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run()
    serve(app, port=os.environ.get('PORT', 8000), cleanup_interval=100)
