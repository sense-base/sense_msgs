from setuptools import setup
from glob import glob

package_name = 'eeg_msgs'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/msg', glob('eeg_msgs/msg/*.msg')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahmed Al-Hindawi',
    maintainer_email='a.al-hindawi@ucl.ac.uk',
    description='EEG Message Definitions',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
