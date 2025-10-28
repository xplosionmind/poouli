from setuptools import setup, find_packages
import pathlib

long_description = (pathlib.Path(__file__).parent.resolve() / 'README.md').read_text(encoding='utf-8')
packages = find_packages(where='src')

setup(
	name='poouli',
	version='0.1.3',
	description="Synchronize local files with MediaWiki instances.",
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://codeberg.org/tommi/poouli',
	author='Tommi',
	author_email='surfing@tommi.space',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.13',
		'Topic :: Documentation',
		'Topic :: Internet',
		'Topic :: Text Processing',
		'Topic :: Text Processing :: Markup :: Markdown',
		'Topic :: Utilities'
	],
	keywords='Experimental Publishing, Markdown, MediaWiki, Notes, Pandoc, Wiki, XPUB, Zettelkasten',
	packages=packages,
)
