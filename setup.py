from setuptools import setup, find_packages

setup(
    name="nostrpy",
    version="0.1.1.dev1",
    description='A Python wrapper for Nostr Serverless API (NSA)',
    url='https://github.com/kevinbolger/nostrpy',
    author='Kevin Bolger',
    author_email='kevin@kevinbolger.xyz',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Data Scientists',
        'Topic :: Software Development :: Data Science Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],

    keywords='nostr nsa datascience',
    
    packages=find_packages(),

    install_requires=['requests'],

    python_requires='>=3.11',

)