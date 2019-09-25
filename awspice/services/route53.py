# -*- coding: utf-8 -*-
from .base import AwsBase

class Route53Service(AwsBase):
    '''
    Class belonging to the Route 53 DNS Service
    '''

    def get_domains(self):
        '''
        Get hosted zones and its records

        Returns:
            (lst): List of Hosted Zones with Records
        '''
        domains = []
        for hz in self.list_hosted_zones():
            hz['Records'] = self.list_records(hz['Id'])
            domains.append(hz)
        return domains

    def list_hosted_zones(self):
        '''
        List all hosted zones

        Returns:
            List of hosted zones
        '''
        return self.inject_client_vars(self.client.list_hosted_zones()['HostedZones'])

    def list_records(self, hosted_zone_id):
        '''
        List all records for a hosted zone

        Args:
            hosted zone (str): The ID of the hosted zone that contains the resource record sets that you want to list

        Returns:
            List of DNS records
        '''
        records = []

        config = self.get_client_vars()
        paginator = self.client.get_paginator('list_resource_record_sets')
        for response in paginator.paginate(HostedZoneId=hosted_zone_id):
            for x in response['ResourceRecordSets']: records.append(x)

        return self.inject_client_vars(records, config)

    def list_records_by_domain(self, domain):
        '''
        List all records of a hosted-zone domain

        Args:
            domain (str): The DOMAIN name of the hosted zone that contains the resource record sets that you want to list

        Returns:
            List of DNS records
        '''
        hosted_zone = filter(lambda x: domain  + "." == x['Name'], self.list_hosted_zones())
        if hosted_zone:
            return self.list_records(hosted_zone[0]['Id'])
        return None

    def __init__(self):
        AwsBase.__init__(self, 'route53')
        self.change_region('us-east-1')
