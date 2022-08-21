from setuptools import setup
import os
from glob import glob

package_name = 'command_publisher_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='raamkishore.p@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['diff_drive_publisher_node = command_publisher_package.diff_drive_publisher_node:main',
                            'cyclic_diff_drive_publisher_node = command_publisher_package.cyclic_diff_drive_publisher_node:main'
        ],
    },
)
