# NetSpeedFox

NetSpeedFox is a tool that monitors your internet speed and sends an email alert if the download speed drops below a specified threshold. This tool allows you to configure your email settings and threshold limit easily.

## Features

- Monitors your internet speed every minute.
- Sends a personalized and funny email alert if the download speed drops below the configured threshold.
- Easy configuration through a setup script.

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/prabirsh/NetSpeedFox.git
    ```

2. **Install Required Libraries:**

    Make sure you have Python installed. Then, install the required libraries using pip:

    ```sh
    pip install speedtest-cli schedule
    ```

## Setup

1. **Run the Setup Script:**

    The setup script will prompt you to enter your email settings and speed threshold. This information will be saved in a `config.json` file.

    ```sh
    python setup.py
    ```

    You will be prompted to enter:
    - Your email address
    - Your email password (app-specific password from Google)
    - The recipient's email address
    - The speed threshold (in Mbps, example: 5)

2. **Check the Configuration File:**

    After running the setup script, a `config.json` file will be created with your configurations:

    ```json
    {
        "from_email": "your_email@gmail.com",
        "from_password": "your_password",
        "to_email": "recipient_email@gmail.com",
        "speed_threshold": 5
    }
    ```
## Google Account Password Retrieval Instructions

To obtain the email password, follow these steps:
- Open your Gmail account and click on 'Manage Google Account.'
- Search for 'App Passwords' and click on it.
- Create a new app by entering a name, then click 'Create.'
- A small popup window will appear displaying the password.
- Use this password during the setup process.

## Usage

1. **Run the Monitor Script:**

    The monitor script will check your internet speed every minute and send an email alert if the download speed drops below the configured threshold.

    ```sh
    python NetSpeedFox.py
    ```

## Configuration

The `config.json` file stores your email details and speed threshold. You can edit this file manually if needed.

### Example `config.json`

```json
{
    "from_email": "your_email@gmail.com",
    "from_password": "your_password",
    "to_email": "recipient_email@gmail.com",
    "speed_threshold": 5
}
```

## Troubleshooting

- Email Not Sent: Make sure you have allowed less secure apps to access your email account if you are using Gmail. You can enable this in your Google account settings.
- Incorrect Speed Readings: Ensure that your internet connection is stable and try running the script again.
