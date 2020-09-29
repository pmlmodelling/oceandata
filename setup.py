from setuptools import Command, find_packages, setup


DESCRIPTION = "Random methods to get urls of oceanographic data"
LONG_DESCRIPTION = """
**oceandata** is a Python package providing tools for searching oceanographic data

"""

PROJECT_URLS = {
    "Bug Tracker": "https://github.com/r4ecology/oceandata/issues",
    "Source Code": "https://github.com/r4ecology/oceandata",
}

#REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]


setup(name='oceandata',
      version='0.1.0',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      python_requires='>=3.6.1',
      classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

      project_urls=PROJECT_URLS,
      url = "https://github.com/r4ecology/oceandata",
      author='Robert Wilson',
      maintainer='Robert Wilson',
      author_email='rwi@pml.ac.uk',

      packages = ["oceandata"],
      setup_requires=[
        'setuptools',
        'setuptools-git',
        'wheel',
    ],
      install_requires = ["pandas", "bs4"],
      zip_safe=False)




