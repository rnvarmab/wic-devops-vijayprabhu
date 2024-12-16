resource "aws_instance" "ec2_instance" {
    ami = "ami-0c1a7f89451184c8b"
    instance_type = var.instance_type
    tags = {Name = "third-machine"}
}