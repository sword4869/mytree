from setuptools import find_packages, setup
setup(
    name='mytree',
    version='0.0.1',
    description='a pip package which is used to simulate `tree` command in linux',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author='sword4869',
    url='https://github.com/sword4869/mytree',
    packages=find_packages(),
    install_requires=[
        'configargparse'
    ],
    entry_points={
        'console_scripts': [
            'mytree = mytree.tree:main',
        ]
    }
)
