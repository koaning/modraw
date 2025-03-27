import os
from setuptools import setup, find_packages


base_packages = [
    "anywidget>=0.9.2", 
    "pillow>=11.1.0"
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="modraw",
    version="0.1.0",
    description="Collection of Anywidget Widgets",
    author="Vincent D. Warmerdam",
    packages=find_packages(exclude=["notebooks"]),
    package_data={"modraw": ["static/*.js", "static/*.css"]},
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=base_packages,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
    license_files=["LICENSE"],
)
