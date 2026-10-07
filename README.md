# S3 Cloud Automation using Python & Boto3

A practical DevOps automation project for managing AWS S3 objects using Python, Boto3, AWS CLI, and Bash.

This project automates common S3 operations such as listing, uploading, downloading, and deleting files through Python scripts and a simple Bash menu.

## Features

- List objects from an AWS S3 bucket
- Upload local files to S3
- Download files from S3
- Delete files from S3
- Run S3 operations through a Bash menu
- Use Python and Boto3 for AWS automation
- Use AWS CLI to verify S3 operations

## Architecture

```text
Local Machine
     │
     ▼
Bash Menu
     │
     ▼
Python Scripts
     │
     ▼
Boto3
     │
     ▼
AWS S3
```

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
└── README.md
```

> `venv/` is used locally for Python dependencies and is excluded from Git using `.gitignore`.

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- AWS CLI installed
- An AWS account
- AWS credentials configured
- Access to an S3 bucket

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd s3-boto3-automation
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Boto3

```bash
pip install boto3
```

### 4. Configure AWS credentials

Configure the AWS CLI:

```bash
aws configure
```

Verify AWS access:

```bash
aws s3 ls
```

## Usage

Make the Bash script executable:

```bash
chmod +x s3-automation.sh
```

Run the automation menu:

```bash
./s3-automation.sh
```

The menu provides:

```text
S3 Cloud Automation
1. List Files
2. Upload File
3. Download File
4. Delete File
5. Exit
```

### Run Individual Python Scripts

You can also run each operation directly.

**List S3 files:**

```bash
python list_files.py
```

**Upload a file:**

```bash
python upload.py
```

**Download a file:**

```bash
python download.py
```

**Delete a file:**

```bash
python delete.py
```

## Example

The automation can perform the following workflow:

```text
Local File
    │
    ├── Upload ────────► S3
    │
    ├── List ──────────► View S3 Objects
    │
    ├── Download ◄───── S3
    │
    └── Delete ────────► S3
```

## Security

- AWS credentials are not stored in the source code.
- AWS CLI credentials are used for authentication.
- The virtual environment is excluded from Git.
- No sensitive credentials or secrets should be committed to the repository.

## What I Learned

- Using Boto3 to interact with AWS S3
- Automating cloud operations with Python
- Combining Bash and Python for automation
- Working with AWS CLI
- Managing files in cloud storage programmatically
- Using Python virtual environments
- Building and documenting a practical DevOps automation project

## Future Improvements

- Add command-line arguments for file operations
- Add error handling and validation
- Add logging
- Support custom S3 buckets and file paths
- Add GitHub Actions for automated testing

## Author

**Tanjim Ahmed**

DevOps Intern
