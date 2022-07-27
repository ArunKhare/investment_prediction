from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME ="investment predictions"
VERSION = '0.0.1'
AUTHOR = "ARUN KHARE"
DESCRIPTION = "Automate the investment predictions process"
REQUIREMENTS_FILE_NAME= "requirements.txt"
HYPEN_E_DOT = '-e .'

def get_requirements_list()->List[str]:
    ''' 
    Description : This function is going to return list mention in requirements.txt file
    return: This funtion is going to return a list which contain list of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)