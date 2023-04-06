from setuptools import setup

VERSION = "0.0.3"

setup(
  name='util_msg',
  version=VERSION,
  url='https://github.com/keemsir/util-msg',
  author='keemsir',
  author_email='keemsir@gmail.com',
  packages=['util_msg'],
  description='for alarm',
  license='keemsir',
  install_requires=[
      'slack_sdk',
      'python-telegram-bot==13.14'
  ]
)
