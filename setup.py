from setuptools import setup, find_packages

setup(
    name='CodeBot',
    version='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests','docker']),
    url='',
    license='',
    author='Elichai',
    author_email='',
    description='',
    install_requires=['docker', 'tweepy']
)
