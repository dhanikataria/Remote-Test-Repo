# Terraform AWS EC2 Instance Project

This Terraform project sets up an AWS EC2 instance using a modular approach. It uses Terraform to provision infrastructure on AWS.

## Project Structure

- **modules/ec2_instance**: This directory contains the module for provisioning an EC2 instance. It consists of:
  - `main.tf`: Defines the AWS provider and the EC2 instance resource.
  - `outputs.tf`: Defines the outputs for the module, such as the public IP address of the created instance.
  - `variables.tf`: Defines the input variables for the module, such as the AMI ID and instance type.

- **main.tf**: This file in the root directory sets up the AWS provider and initializes the EC2 instance module. It specifies the values for the input variables required by the module.

- **outputs.tf**: This file in the root directory defines the outputs for the entire Terraform configuration, such as the public IP address of the EC2 instance.

## Terraform Code

The Terraform configuration provisions an EC2 instance on AWS in the `us-east-1` region. It uses the modular approach, with the EC2 instance module encapsulating the instance provisioning logic. The instance is created with the specified AMI ID and instance type.

## Getting Started

To use this Terraform project:

1. Ensure you have Terraform installed on your local machine.
2. Clone this repository to your local environment.
3. Navigate to the project directory in your terminal.
4. Run `terraform init` to initialize the project.
5. Run `terraform apply` to apply the Terraform configuration and provision the infrastructure.
6. After the provisioning is complete, you can see the outputs by running `terraform output`.

## Inputs

The project accepts the following input variables:

- `ami_variable`: The ID of the AMI (Amazon Machine Image) to use for the EC2 instance.
- `instance_type_variable`: The type of EC2 instance to launch.

## Outputs

The project provides the following outputs:

- `public-ip-address`: The public IP address of the provisioned EC2 instance.


