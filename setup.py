from setuptools import setup

setup(
    name='editai',
    version='0.1.0',
    py_modules=['app'],
    install_requires=[
        'click',
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'editai = app:cli',
        ],
    },
)
