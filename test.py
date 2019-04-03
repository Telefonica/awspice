import awspice
import datetime
import time
from awspice import helpers

aws = awspice.connect(profile='default', region='eu-west-1')

regions = aws.service.ec2.get_regions()
profiles = aws.service.ec2.get_profiles()
start_time = time.time()

######
#  Test for acm
######
#x = aws.service.acm.list_certificates(regions)
#print(x)

#x = aws.service.acm.get_certificate_by('domain', '*.e-paths.com', regions)
#print(x)

#x = aws.service.acm.get_certificate('arn:aws:acm:us-east-1:456404846277:certificate/96180e6f-13b3-45b7-a44f-2bfb8c942b5f', regions)
#print(x)

######
#  Test for ec2
######

x = aws.service.ec2.get_secgroups_by(filters={'range': '0.0.0.0/0', 'protocol': 'tcp'}, regions=['eu-central-1'])
print(x)

x = aws.service.ec2.get_address_by(filters={'instance': 'i-0ae13cb39424aabf4'})
print(x)

x = aws.service.ec2.get_instances_status_by({'event': ['system-reboot','instance-reboot']})
print(x)

######
#  Test for elb
######

x = aws.service.elb.get_loadbalancers(regions)
print(x)

x = aws.service.elb.get_loadbalancers_by('LoadBalancerName', 'QA-Selenium-Balancer', regions)
print(x)

######
#  Test for iam
######

x = aws.service.iam.get_inactive_users()
print(x)

x = aws.service.iam.get_users()
print(x)

x = aws.service.iam.get_access_keys('david.amrani')
print(x)

#No se que pasarle
#x = aws.service.iam.get_access_key_last_used()
#print(x)


######
#  Test for rds
######

x = aws.service.rds.get_databases(regions)
print(x)

x = aws.service.rds.get_database_by({'id':'alejandria-pro'})
print(x)

x = aws.service.rds.get_snapshots(regions)
print(x)

x = aws.finder.find_instances(filters={'status': 'running', 'user': 'fran'}, regions=regions)
print(x)

######
#  Test for s3
######

x = aws.service.s3.get_buckets()
print(x)

x = aws.service.s3.get_bucket_acl('hackforgood')
print(x)

x = aws.service.s3.get_public_buckets()
print(x)

x = aws.service.s3.list_bucket_objects('threats-backups')
print(x)

######
#  Test for finder
######

x = aws.finder.find_instances(profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_instance(filters={'status': 'attached'}, profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_volumes(filters={'status': 'available', 'encrypted': 'false'}, profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_volume(filters={'status': 'available', 'encrypted': 'false'}, profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_loadbalancers(profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_loadbalancer(filters={'status': 'running'}, profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_users(profiles=profiles)
print(x)

x = aws.finder.find_inactive_users(profiles=profiles)
print(x)

x = aws.finder.find_buckets(profiles=profiles)
print(x)

x = aws.finder.find_rds_databases(profiles=profiles, regions=regions)
print(x)

x = aws.finder.find_rds_snapshots(profiles=profiles, regions=regions)
print(x)

######   No se que pasarle
#  Test for security
######

#x = aws.security.get_instance_portlisting(instanceid='i-1ec1faa7')
#print(x)

######
#  Test for stats
######

x = aws.stats.get_stats(regions)
print(x)

x = aws.stats.cost_saving(regions)
print(x)

print(time.time() - start_time)