from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dev_tools/__init__.py
from dev_tools import __version__ as version

setup(
	name="dev_tools",
	version=version,
	description="Frappe Dev Tools App",
	author="Aakvatech Limited",
	author_email="info@aakvatech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
