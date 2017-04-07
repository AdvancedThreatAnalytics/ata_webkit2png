# Webkit2png

Webkit2png is a generic tool for getting a screenshot for a given url.
Over that there is a simple API written in Flask.

### Setup and Running
Just run `docker-compose up` and it will build the image and start up the container.
Exposed port is 8080 so API will be available at `http://localhost:8080/`

### API Doc
All the stuff is located in the `api/main.py`

```json
Request Method: POST 
API Endpoint: /
Descripton: Get the image for a given url with the given sizes 

Params:
    {
      "url": "source_url", // required
      "dimensions": "800x600", // dimensions of the screenshot, format: "widthxheight", default is 1280x1024
      "wait": "5" // wait until page will be loaded, format: number in seconds, default is 5 seconds
    }
    
Response: Directly Image file or a json response about the error

Request Method: POST
API Endpoint: /ping
Description: Convenient method for testing if everything is up and running correctly
Params: No params
Response:
    {
      "status": "ok"
    }
```
