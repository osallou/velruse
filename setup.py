from setuptools import setup

requires=[
    'python-openid',
    'oauth2',
    'pyramid',
    'requests',
    'anykeystore',
],

tests_require = requires + [
    'nose',
    'selenium',
]

setup(name='velruse',
      version='0.3dev',
      description=(
          'Simplifying third-party authentication for web applications.'),
      long_description='',
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='Ben Bangert',
      author_email='ben@groovie.org',
      maintainer='Michael Merickel',
      maintainer_email='oss@m.merickel.org',
      url='velruse.readthedocs.org',
      license='',
      packages=['velruse'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={
          'tests': tests_require,
      },
      entry_points="""
      [paste.app_factory]
      main = velruse.app:make_velruse_app
      """,
      )
