import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cifrazia-django-jet',
    description='Django-jet fork with Django@3.0+ support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Adam Bright',
    author_email='adam.brian.bright@gmail.com',
    url='https://github.com/AdamBrianBright/django-jet',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    license='AGPLv3',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Django >= 3.2, < 4.0',
        'six >= 1.15.0, < 2.0.0',
    ],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
