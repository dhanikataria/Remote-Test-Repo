# Deploying Python Flask Application on AWS with Terraform

This repository contains Terraform code to deploy a Python Flask application onto the AWS Cloud.

## Prerequisites

Before you begin, ensure you have the following:

1. [Terraform](https://www.terraform.io/downloads.html) installed on your local machine.
2. AWS account credentials configured on your machine.

## AWS Credentials Configuration

To configure your AWS credentials, follow these steps:

1. Install the AWS Command Line Interface (CLI) by following the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

2. Once installed, run the following command to configure your AWS credentials:

    ```
    aws configure
    ```

3. You will be prompted to enter your AWS Access Key ID, Secret Access Key, default region, and output format. Enter these details as requested.

4. After successful configuration, your AWS credentials will be stored in the `~/.aws/credentials` file on your local machine.

## Deployment

To deploy the Python Flask application using Terraform, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the cloned repository directory:

    ```
    cd <repository_directory>
    ```

3. Initialize Terraform:

    ```
    terraform init
    ```

4. Review and customize the Terraform code with path to your public key, private key & python flask applicaiton (app.py or anyother app).

5. Apply the Terraform configuration to provision AWS resources:

    ```
    terraform apply
    ```

6. Once the Terraform apply process is complete, you will receive an output containing the URL of the deployed Flask application.

## Cleanup

To clean up and destroy the AWS resources created by Terraform, run the following command:
    ```
    terraform destroy
    ```

