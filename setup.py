from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    "this function will return the list of requirements"

    requirements=[]

    with open (file_path) as fh:
        requirements=fh.readlines()
        requirements=[i.replace('\n',"") for i in requirements]

        return requirements







setup(
name = 'MLPROJECT',
version='0.0.1',
author='amol',
author_email='amolnayakawadi1@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)
