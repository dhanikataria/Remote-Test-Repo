provider "aws" {

    region = "us-east-1"
  
}

resource "aws_instance" "example" {

    ami = var.ami_varible
    instance_type = var.instance_type_varibale
  
}