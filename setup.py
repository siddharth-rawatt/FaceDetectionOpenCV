# The setup script is the center of all activity in building, distributing, and installing modules using the Distutils.
# The main purpose of the setup script is to describe my module distribution to the Distutils, so that the
# various commands that operate on the modules do the right thing.

# building out applicaion as a package
from setuptools import find_packages, setup

# from typing import List


def get_requirements(file_path) -> list[str]:
    """
    This function will return a list of requirements modules
    """
    hyphen_e_dot = "-e."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)


setup(
    name="FaceDetection",
    version="0.0.1",
    author="Siddharth Rawat",
    author_email="siddharth.rawatt@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
