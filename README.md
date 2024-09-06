
# csv-uploader
>Web application for uploading and processing CSV files. This project provides a Python (Flask) web application that allows users to upload CSV files through a web interface. The application performs basic processing (currently printing content to the browser) and then stores the files in an S3 bucket. 
>To optimize storage costs and data retention, the application automatically configures an S3 lifecycle rule to transition files to S3 Glacier after a specified period. This helps reduce storage costs for infrequently accessed files.
>This project can be deployed to a Kubernetes cluster using Kops and Helm. The deployment utilizes mixed instance groups and auto-scaling for both application and cluster.

## Table of Contents
* [Prerequisites](#prerequisites) 
* [Technologies Used](#technologies-used)
* [Architecture](#architecture)
* [Setup](#setup)
* [Getting Started](#getting-started)

## Prerequisites
- Kops installed and configured
- AWS CLI with necessary permissions
- Kubernetes cluster
- Deployment instructions and configuration details are beyond the scope of this basic README.

## Technologies Used
- Python
- Flask
- Docker
- Kops
- Ansible
- Helm

## Architecture
<!-- <img width="1299" alt="image" src="https://github.com/user-attachments/assets/7c8559a8-3d6f-468c-bdd6-77a63fd29ddd">
 -->

## Setup

Set up environment variables:
Create a file named .env in the project root directory and add the following environment variables (replace placeholders with your actual values:
FLASK_SECRET_KEY=<your-secret-key>
FLASK_ACCESS_KEY_ID=<your-aws-access-key-id>
FLASK_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_BUCKET_NAME=<your-s3-bucket-name>
DOMAIN='localhost'
PORT='8080'
PREFIX=

## Getting Started
Clone the repository:
git clone https://github.com/rskelevra/csv-uploader.git
cd csv-uploader

Run the application:
python app.py

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


