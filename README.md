# 🛡️ BPH Intel Dashboard 🖥️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

[![OTX](https://img.shields.io/badge/OTX-Powered-orange.svg)](https://otx.alienvault.com/)

Track potential Bulletproof Hosting (BPH) infrastructure using AlienVault's Open Threat Exchange (OTX) API. This project includes a Python script for data fetching and processing, plus a sleek web dashboard for visualizing results.

## 🌟 Features

- 🔍 Real-time tracking of BPH infrastructure
- 🔄 Automated data fetching from AlienVault OTX
- 📊 Interactive web dashboard for data visualization
- ☁️ Easy deployment on Google Cloud Platform

## 🚀 Quick Start

1. Clone the repo
   ```sh
   git clone https://github.com/yourusername/bph-intel-dashboard.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your OTX API key
   ```sh
   export OTX_API_KEY='your_api_key_here'
   ```
4. Run the tracker
   ```sh
   python bph_tracker.py
   ```

## 📚 Table of Contents

- [Prerequisites](#-prerequisites)
- [Google Cloud Platform Setup](#-google-cloud-platform-setup)
- [VM Instance Setup](#-vm-instance-setup)
- [Python Script Setup](#-python-script-setup)
- [Website Setup](#-website-setup)
- [Running The Tracker](#-running-the-tracker)
- [Monitoring and Maintenance](#-monitoring-and-maintenance)

## 📋 Prerequisites

- Google Cloud Platform account
- AlienVault OTX API key
- Basic knowledge of Python and command-line operations

## 🌐 Google Cloud Platform Setup

### Create a New GCP Project

1. Go to the [GCP Console](https://console.cloud.google.com/)
2. Click on the project dropdown > **New Project**
3. Enter a project name and click **Create**

### Enable Necessary APIs

1. In the GCP Console, go to **APIs & Services** > **Dashboard**
2. Click **+ ENABLE APIS AND SERVICES**
3. Search for and enable:
   - Compute Engine API
   - Cloud Storage API

### Set Up a VPC Network (Optional, but Recommended)

1. Go to **VPC network** > **VPC networks**
2. Click **CREATE VPC NETWORK**
3. Follow the prompts to set up your network

## 💻 VM Instance Setup

### Create a VM Instance

1. Go to **Compute Engine** > **VM instances**
2. Click **CREATE INSTANCE**
3. Configure your VM (name, region, machine type, etc.)
4. Under **Boot disk**, select **Ubuntu 20.04 LTS**
5. Allow HTTP and HTTPS traffic
6. Click **Create**

### Connect to Your VM

- Use the **SSH** button in the GCP Console to connect to your VM

### Update the System and Install Python

```sh
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip -y
```

## 🐍 Python Script Setup

### Install Required Python Libraries

```sh
pip3 install OTXv2 requests
```

### Create the Python Script

1. Create `bph_tracker.py`
2. Paste the provided script content
3. Replace placeholders with your actual OTX API key and GCS bucket name

## 🌐 Website Setup

### Create a Google Cloud Storage Bucket

1. Go to **Cloud Storage** > **Buckets**
2. Click **CREATE BUCKET**
3. Follow the prompts to create your bucket

### Make the Bucket Publicly Accessible

1. In bucket details, go to **Permissions**
2. Add `allUsers` with the **Storage Object Viewer** role

### Enable Website Hosting for the Bucket

1. Go to **Website configuration**
2. Set `index.html` as the main page

### Create the HTML File

1. Create `index.html`
2. Paste the provided HTML content
3. Upload to your GCS bucket

## 🏃‍♂Running The Tracker

### Start the Python Script
python3 bph_tracker.py

```sh
python3 bph_tracker.py
```

### Access Your Website

Visit `https://storage.googleapis.com/YOUR_BUCKET_NAME/index.html`

## 🔧 Monitoring and Maintenance

- Check VM system logs: `sudo journalctl -u bph_tracker`
- Monitor script output: `tail -f nohup.out`
- Regularly update system and Python packages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/bph-intel-dashboard/issues).

## 👏 Acknowledgements

- [AlienVault OTX](https://otx.alienvault.com/)
- [Google Cloud Platform](https://cloud.google.com/)

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
