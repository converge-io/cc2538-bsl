from setuptools import setup, find_packages

with open("requirements.txt") as requirements:
    install_requires = requirements.readlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="cc2538-bsl",
    version="2.2",
    description="""Python cross-platform script to upload firmware
    via the serial boot loader onto the CC13xx, CC2538 and CC26xx SoC.""",
    long_description=long_description,
    license="BSD 3-clause Licence",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: BSD 3-Clause License",
        "Environment :: Console",
        "Operating System :: POSIX"
    ]
)
