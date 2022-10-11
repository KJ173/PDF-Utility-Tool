from setuptools import setup
from setuptools import find_packages

setup(
    name='PdfEditor',
    version='0.0.3',
    description='Modify previously created PDF\'s',
    author='Yamil Asusta (elbuo8); additions by Brandon B',
    author_email='yamil.asusta@upr.edu; titusrevised@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    url='https://github.com/titusrevised/PdfEditor',
    zip_safe = False,
    install_requires=[
        'reportlab'
    ],
    dependency_links=[
        'http://github.com/knowah/PyPDF2/tarball/master'
    ],
)
