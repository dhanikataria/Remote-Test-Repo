# Lambda Function Project

This project contains a Lambda function written in Go. The function takes input parameters in JSON format and returns a response accordingly. Below are the steps to deploy and invoke the Lambda function.

## Overview

This Lambda function is designed to handle events with two fields: "name" and "age". It processes these fields and returns a message with the person's name and age.

## Deployment

1. **Create IAM Role**: Attach the AWS managed policy `AWSLambdaBasicExecutionRole` to a role named `lambda-ex`.

    ```powershell
    aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    ```

2. **Create Lambda Function**: Deploy the Lambda function using the provided ZIP file and configure its runtime environment. Please make sure to replace "Xs" in the following command with your specific ARN number

    ```powershell
    aws lambda create-function --function-name dhani --zip-file fileb://function.zip --handler bootstrap --runtime provided.al2023 --role arn:aws:iam::XXXXXXXXXXXX:role/lambda-ex
    ```

## Invocation

Invoke the Lambda function using the following command:

```powershell
aws lambda invoke --function-name dhani --cli-binary-format raw-in-base64-out --payload '{\"name\":\"Jim\",\"age\":33}' output.txt
