# csv-uploader
Kubernetes setup with Kops featuring mixed instance groups and auto-scaling for both deployment and cluster. Deploys Nginx and a Python web app in the same pod, with shared storage for static files. Includes Ansible for config management, Helm for templating, and uploads CSVs to S3 with Glacier transition.

## Features

- **Upload CSV Files**: Users can upload CSV files through a simple web interface.
- **File Processing**: The content of the CSV file is processed (for example, printed to the console).
- **File Storage**: Files are uploaded to an S3 bucket.
- **List Uploaded Files**: A list of previously uploaded files is displayed on the web page.
- **Responsive Design**: The web interface is built with Bootstrap to be responsive and visually appealing on all devices.

## Installation

1. **Clone the repository**:

   git clone https://github.com/rskelevra/csv-uploader.git
   cd csv-uploader

2. **Set up environment variable in .env file**:

AWS_BUCKET_NAME='changeme'
FLASK_ACCESS_KEY_ID='changeme'
FLASK_SECRET_ACCESS_KEY='changeme'
FLASK_SECRET_KEY='changeme'
DOMAIN='localhost'
PORT='8080'
PREFIX=

3. **Create empty uploads/ directory**:

mkdir uploads

4. **Build the Application**:
docker build -t csv-uploader:latest .

5. **Running the Application**:
docker run -p 8080:5000 --name web my-web-app:latest

The application will start on http://127.0.0.1:8080/. Open this URL in your web browser to access the web interface.

**AWS S3 Configuration**

To automatically transition objects to Amazon S3 Glacier after a specified number of days:

Go to the S3 bucket in your AWS Management Console.
Under the "Management" tab, create a lifecycle rule to transition objects to Glacier after your desired number of days.

# CSV File Uploader Web Application

docker pull rsharm49/casestudy:v0.2
docker run -p 8080:5000 --name web my-web-app:latest
Once uploaded, the files are processed, stored locally, and then uploaded to an Amazon S3 bucket. The application also lists previously uploaded files and provides immediate feedback to the user after an action.

**Project Structure**

csv-uploader/
│
├── app.py               # Main application file
├── .env                 # Environment variables (not included in version control)
├── uploads/             # Directory for storing uploaded files
├── templates/
│   └── index.html       # HTML template for the web interface
├── ansible/             # Ansible configuration directory
│   ├── playbook.yaml        # Main Ansible playbook
│   ├── templates/
│       ├── nginx.conf.j2/              # nginx conf file
├── helm/                # Helm chart directory
│   ├── Chart.yaml           # Helm chart metadata
│   ├── README
│   ├── values.yaml          # Default values for the chart
│   ├── templates/           # Directory for Kubernetes object templates
│       ├── deployment.yaml      # Deployment template
│       ├── service.yaml         # Service template
│       ├── hpa.yaml             # HPA template
│       ├── ingress.yaml         # Ingress template (optional)
│       ├── statefulset.yaml             # PVC template (if needed)
│       ├── configmap.yaml             # configmap.yaml (if needed)
│       └── _helpers.tpl         # Helper templates (if needed)
└── requirements.txt      # Python dependencies


Dependencies
Flask: A lightweight WSGI web application framework in Python.
Boto3: The AWS SDK for Python, used to interact with AWS services including S3.
python-dotenv: A tool to manage environment variables from a .env file.
Bootstrap: A popular front-end framework for developing responsive web applications.
Security Considerations
Ensure that your FLASK_SECRET_KEY and AWS credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) are kept secure and not exposed in version control.
Use environment variables to manage sensitive information securely.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask for providing an easy-to-use framework for web development.
Bootstrap for the front-end framework.
AWS for cloud storage services.