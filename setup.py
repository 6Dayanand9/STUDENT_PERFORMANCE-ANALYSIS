from setuptools import setup,find_packages
from typing import List
HYPEN_DOT_E = '-e'
def get_requirement(file_path:str):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
        return requirements
setup(
    name="Student PerFormance Analysis",
    version="0.0.1",
    author="Dayanand Nimbalkar",
    author_email="6nimbalkardayanand9@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement("requirement.txt"),
)