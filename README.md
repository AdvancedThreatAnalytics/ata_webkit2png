# Webkit2png

Webkit2png is a generic tool for getting a screenshot for a given url. The exposed API is written in Flask.

### Setup and Running
Just run `docker-compose up` and it will build the image and start up the container.
Exposed port is 8080 so API will be available at `http://localhost:8080/`

### API Doc
All the API implementation is located in the `api/main.py`.

1. Get the image for a given url with the given sizes. Response will either be the image or a json response with an error.

```python
import requests

url = 'http://localhost:8080/'
data = {
  'url': 'source_url', # URL to the html to be converted
  'dimensions': '800x600', # Dimensions of the screenshot, format: 'widthxheight', default is 1280x1024
  'wait': '5' # Wait before taking screenshot, format: Number in seconds, default is 5 seconds
}

resp = requests.post(url=url, json=data)
```

2. Convenient method for testing if everything is up and running correctly

```python
import requests

url = 'http://localhost:8080/ping'

resp = requests.post(url=url, json={})
resp.json['status'] == 'ok'
```
