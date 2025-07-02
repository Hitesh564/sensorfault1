from setuptools import setup, find_packages

def get_requirements(file_path):
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any leading/trailing whitespace characters
    requirements = [req.strip() for req in requirements if req.strip()]
    
    return requirements

setup(
    name='sensor fault',
    version='0.0.1',
    author='Hitesh Jindal',
    author_email='jindalhitesh564@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt'),
)