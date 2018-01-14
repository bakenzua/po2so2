from setuptools import setup

setup(name='Po2So2',
      version='0.0.1',
      description='A package to calculate po2 from so2 and vice versa',
      long_description='A package to calculate po2 from so2 and vice versa',
      url='https://github.com/bakenzua/po2so2.git',
      author='bakenzua',
      author_email='barnaby.sanderson@gstt.nhs.uk',
      license='MIT',
      packages=['po2so2'],
      package_dir={'': 'src'},
      install_requires=[
          'numpy'
      ],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Healthcare Industry',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',

          # Developed on 3.6
          # Not tried on 2 or other versions
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],

      )
