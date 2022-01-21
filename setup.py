from setuptools import setup, find_packages

from admin_views import __version__

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    author='Ludovic Delsol',
    author_email='ludel47@gmail.com',
    classifiers=['Development Status :: 1 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Topic :: Utilities'],
    description='Create custom view for Django admin.',
    include_package_data=True,
    install_requires=['django'],
    license='APL',
    long_description=README,
    name='django-admin-views',
    packages=find_packages(exclude=['sample_project']),
    url='https://github.com/iambrandontaylor/django-admin-sortable',
    version=__version__,
    zip_safe=False
)
