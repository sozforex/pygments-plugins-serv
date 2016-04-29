#!/usr/bin/python

from setuptools import setup

setup(name='pygments-plugins-serv',
      version='0.0.1',
      description='Pygments Github custom lexers.',
      keywords='pygments github lexer',
      license='BSD',

      author='Kichatov Feodor',
      author_email='sozforex@gmail.com',

      url='https://github.com/sozforex/pygments-plugins-serv',

      packages=['pygments_plugins_serv'],
      install_requires=['pygments>=2.0.2'],

      entry_points='''[pygments.lexers]
                      M4Lexer=pygments_plugins_serv.lexers.m4:M4Lexer''',

      classifiers=[
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)