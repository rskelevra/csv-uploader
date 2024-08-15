# csv-uploader
Kubernetes setup with Kops featuring mixed instance groups and auto-scaling for both deployment and cluster. Deploys Nginx and a Python web app in the same pod, with shared storage for static files. Includes Ansible for config management, Helm for templating, and uploads CSVs to S3 with Glacier transition.

# CSV File Uploader Web Application

docker pull rsharm49/casestudy:v0.2
Once uploaded, the files are processed, stored locally, and then uploaded to an Amazon S3 bucket. The application also lists previously uploaded files and provides immediate feedback to the user after an action.

## Features

- **Upload CSV Files**: Users can upload CSV files through a simple web interface.
- **File Processing**: The content of the CSV file is processed (for example, printed to the console).
- **File Storage**: Files are stored locally in the `uploads/` directory and then uploaded to an S3 bucket.
- **List Uploaded Files**: A list of previously uploaded files is displayed on the web page.
- **Responsive Design**: The web interface is built with Bootstrap to be responsive and visually appealing on all devices.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- Flask
- Boto3 (AWS SDK for Python)
- python-dotenv (for environment variable management)
- An AWS account with access to S3

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rskelevra/csv-uploader.git
   cd csv-uploader

2. **Set up environment variables**:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Create empty uploads/ directory**:

mkdir uploads

4. **Install the required packages**:
pip install flask
pip install boto3
pip install python-dotenv

5. **Running the Application**:

python app.py
The application will start on http://127.0.0.1:8080/. Open this URL in your web browser to access the web interface.

**AWS S3 Configuration**

To automatically transition objects to Amazon S3 Glacier after a specified number of days:

Go to the S3 bucket in your AWS Management Console.
Under the "Management" tab, create a lifecycle rule to transition objects to Glacier after your desired number of days.

**Project Structure**

csv-uploader/
│
├── app.py               # Main application file
├── .env                 # Environment variables (not included in version control)
├── uploads/             # Directory for storing uploaded files
├── templates/
│   └── index.html       # HTML template for the web interface
├── k8s/                 # Kubernetes manifests directory
│   ├── deployment.yaml      # Deployment manifest
│   ├── service.yaml         # Service manifest
│   ├── hpa.yaml             # Horizontal Pod Autoscaler manifest
│   ├── ingress.yaml         # Ingress manifest (optional)
│   ├── pvc.yaml             # Persistent Volume Claim manifest (if persistent storage is needed)
├── ansible/             # Ansible configuration directory
│   ├── playbook.yaml        # Main Ansible playbook
│   ├── roles/               # Directory for Ansible roles
│       ├── webapp/              # Role for webapp configuration
│           ├── tasks/               # Tasks directory
│           │   └── main.yaml            # Main tasks for the webapp role
│           ├── templates/           # Templates directory for configuration files
│           │   └── .env.j2              # Jinja2 template for .env file
│           ├── files/               # Directory for static files
│           │   └── your_static_file     # Any static files you need to deploy
│           └── handlers/            # Handlers directory for the role
│               └── main.yaml            # Handlers (e.g., for restarting services)
├── helm/                # Helm chart directory
│   ├── Chart.yaml           # Helm chart metadata
│   ├── values.yaml          # Default values for the chart
│   ├── templates/           # Directory for Kubernetes object templates
│       ├── deployment.yaml      # Deployment template
│       ├── service.yaml         # Service template
│       ├── hpa.yaml             # HPA template
│       ├── ingress.yaml         # Ingress template (optional)
│       ├── pvc.yaml             # PVC template (if needed)
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