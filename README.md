# S3 Cloud Automation using Python & Boto3

A simple DevOps automation project for managing AWS S3 files using Python, Boto3, and Bash.

## Features

- List files from an S3 bucket
- Upload local files to S3
- Download files from S3
- Delete files from S3
- Bash menu to run the automation scripts

## Architecture

Local Machine → Python + Boto3 → AWS S3

## Technologies

- Python
- Boto3
- AWS S3
- AWS CLI
- Bash
- Git & GitHub

## Project Structure

```text
s3-boto3-automation/
├── files/
│   └── .gitkeep
├── delete.py
├── download.py
├── list_files.py
├── upload.py
├── s3-automation.sh
├── .gitignore
├── README.md
└── venv/              # Local only, not committed

Setup
1. Clone the repository
git clone <your-repository-url>
cd s3-boto3-automation

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install Boto3
pip install boto3

4. Configure AWS credentials
Make sure AWS CLI is configured:
aws configure

Verify access:
aws s3 ls

Usage
Make the Bash script executable:
chmod +x s3-automation.sh

Run:
./s3-automation.sh

The menu provides:
1. List Files
2. Upload File
3. Download File
4. Delete File
5. Exit

What I Learned
- Using Boto3 to interact with AWS S3
- Automating cloud operations with Python
- Combining Bash and Python for automation
- Managing AWS resources through scripts
- Using virtual environments for Python dependencies
- Building and documenting a practical DevOps project
