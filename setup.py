from setuptools import setup, find_packages

def read_requirements(file_path="requirements.txt"):
    with open(file_path, "r") as file:
        requirements = [
            line.strip()
            for line in file
            if line.strip() and not line.startswith("#")
        ]
    return requirements

setup(
    name="heart-disease-prediction",
    version="1.0.0",
    author="Manas Sahu",
    author_email="sahumanasssss@gmail.com",
    description="Streamlit-based Heart Disease Prediction Machine Learning Application",
    long_description="A machine learning web application to predict heart disease using patient health parameters. Built with Python, Scikit-learn, and Streamlit.",
    long_description_content_type="text/plain",
    packages=find_packages(exclude=("officialenv",)),
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires=">=3.8",
)
