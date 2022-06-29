from setuptools import setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages


package_name = 'urdf_tutorial_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
  	(os.path.join('share', package_name), glob('urdf/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='legacy',
    maintainer_email='ahoyos@academia.usbbog.edu.co',
    description='Robot example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	 	'state_publisher = urdf_tutorial_py.state_publisher:main'
        ],
    },
)
