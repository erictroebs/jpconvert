from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='jpconvert',
    version='0.3.7',
    author='Eric Tröbs',
    author_email='eric.troebs@tu-ilmenau.de',
    description='macros for Jupyter Notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erictroebs/jpconvert',
    project_urls={
        'Bug Tracker': 'https://github.com/erictroebs/jpconvert/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'requests==2.28.1',
        'python-magic==0.4.27'
    ]
)
