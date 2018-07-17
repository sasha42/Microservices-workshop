# Microservices workshop

Hello and welcome!

These are materials that were prepared for the [Miroservices workshop](https://www.meetup.com/noisebridge/events/rdmjcpyxkbvb/) held at Noisebridge on the 26th of July 2018. In this workshop you will learn how to create a function that generates data, how to expose it as a server, and then how to host it as a microservice.

## Preliminary setup
For this workshop you will need the latest version of Python 3, as of writing it is `python 3.6.6`. It's useful to also have git set up, along side heroku.
```
# create the repository
mkdir microservice
cd microservice

# create a git instance
git init

# if you don't have virtualenv installed, install it
sudo pip3 install virtualenv

# then create virtualenv
virtualenv venv
source venv
```

Once preliminary setup is complete, we will install two basic libraries that will help us with the process.
```
pip install flask requests
```

## Creating a function
In order to create a function, you will first need a source of data. For this example, we'll be scraping a public API that returns a yes or a no. You can [find more APIs here](https://github.com/toddmotto/public-apis).
```python
import requests

def get_yes_or_no():
  resp = requests.get('https://yesno.wtf/api')
  yes_or_no = resp.json()['answer']
  return yes_or_no
```
Once you have this function, you're able to have a yes or a no returned to you.

## Exposing as a service
You will now need to wrap this function in such a way that you're able to expose it as a service. For this, I'll be using the popular [Flask](http://flask.pocoo.org/) library.
```python
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
```

The above snippet will provide the basis, however you will need to add your view functions as well as the function we generated above.

```python
@app.route('/')
def index():
  yes_or_no = get_yes_or_no()
  return yes_or_no
```

In the end, your python file should look like the `app.py` file included in this repository.

## Hosting microservice
We will be hosting the service on [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) which hosts microservices for free. You'll need to set up an account and the CLI interface.

Once setup, you will need to create a new project, and push to it:
```
heroku create
git add app.py requirements.txt Procfile runtime.txt
git commit -m "initial commit"
git push heroku master
```
