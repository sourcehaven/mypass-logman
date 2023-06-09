from setuptools import setup

setup(
    name='mypass-logman',
    version='1.0.0',
    description='Mypass Login Manager',
    author='ricky :) (: skyzip',
    author_email='skyzip96@gmail.com',
    license='MIT',
    packages=['mypass_logman'],
    package_dir={'mypass_logman': 'mypass'},
    install_requires=['requests'],
    package_data={'': ['license']}
)
