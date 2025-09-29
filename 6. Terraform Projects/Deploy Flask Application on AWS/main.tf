provider "aws" {
    region ="us-east-1"
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "my_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.0.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
}



resource "aws_internet_gateway" "my_gateway" {
  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_route_table" "my_routingtable" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_gateway.id
  }

  }

resource "aws_security_group" "my_group" {
  name   = "group"
  vpc_id = aws_vpc.my_vpc.id

  ingress {
    description = "HTTP from VPC"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  
}

resource "aws_key_pair" "my_key" {
  key_name   = "my_public_key"  # Replace with your desired key name
  public_key = file("PATH_TO_PUBLIC_KEY")  # Replace with the path to your public key file
}

resource "aws_route_table_association" "rta1" {
  subnet_id      = aws_subnet.my_subnet.id
  route_table_id = aws_route_table.my_routingtable.id
}

resource "aws_instance" "server" {
  ami                    = "ami-0261755bbcb8c4a84"
  instance_type          = "t2.micro"
  key_name      = aws_key_pair.my_key.key_name
  vpc_security_group_ids = [aws_security_group.my_group.id]
  subnet_id              = aws_subnet.my_subnet.id

  connection {
    type        = "ssh"
    user        = "ubuntu"  # Replace with the appropriate username for your EC2 instance
    private_key = file("PATH_TO_YOUR_PUBLIC_KEY")  # Replace with the path to your private key
    host        = self.public_ip
  }

  # File provisioner to copy a file from local to the remote EC2 instance
  provisioner "file" {
    source      = "PATH_TO_PYTHON_FLASK_APPLICATION_app.py"  # Replace with the path to your local file
    destination = "/home/ubuntu/app.py"  # Replace with the path on the remote instance
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'Hello from the remote instance'",
      "sudo apt update -y",  # Update package lists (for ubuntu)
      "sudo apt-get install -y python3-pip",  # Example package installation
      "cd /home/ubuntu",
      "sudo pip3 install flask",
      "sudo python3 app.py &",
    ]
  }
}
