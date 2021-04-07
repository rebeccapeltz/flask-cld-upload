import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import Flask,render_template, request
from cloudinary.utils import cloudinary_url

load_dotenv()

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)
#verify cloud
app.logger.info('%s',os.getenv('CLOUD_NAME'))

# home route
@app.route('/')
def hello():
    return "Hello World!"


@app.route("/upload", methods=['POST'])
@cross_origin()
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
      app.logger.info(type(upload_result))
      return jsonify(upload_result)
    
@app.route("/cld_optimize", methods=['POST'])
@cross_origin()
def cld_optimize():
  app.logger.info('in optimize route')

  cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))
  if request.method == 'POST':
    public_id = request.form['public_id']
    app.logger.info('%s public id', public_id)
    if public_id:
      cld_url = cloudinary_url(public_id, fetch_format='auto', quality='auto', secure=True)
      
      app.logger.info(cld_url)
      return jsonify(cld_url)

if __name__ == '__main__':
    app.run()

