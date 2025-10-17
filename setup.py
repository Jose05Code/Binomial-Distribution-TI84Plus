#!/usr/bin/env python

from setuptools import setup, find_packages
import os

long_description = """
Binomial Distribution TI-84 Plus - package configuration for local editable installs
"""

version = "1.0.0"

requirements = [
]

if __name__ == '__main__':
    setup(
        name='binomial_distribution_ti84plus',
        version=version,
        description='Binomial utils and tests for TI-84 project',
        long_description=long_description,
        author="Jose",
        packages=find_packages(
            exclude=[
                'tests',
            ],
            include=[
                'src',
                'utils',
            ],
        ),
    license='MIT',
    install_requires=requirements,
            classifiers=[
          'Development Status :: 1 - Planning',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
    )