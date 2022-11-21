from flask import Flask, render_template, request
from turkey_math import do_turkey_math

app = Flask(__name__)


@app.route('/form')
def form():
  return render_template('./form.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
  if request.method == 'GET':
    return f"The URL /data is accessed directly. Try going to '/form' to submit form"
  if request.method == 'POST':
    form_data = request.form
    output = do_turkey_math(**form_data)
    if not output:
      return render_template('invalid_data.html')
    return render_template('data.html', form_data=output)


app.run(host='localhost', port=5000)
