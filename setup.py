from setuptools import setup, find_packages

setup(name='WEB_CLIENT',
      version='0.1',
      description='implementation of the web part of the client-averaged service',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
	      'Programming Language :: Python',
	      'Programming Language :: Python :: 3.6',        
	      'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='django webclient',
      url='https://bmstu.codes/developers34/web-client',
      author='Brodnikov Nazar',
      author_email='Brodnikovnv@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'django>=2.1', 'requests>=2.18' , 'django-heroku', 'gunicorn'
      ],
      include_package_data=True,	
      zip_safe=False)
