#!/bin/bash

echo "S3 Cloud Automation"
echo "1. List Files"
echo "2. Upload File"
echo "3. Download File"
echo "4. Delete File"
echo "5. Exit"

read -p "Choose an option: " choice

case $choice in
    1)
        python list_files.py
        ;;
    2)
        python upload.py
        ;;
    3)
        python download.py
        ;;
    4)
        python delete.py
        ;;
    5)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option"
        ;;
esac
