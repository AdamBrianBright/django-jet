import os

from setuptools import find_packages, setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path) as _fh:
        return _fh.read()


setup(
    name='cifrazia-django-jet',
    description='Modern template for Django-3 admin interface with improved functionality',
    long_description=read('README.md'),
    author='Adam Bright',
    author_email='adam.brian.bright@gmail.com',
    url='https://github.com/AdamBrianBright/django-jet',
    packages=find_packages(),
    license='AGPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Django >= 3.2, < 4.0',
        'six >= 1.15.0, < 2.0.0',
    ]
)
