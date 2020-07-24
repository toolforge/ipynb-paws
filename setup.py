from setuptools import setup, find_packages

setup(
    name='paws',
    version='0.2',
    description='Package / Module importer for importing code from Jupyter Notebook files (.ipynb) inside PAWS',
    url='http://github.com/yuvipanda/ipynb-paws',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
    python_requires='>=3.4'
)
