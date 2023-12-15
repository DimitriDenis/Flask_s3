from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS_VIDEO = {'mp4'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions



@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'Veuillez sélectionner une vidéo.'

    video_file = request.files['video']

    if not video_file or not allowed_file(video_file.filename, ALLOWED_EXTENSIONS_VIDEO):
        return 'Format de fichier vidéo non autorisé. Veuillez choisir une vidéo au format mp4.'

   
    video_presigned_url = upload_to_s3(video_file, 'Videos')

    
    return redirect(url_for('index'))


def upload_to_s3(file, folder):
    s3 = boto3.client('s3', region_name='YOUR_REGION', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')
    bucket_name = 'YOUR_BUCKET_NAME'

    filename = secure_filename(file.filename)
    s3.upload_fileobj(file, bucket_name, f"{folder}/{filename}")

   
    presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': f"{folder}/{filename}"})

    return presigned_url



@app.route("/")
def index():
   
    s3 = boto3.client('s3', region_name='YOUR_REGION', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')
    bucket_name = 'YOUR_BUCKET_NAME'

    
    video_response = s3.list_objects(Bucket=bucket_name, Prefix='Videos/')

    
    videos = []
    for video_obj in video_response.get('Contents', []):
        video_filename = video_obj['Key']
        video_presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': video_filename}, ExpiresIn=3600)

        title = video_filename.replace('Videos/', '').replace('.mp4', '').replace('_', ' ')

        videos.append({
            'title': title,
            'video_presigned_url': video_presigned_url
        })

    return render_template('index.html', videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
