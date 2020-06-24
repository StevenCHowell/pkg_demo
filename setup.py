import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='demo-python-pkg',
    version='0.0.1',  # see www.python.org/dev/peps/pep-0440/#version-scheme
    author='Steven C. Howell',
    author_email='me@some_email.com',
    description='Throw away code to test packaging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),  # no need to explicitly list
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # zip_safe=False,  # setuptools.readthedocs.io/en/latest/setuptools.html#setting-the-zip-safe-flag
)
