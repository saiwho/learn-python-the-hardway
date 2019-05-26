try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'This is Exercise 47 from LPTHW book',
'author': 'Sai Pothan',
'url': 'URL to get it at.',
'download_url': 'github.com/saipothanjanjanam',
'author_email': 'saipothan.janjanam@gmail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex47'],
'scripts': [],
'name': 'ex47'
} 

setup(**config)
