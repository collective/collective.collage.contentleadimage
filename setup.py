from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.collage.contentleadimage',
      version=version,
      description="Views for Products.Collage that display content with images from collective.contentleadimage",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read()  + "\n" +
                       open(os.path.join("docs", "AUTHORS.txt")).read()  + "\n" +
                       open(os.path.join("docs", "LICENSE.txt")).read()  + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone collage contentleadimage view image',
      author='JCU eResearch Centre',
      author_email='eresearch@jcu.edu.au',
      url='https://svn.plone.org/svn/collective/Products.Collage/addons/collective.collage.contentleadimage',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.collage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Collage',
          'collective.contentleadimage',
          'collective.fastview',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
