from setuptools import setup, find_packages



setup(name = 'django-thumbs',
      version = '0.1',
      description = 'The easiest way to create thumbnails for your images with Django',
      author = 'Leander Hanwald',
      author_email = 'shockflash@web.de',

      url = 'https://github.com/shockflash/thumbs/',
      download_url = 'https://github.com/shockflash/thumbs/tarball/master',

      packages = find_packages(),

      license = 'BSD',

      classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )

