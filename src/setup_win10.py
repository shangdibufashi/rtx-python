from setuptools import setup, find_packages
import os, glob

pwd = os.path.dirname(os.path.abspath(__file__))

setup(
    name = 'rtx.rtx',
    version = '1.0.0',
    description = 'image processing for Python',
    author = 'Leo',
    classifiers=[
        'Development Status :: 1.0 - Beta',
        'Programming Language :: Cython',
        'Operating System :: Microsoft :: Windows',
    ],
    packages = find_packages(),
    package_dir={'rtx': 'rtx'},
    package_data={
        'rtx':["*.dll","*.json","*.pyd"]
    },
    # 如果你的包有Python代码，确保它们也被包含
    include_package_data=True,
    zip_safe=False,
)
