from setuptools import setup

VERSION = "0.0.1"

setup(
  name='slack_msg',
  version=VERSION,
  url='https://github.com/keemsir/salck-msg',
  author='keemsir',
  author_email='keemsir@gmail.com',
  packages=[slack_msg'],
  description='for alarm',
  license='keemsir',
  install_requires=[
      'slack'
  ]
)
