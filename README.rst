Awspice
=======

|Version| |PythonVersions| |Docs| |Travis| |Codacy|

.. |Docs| image:: https://readthedocs.org/projects/awspice/badge/?version=latest
   :target: http://awspice.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs
.. |Version| image:: http://img.shields.io/pypi/v/awspice.svg?style=flat
   :target: https://pypi.python.org/pypi/awspice/
   :alt: Version
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/de3c0b7119994ee1a6a9736a7b95bf5d
   :target: https://app.codacy.com/app/davidmoremad/awspice?utm_source=github.com&utm_medium=referral&utm_content=Telefonica/awspice&utm_campaign=Badge_Grade_Dashboard
   :alt: Codacy
.. |Travis| image:: https://travis-ci.org/Telefonica/awspice.svg?branch=master
   :target: https://travis-ci.org/Telefonica/awspice
   :alt: Travis-CI
.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/awspice.svg
   :alt: PyPI - Python Version


Table of content (Full doc in `ReadTheDocs <http://awspice.readthedocs.io/en/latest/>`_) :

* `Installation <#installation>`_
* `Configuration <#configuration>`_
* `Test <#test>`_
* `Usage <#usage>`_


****************
What is Awspice?
****************

Is a wrapper of Boto3 library to list inventory and manage your AWS infrastructure
The objective of the wrapper is to make easier some common tasks in AWS, being able to dig through different regions and accounts.

Awspice make it easy to:

* List all your EC2 instances for multiple regions and accounts
* Get deployed infraestructure behind a Load Balancer.
* List all instances with exposed critical ports like 22 or 3389
* Get info about all certificates of your account/s
* Find exposed S3 buckets

------------------------------------------------------------------------------------------

.. installation-section

************
Installation
************

.. code-block:: bash

  pip install awspice

------------------------------------------------------------------------------------------

.. configuration-section

*************
Configuration
*************

The client is built and configured using ``awspice.connect()``. This method indicates the type of authentication and region on which you are going to work.


.. code-block:: python

  import awspice

  # Region: eu-west-1 | Profile: Default
  aws = awspice.connect()

  # Using profiles
  aws = awspice.connect(region='us-west-2', profile='dev_profile')
  # Using access keys
  aws = awspice.connect('us-west-2', access_key='AKIA***********', secret_key='/HR$4************')




------------------------------------------------------------------------------------------

.. usage-section

*****
Usage
*****

**Example**: Get balancer and instances behind a domain.

.. code-block:: python

  aws = awspice.connect()

  elb = aws.service.elb.get_loadbalancer_by('domain', 'donalddumb.com')
  for elb_instance in elb['Instances']:
    instance = aws.service.ec2.get_instance_by('id', elb_instance['InstanceId'])


**Example**: List all unused volumes

.. code-block:: python

  all_regions = aws.service.ec2.get_regions()
  volumes = awsmanager.service.ec2.get_volumes_by('status', 'available', regions=all_regions)


**Example**: Search instance in all accounts and regions by Public IP

.. code-block:: python

  profiles = aws.service.ec2.get_profiles()
  regions = aws.service.ec2.get_regions()

  for profile in profiles:
      aws.service.ec2.change_profile(profile)

      instance = aws.service.ec2.get_instance_by('publicip', '35.158.163.235', regions=regions)

      if instance:
          print 'Instance found: %s (Account: %s, Region: %s)' % (instance['InstanceId'], instance['RegionName'], instance['Authorization']['Value'])
          break
