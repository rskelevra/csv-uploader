from flask import Flask, request, redirect, url_for, render_template, flash
from dotenv import load_dotenv
import os
import boto3

# Load environment variables from .env


load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Initialize S3 client
s3_client = boto3.client('s3', aws_access_key_id = os.getenv('FLASK_ACCESS_KEY_ID'),
                         aws_secret_access_key = os.getenv('FLASK_SECRET_ACCESS_KEY'),
                         region_name='ap-south-1')

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process CSV file and collect lines to display
        content = []
        with open(filepath, 'r') as f:
            content = f.readlines()

        # Upload file to S3
        s3_client.upload_file(filepath, BUCKET_NAME, file.filename)

        flash(f'File {file.filename} successfully uploaded and processed.')

        # Display the file content in the browser
        return render_template('file_content.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)