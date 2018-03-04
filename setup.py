from setuptools import setup

setup(name='eeprom_spec',
      version='0.1',
      description='Writing human and machine readable data from EEPROM specification in json',
      url='https://github.com/sjeapes/eeprom_spec',
      author='Steve Jeapes',
      author_email='github.eeprom@arcoarena.co.uk',
      license='GPLv3',
      packages=['eeprom_spec'],
      requires=['intelhex'],
      zip_safe=False)