import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mailrelay-python",
    version="1.0.2",
    description="Python developed library for mailrelay API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GearPlug/mailrelay-python",
    author="Johann S. Cardenas",
    author_email="jcardenas@gearplug.io",
    license="MIT",
    packages=["mailrelay"],
    install_requires=["requests"],
    zip_safe=False,
)