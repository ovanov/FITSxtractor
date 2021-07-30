from distutils.core import setup
setup(
  name = 'FITSxtractor',
  packages = ['FITSxtractor'],
  version = '0.1',
  license='MIT',
  description = 'This package extracts xml metadata from FITS output to a csv or xlsx file',
  author = 'ovanov',
  author_email = 'ovanov@protonmail.com',
  url = 'https://github.com/ovanov/FITSxtractor',
  download_url = 'https://github.com/ovanov/FITSxtractor/archive/refs/tags/v0.1.tar.gz',
  keywords = ['FITS', 'xml', 'csv', 'CLI programm'],
  install_requires=[
          'pandas',
          'openpyxl',
          'tqdm'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)