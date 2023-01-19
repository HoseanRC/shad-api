from setuptools import setup, find_packages

requirements = [
    'wheel',
    'pycryptodome',
    'websockets',
    'pybase64',
    'aiohttp',
    'mutagen',
    'TinyTag',
    'urllib3',
]

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name = 'shadapi',
    version = '0.1',
    author='HoseanRC',
    author_email = '',
    description = 'This is an unofficial library and fastest library for deploying robots on Shad accounts.',
    keywords = ['shad', 'shadapi', 'shadio', 'chat', 'bot', 'robot', 'asyncio'],
    long_description = readme,
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/HoseanRC/shad-api',
    packages = find_packages(),
    install_requires = requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
)
