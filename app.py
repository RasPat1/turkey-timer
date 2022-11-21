from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

from turkey_math import do_turkey_math

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()


@app.route('/')
def form():
  return render_template('./index.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
  if request.method == 'GET':
    return f"The URL /data is accessed directly. Try going to '/' to submit form"
  if request.method == 'POST':
    form_data = request.form
    output = do_turkey_math(**form_data)
    if not output:
      return render_template('invalid_data.html')
    return render_template('data.html', form_data=output)
