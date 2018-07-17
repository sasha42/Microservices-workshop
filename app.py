from flask import Flask
import requests

app = Flask(__name__)

def get_yes_or_no():
  resp = requests.get('https://yesno.wtf/api')
  yes_or_no = resp.json()['answer']
  return yes_or_no

@app.route('/')
def index():
  yes_or_no = get_yes_or_no()
  return yes_or_no

if __name__ == "__main__":
    app.run(debug=False, use_reloader=True)
