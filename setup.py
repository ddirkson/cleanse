import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cleanse',
    version='0.1',
    license='MIT',
    description='Replace sensitive xml data while maintaining its structure',
    long_description=long_description,
    author='Dalton Dirkson',
    author_email='sodakdoubled@gmail.com',
    url='https://github.com/SodakDoubleD/cleanse',
    download_url='https://github.com/SodakDoubleD/cleanse/',
    keywords='XML data-spoofing python CLI tool',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'Faker',
        'lxml'
    ],
)
