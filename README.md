
Project Name


csv-uploader: Web application for uploading and processing CSV files
This project provides a Python (Flask) web application that allows users to upload CSV files through a web interface. The application performs basic processing (currently printing content to the browser) and then stores the files in an S3 bucket.

S3 Bucket Transition Lifecycle
To optimize storage costs and data retention, the application automatically configures an S3 lifecycle rule to transition files to S3 Glacier after a specified period. This helps reduce storage costs for infrequently accessed files.

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

S3 Bucket Transition Lifecycle Configuration

Log in to the AWS Management Console.
Navigate to S3 > Your Bucket > Management > Lifecycle rules.
Create a new lifecycle rule:
Rule Name: GlacierTransition
Action: Transition objects to S3 Glacier.
Transition: Configure the transition criteria (e.g., after 30 days for current versions, after 90 days for noncurrent versions).
Additional Notes

For security, avoid exposing sensitive information (secret key, AWS credentials) in version control.
This project demonstrates a basic setup. Enhancements can be made for advanced functionalities.
Deployment with Kubernetes (Optional)

This project can be deployed to a Kubernetes cluster using Kops and Helm. The deployment utilizes mixed instance groups and auto-scaling for both application and cluster.

Prerequisites

Kops installed and configured
AWS CLI with necessary permissions
Kubernetes cluster
Deployment instructions and configuration details are beyond the scope of this basic README. Refer to the project's documentation for advanced deployment options.

This consolidated README provides a high-level overview of the project's functionalities, including the new S3 bucket transition lifecycle feature. Refer to the project's codebase and documentation for further details.
