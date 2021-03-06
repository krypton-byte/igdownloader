
from distutils.core import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'instatools3',        
  packages = ['instatools3'],   
  version = '0.0.1',    
  license='MIT',     
  description = 'Intagram Stalker&Downloader', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/instatools3',   
  download_url = 'https://github.com/krypton-byte/instatools3/archive/0.0.1.tar.gz',    
  keywords = ['instagram', 'downloader', 'stalker'], 
  install_requires=[           
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)