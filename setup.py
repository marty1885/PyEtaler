from distutils.core import setup
from distutils.command.build import build

import subprocess
import shutil
import os
import sys

if sys.version_info < (3, 0):
    raise ValueError("Do not run the script under Python2")

src_dir = os.path.dirname(os.path.abspath(__file__))
print(src_dir)
class build_binding(build):
    def run(self):
        protoc_command = ["python3", os.path.join(src_dir, "genbinding.py")]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        shutil.copyfile('etaler_rflx.so', 'etaler/etaler_rflx.so')
        shutil.copyfile('etaler_rflx_rdict.pcm', 'etaler/etaler_rflx_rdict.pcm')
        build.run(self)

setup(
  name = 'pyetaler',
  packages = ['etaler'],
  version = '0.0.1',
  license='bsd-3-clause',
  description = 'A high performance implementation of Numenta\'s HTM algorithms',
  author = 'Martin Chang',
  author_email = 'marty188586@gmail.com',
  url = 'https://github.com/etaler/PyEtaler/tree/master',
  keywords = ['HTM', 'Hierarchical Temporal Memory', 'Numenta', "AI", "SDR"
      "sparse distributed representation", "bioinspired"],
  install_requires=[
          'cppyy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD 3-clause "New" or "Revised" license',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  cmdclass = {
      'build': build_binding
  },
  package_data = {'':['*.so', '*.pcm', '*.dll']}
)