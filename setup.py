from setuptools import setup, find_packages

import multigrid


setup(name='multigrid',
	  version="{ver} {rev}".format(
		  ver=multigrid.__version__,
		  rev=multigrid.__revision__,
		  ),
	  description='MultiGrid',
	  long_description=open('README.txt').read(),
	  author=', '.join(multigrid.__author__),
	  author_email='AntonEvgenich@gmail.com',
	  install_requires=['celery>=3.0.0',
						'argparse>=1.1',
						'dill>=0.1.0'
						],
	  packages=find_packages(),
	  platforms=['any'],
	  keywords=['distributed computing',
				'parallel programming',
				'Modelica'
				],
	  license='GPL2',
	  classifiers=[
		  'Development Status :: 1 - Alpha',
		  'Intended Audience :: Developers',
		  'Intended Audience :: Education',
		  'Intended Audience :: Science/Research',
		  'License (GPL2)',
		  'Programming Language :: Python',
		  'Topic :: Scientific/Engineering',
		  'Topic :: Software Development',
		  ],
	  entry_points={
		  'console_scripts':
			  ['multigrid = multigrid.api:main']
	  },
	  )