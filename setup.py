from setuptools import setup, find_packages

setup(
  name = 'panoptic-transformer',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Panoptic Transformer',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/panoptic-transformer',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention-mechanism',
  ],
  install_requires=[
    'einops>=0.3',
    'numpy',
    'pillow',
    'torch>=1.6',
    'torchvision'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
