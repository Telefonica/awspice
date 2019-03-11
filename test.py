import awspice
import datetime
import time
from awspice import helpers

aws = awspice.connect(profile='default', region='eu-west-1')

regions = aws.service.ec2.get_regions()
profiles = aws.service.ec2.get_profiles()
start_time = time.time()

# x = aws.service.rds.get_database_by({'id':'alejandria-pro'})
# x = aws.finder.find_instances(filters={'status': 'running', 'user': 'fran'}, regions=regions)
# x = aws.finder.find_volumes(filters={'status': 'available', 'encrypted': 'false'})
# x = aws.service.ec2.get_secgroups_by(filters={'range': '0.0.0.0/0', 'protocol': 'tcp'}, regions=['eu-central-1'])
# x = aws.finder.find_ami(filters={'owner': '563089500877', 'public': 'false'})
# x = aws.finder.find_snapshots(filters={'owner': '456404846277', 'status': 'pending'})
# x = aws.service.ec2.get_address_by(filters={'instance': 'i-0ae13cb39424aabf4'})
# x = aws.service.ec2.get_instances_status_by({'event': ['system-reboot','instance-reboot']})
# x = aws.service.s3.get_bucket_acl('hackforgood')
# x = aws.service.iam.get_access_keys('david.amrani')
print aws.service.elb.get_loadbalancer_by('cname', 'elevenpaths-web-pro-1763591843.eu-west-1.elb.amazonaws.com')

# for y in x:
#     print(y['InstanceId'])
#     print(y['Region']['RegionName'])
#     print(y['KeyName'])
#     print


print time.time() - start_time