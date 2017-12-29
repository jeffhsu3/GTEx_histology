import glob
from setuptools import setup


name = 'gtex_histology'
version = '0.1'


metadata = {'name': name,
            'version': version,
            'scripts': glob.glob('scripts/*.py'),
            'description': 'genda',
            'author': 'Jeffrey Hsu',
            'packages': ['gtex_histology',
                         ],
            }


if __name__ == '__main__':
    dist = setup(**metadata)
