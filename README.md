csv-uploader: Web application for uploading and processing CSV files
This project provides a Python (Flask) web application that allows users to upload CSV files through a web interface. The application performs basic processing (currently printing content to the browser) and then stores the files in an S3 bucket.

Features
Upload CSV Files: Users can upload CSV files through a simple web interface.
Process CSV Files: The application performs basic processing on the uploaded files.
Store CSV Files in S3: Processed files are automatically uploaded to a configured S3 bucket.
Getting Started

Clone the repository:
git clone https://github.com/rskelevra/csv-uploader.git
cd csv-uploader
Use code with caution.

Install dependencies:
Python 3.x
pip (Python package manager)
AWS CLI with necessary S3 permissions
Flask and other required Python packages (see requirements.txt)
Boto3 library for interacting with AWS S3

pip install -r requirements.txt
Use code with caution.

Set up environment variables:
Create a file named .env in the project root directory and add the following environment variables (replace placeholders with your actual values:
FLASK_SECRET_KEY=<your-secret-key>
FLASK_ACCESS_KEY_ID=<your-aws-access-key-id>
FLASK_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_BUCKET_NAME=<your-s3-bucket-name>
DOMAIN='localhost'
PORT='8080'
PREFIX=

Run the application:
python app.py
Use code with caution.

The application will be accessible at http://127.0.0.1:5000/.

Additional Notes
Configure S3 lifecycle rules to transition files to Glacier storage for long-term retention (see documentation).
For security, avoid exposing sensitive information (secret key, AWS credentials) in version control.
This project demonstrates a basic setup. Enhancements can be made for advanced functionalities.

Deployment with Kubernetes
This project can be deployed to a Kubernetes cluster using Kops and Helm. The deployment utilizes mixed instance groups and auto-scaling for both application and cluster.

Prerequisites
Kops installed and configured
AWS CLI with necessary permissions
Kubernetes cluster