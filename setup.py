from setuptools import setup, find_packages

setup(name="exodide",
      author="Yamada Hiroyuki",
      description="build_ext for Pyodide",
      version="0.0.0",
      url="https://github.com/ymd-h/exodide",
      install_requires=["wheel"],
      packages=find_packages(),
      package_data={"exodide":
                    ["cpython/*.h",
                     "cpython/cpython/*.h",
                     "cpython/internal/*.h"
                     "cpython/LICENSE",
                     "numpy/numpy/*.h",
                     "numpy/numpy/libdivide/*",
                     "numpy/numpy/random/*.h",
                     "numpy/LICENSE*"]},
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Development Status :: 4 - Beta",
                   "Operating System :: OS Independent",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Libraries"],
      include_package_data=True)
