import unittest
import awspice

class ModuleFinderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nStarting unit tests of base service module")

    def test_get_client_vars(self):
        aws = awspice.connect('eu-west-2', profile='test')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test', 'access_key': 'None'})

    def test_set_auth_config(self):
        aws = awspice.connect('eu-west-2', profile='test')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test', 'access_key': 'None'})
        aws.service.ec2.set_auth_config(region=client_vars['region']['RegionName'], profile='test2')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test2', 'access_key': 'None'})
        aws.service.ec2.set_auth_config(region=client_vars['region']['RegionName'], access_key='key', secret_key='secret')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'None', 'access_key': 'key'})

    def test_change_region(self):
        aws = awspice.connect('eu-west-2', profile='test')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test', 'access_key': 'None'})
        aws.service.ec2.change_region('eu-west-1')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (Ireland)', 'Country': 'Ireland', 'RegionName': 'eu-west-1'}, 'profile': 'test', 'access_key': 'None'})

    def test_change_profile(self):
        aws = awspice.connect('eu-west-2', profile='test')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test', 'access_key': 'None'})
        aws.service.ec2.change_profile('test2')
        client_vars = aws.service.ec2.get_client_vars()
        self.assertEqual(client_vars, {'region': {'Description': 'EU (London)', 'Country': 'London', 'RegionName': 'eu-west-2'}, 'profile': 'test2', 'access_key': 'None'})

    def test_get_profiles(self):
        aws = awspice.connect('eu-west-2', profile='test')
        profiles = aws.service.ec2.get_profiles()
        ss = ['test' in item or 'test2' in item for item in profiles]
        self.assertEqual(True, all(ss))

    def test_parse_profiles(self):
        aws = awspice.connect('eu-west-2', profile='test')
        profiles = aws.service.ec2.parse_profiles('ALL')
        ss = ['test' in item or 'test2' in item for item in profiles]
        self.assertEqual(True, all(ss))
        profiles = aws.service.ec2.parse_profiles(['test'])
        self.assertEqual(profiles, ['test'])
        profiles = aws.service.ec2.parse_profiles('test5')
        self.assertEqual(profiles, ['test5'])

    def test_parse_regions(self):
        aws = awspice.connect('eu-west-1', profile='test')
        regions = aws.service.ec2.parse_regions('eu-west-2')
        self.assertEqual(regions, [{'RegionName':'eu-west-2'}])
        regions = aws.service.ec2.parse_regions(['eu-west-1', 'eu-west-2'])
        ss = ['eu-west-1' in item.values() or 'eu-west-2' in item.values() for item in regions]
        self.assertEqual(True, all(ss))
        regions = aws.service.ec2.parse_regions([{'RegionName':'eu-west-1'}, {'RegionName':'eu-west-2'}])
        ss = ['eu-west-1' in item.values() or 'eu-west-2' in item.values() for item in regions]
        self.assertEqual(True, all(ss))




if __name__ == '__main__':
        unittest.main()