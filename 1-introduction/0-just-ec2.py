from troposphere import Ref, Template
import troposphere.ec2 as ec2
t = Template()
instance = ec2.Instance("myinstance")
instance.ImageId = "ami-0dc5785603ad4ff54"
instance.InstanceType = "t2.micro"
t.add_resource(instance)
print(t.to_json())
print(t.to_yaml())