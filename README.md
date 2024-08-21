README for csv uploader Web Application with S3 Integration
This project involves developing a basic web application using Python (Flask) to upload, process, and store CSV files.
The application allows users to upload CSV files through a simple web interface, processes the files by printing their content to the browser,
and then uploads the files to an Amazon S3 bucket. Additionally, the S3 bucket is configured to transition files to S3 Glacier for long-term storage.

## Prerequisites
Python 3.x installed on your system.
pip (Python package manager) installed.
AWS CLI configured with necessary permissions to access S3.
Flask and other required Python packages installed.
Boto3 library installed for interacting with AWS S3.
An S3 Bucket to store the uploaded CSV files.

## Setup Instructions
1. Clone the Repository
Clone this repository to your local machine:
   git clone https://github.com/rskelevra/csv-uploader.git
   cd csv-uploader

2. Install Required Python Packages manually or Install by requirements file:
   pip install -r requirements.txt

3. To create an S3 bucket
aws s3 mb s3://<your-bucket-name> --region <your-region>
# Example
aws s3 mb s3://ounass-csv-storage --region ap-south-1

4. Set Up Environment Variables
Create a .env file in the root directory of your project and add the following environment variables:
FLASK_SECRET_KEY=<changeme>
FLASK_ACCESS_KEY_ID=<your-aws-access-key-id>
FLASK_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_BUCKET_NAME=<your-bucket-name>
DOMAIN='localhost'
PORT='8080'
PREFIX=

5. Run the Application
Start the Flask application:
python app.py
The application should now be accessible at http://127.0.0.1:5000/. You can upload CSV files through the web interface.

6. Configure S3 Lifecycle Policy for Glacier Transition
To set up a lifecycle policy that moves objects to S3 Glacier after a certain number of days:
Log in to the AWS Management Console.
Navigate to S3 > Your Bucket > Management > Lifecycle rules.

Create a new lifecycle rule:
Rule Name: GlacierTransition
Action: Transition objects to S3 Glacier.

For Cost Optimization and Data Retention:
Move current versions to S3 Standard-IA after 30 days, and to S3 Glacier after 90 days.
Move noncurrent versions to S3 Glacier after 30 days.

7. Application Features
Upload CSV Files: Users can upload CSV files through the web interface.
Process CSV Files: The application reads the uploaded CSV file and prints its content to the browser.
Store CSV Files in S3: The processed CSV files are automatically uploaded to the configured S3 bucket.
View Processed Files: The web interface displays a list of previously processed files.
