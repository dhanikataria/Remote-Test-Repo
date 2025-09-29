# Cloud based Flask Application to Create Jira Tickets from GitHub Issues

This Flask application automatically creates a Jira ticket when an issue is created in a GitHub repository. The application is hosted on an AWS EC2 instance and communicates with GitHub via a webhook. Below are the instructions to set up and deploy this application.

## Prerequisites

- Python 3.x
- Flask
- AWS EC2 instance
- Valid domain name for Jira
- Valid Jira email address
- Jira API token
- GitHub repository

## Setup

1. Clone the Repository

    Clone the repository containing the Flask application code to your local machine.

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install Dependencies

    Install the necessary Python packages using `pip`.

    ```bash
    pip install flask requests
    ```

3. Configure the Application

    Edit the Flask application script to include your Jira domain, email, and API token. Replace the placeholders with your actual credentials. It is recommended to use environment variables to set up all these 3 elements and not hard coding them in code itself.

4. Launch the Flask Application

    Start the Flask application on your EC2 instance.

    ```bash
    python app.py
    ```

5. Set Up AWS EC2 Instance

    Ensure your EC2 instance is properly configured to allow incoming traffic on port 5000. This can be done by configuring the security group associated with the instance.

6. Create a GitHub Webhook

    1. Navigate to your GitHub repository.
    2. Go to **Settings** > **Webhooks** > **Add webhook**.
    3. Set the **Payload URL** to `http://<EC2_PUBLIC_IP>:5000/jira`.
    4. Set the **Content type** to `application/json`.
    5. Choose **Let me select individual events** and select **Issues**.
    6. Click **Add webhook**.

7. Test the Setup

    Create a new issue in your GitHub repository. This should trigger the webhook and send a POST request to the Flask application, which will create a Jira ticket.

