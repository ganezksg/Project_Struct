from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")



setup(
name="End_to_End_project",
version="0.0.1",
author="Sankar",
author_email="test",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")


)

