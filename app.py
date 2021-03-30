import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging
import os
from dotenv import load_dotenv
from flask import json

load_dotenv()


from flask import Flask,render_template, request
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
#verify cloud
app.logger.info('%s',os.getenv('CLOUD_NAME'))

# home route
@app.route('/')
def hello():
    return "Hello World!"
  
@app.route('/upload', methods=['POST'])
def upload_file():
  app.logger.info('in upload route')

  cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))
  upload_result = None
  if request.method == 'POST':
    file_to_upload = request.files['file']
    app.logger.info('%s file_to_upload', file_to_upload)
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload)
      app.logger.info(upload_result)

      response = app.response_class(
        response=json.dumps(upload_result),
        status=200,
        mimetype='application/json'
      )
      return response

if __name__ == '__main__':
    app.run()

