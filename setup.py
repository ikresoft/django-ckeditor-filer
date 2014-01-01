#!/usr/bin/env python

from setuptools import setup, find_packages
github_url = 'https://github.com/ikresoft/django-ckeditor-filer'


setup(
    name='django-ckeditor-filer',
    version='1.0',
    description='Django CKEditor Filer',
    long_description='Integrate django filer in ckeditor',
    author='Enver Bisevac, Mirza Delic',
    author_email='ikresoft@gmail.com',
    url=github_url,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django, Django CKEditor Filer',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
)