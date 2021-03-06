from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='distark',
      version=version,
      description="distributed python system",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      ],
      keywords='protobuf zmq distributed python',
      author='Gustave Pate',
      author_email='gustave_dot_pate_gmailcom',
      url='http://localhost:8080',
      license='',
      packages=find_packages('src'),
      package_dir={'': 'src'}, include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
      'console_scripts':
      ['distark=distark:main']
      }
      )
