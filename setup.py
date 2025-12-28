from setuptools import setup, find_packages

def read_requirements(file_path="requirements.txt"):
    with open(file_path, "r") as file:
        requirements = [
            line.strip()
            for line in file
            if line.strip() and not line.startswith("-")
        ]
    return requirements


setup(
    name="house_pricing",
    version="0.0.1",
    author="Manas Sahu",
    author_email="sahumanasssss@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements(),
)
