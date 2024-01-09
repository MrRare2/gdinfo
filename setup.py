from setuptools import setup, find_packages

setup(
    name="gdinfo",
    version="1.0",
    packages=find_packages(),
    install_requires=["requests"],
    include_package_data=True,
    package_data={"": ["LICENSE", "README.rst"]},
)
