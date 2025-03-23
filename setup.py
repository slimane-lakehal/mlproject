from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name='mlproject',
    version= '0.0.1',
    author= 'Slimane',
    author_email= 'lakehalslimane@gmail.com',
    package = find_packages(),
    install_required = get_requirements('requirements.txt')
    
)