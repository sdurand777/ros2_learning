from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2_learning_msg',
    version='0.1.0',
    packages=find_packages(
        include=('ros2_learning_msg', 'ros2_learning_msg.*')),
)
