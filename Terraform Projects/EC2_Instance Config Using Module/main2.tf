provider "aws" {

    region = "us-east-1"
  
}

module "ec2_instance" {

    source = "./modules/ec2_instance"
    ami_varible = "ami-0bb84b8ffd87024d8"
    instance_type_varibale = "t2.micro"
  
}