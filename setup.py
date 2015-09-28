from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(name='xcrawler',
      packages=find_packages(),
      install_requires=['lxml', 'cssselect'],
      version='1.1.0',
      description='A multi-threaded, open source web crawler',
      long_description=long_description,
      url='https://github.com/cardsurf/xcrawler',
      author='cardsurf',
      author_email='cardsurf@email.com',
      license='GNU GPL v2.0',
      platforms=['Any'],
      keywords=['crawler', 'spider', 'scraper'],
      classifiers=[
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Operating System :: OS Independent',
                    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                    'Topic :: Internet :: WWW/HTTP',
                    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                  ],
      )

