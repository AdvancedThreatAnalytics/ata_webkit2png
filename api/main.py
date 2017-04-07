import hashlib
import os
import subprocess

from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

TEMP_PATH = '/tmp/images'


@app.route("/ping", methods=['POST'])
def ping():
    return jsonify({'status': 'ok'})


@app.route("/", methods=['POST'])
def home():
    # Before each request cleanup the previous saved images
    for f in os.listdir(TEMP_PATH):
        os.unlink('/'.join([TEMP_PATH, f]))

    source_url = request.form.get('url')
    dimensions = request.form.get('dimensions', "1280x1024").split('x')
    if source_url:
        filepath = save_screenshot(source_url, dimensions[0], dimensions[1])
        return send_file(filepath, mimetype='image/png')

    return jsonify({
        'status': 'error',
        'msg': "Could not take screenshot"
    })


def save_screenshot(url, width, height, wait=5):
    """
    Save screenshot on TEMP_PATH for a given url
    :param url: url of the page
    :param width: width of the screenshot
    :param height: height of the screenshot
    :param wait: wait until page loads, in seconds
    :return: screenshot's path
    """
    filename = hashlib.md5(url).hexdigest()
    filepath = '{}/{}'.format(TEMP_PATH, filename)
    command = ["webkit2png",  "-W", "-o", filepath, "-w", str(wait), "-F",
               "javascript", "-F", "plugins", "-g", str(width), str(height),
               "-x", str(width), str(height), url]

    subprocess.call(command)

    return filepath

if __name__ == '__main__':
    app.run()
