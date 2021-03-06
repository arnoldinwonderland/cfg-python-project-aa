import os
import requests

from flask import Flask, render_template, request

app = Flask(__name__)

#from dotenv import load dotenv
#load_dotenv()

@app.route('/')
def index():
    response = requests.get(
        'https://api.thecatapi.com/v1/images/search',
        headers={'x-api-key': os.getenv('API_KEY')}
    )
    data = response.json()[0]
    print(data)
    url = data['url']
    image_id = data['id']
    return render_template('index.html', picture=url, image_id=image_id)

@app.route('/save')
def add_favourite():
    image_id = request.args.get('image_id')

    response = requests.post(
        'https://api.thecatapi.com/v1/favourites',
        headers={'x-api-key': os.getenv('API_KEY')},
        json={
            'image_id': image_id,
            'sub_id': os.getenv('SUB_ID')
        }
    )
    data = response.json()
    print(data)
    return '{}! Go back!'.format(data['message'])

@app.route('/fav')
def see_favourites():
    response = requests.get(
        'https://api.thecatapi.com/v1/favourites?limit=3',
        headers={'x-api-key': os.getenv('API_KEY')}
    )
    data = response.json()
    print(data)
    return render_template('favourites.html', data=data)

if __name__ == '__main__':
  if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)