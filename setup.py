from setuptools import setup

setup(
    name='Flask-FirebaseAuth',
    version='0.1.1',
    description='Google Firebase Authentication integration for Flask',
    packages=['flask_firebaseauth'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.11',
        'PyJWT>=1.4',
        'cryptography>=1.6',
        'requests>=2.12',
    ])
