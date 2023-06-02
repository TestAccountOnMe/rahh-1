from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=["POST"])
def sub():
  aa = request.form.get("idk")
  with open('resp.txt', 'a') as f:
    f.write(aa + '\n')
  return "Done, you can submit more now."




app.run(host='0.0.0.0', port=81)
