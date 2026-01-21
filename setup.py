# setup.py serves as the core configuration file for Python package distribution using setuptools, enabling commands like pip install . to build, install, and distribute projects. Developers create it to define metadata, discover packages automatically, and manage dependencies for shareable, installable modules.

from setuptools import find_packages, setup

setup(
    name="bankbot_chatbot",
    version="0.1.0",
    author="Piyush Kumar",
    author_email="piyushbhashkar@gmail.com",
    packages=find_packages(),  # to find the constructor __init_.py and treat it as local environment 
    install_requires=[] # for all the packages in requiremnts.txt
)