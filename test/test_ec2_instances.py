import sys, json
import awspice
import botocore
if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

calls = [
    'DescribeInstances',
]

def load(filepath):
    with open(filepath) as file:
        content = json.loads(file.read())
    return content

@patch("botocore.client.BaseClient._make_api_call")
def test_get_instances(mock):
    mock.return_value=load('test/data/ec2/instances.json')
    region = 'eu-west-1'
    x = awspice.connect(region).service.ec2.get_instances()
    assert all(instance['Region']['RegionName'] == region for instance in x)
