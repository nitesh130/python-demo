from setuptools import setup, find_packages
requirements = [r.strip() for r in open("requirements.txt").readlines()]
setup(
    name='python-demo',
    version='0.1.0',
    author='Nitesh Kumar',
    author_email='niteshkumar.jaiswal3@gmail.com',
    description='Test project using python for simple API and docker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nitesh130/python-demo',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=requirements,
)