from setuptools import setup

setup(name='jupyter_v_kernel',
      version='0.0.1',
      description='Minimalistic V kernel for Jupyter',
      author='Rodrigo Abt',
      author_email='rodrigo.abt@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/rodabt/jupyter-v-kernel/',
      download_url='https://github.com/rodabt/jupyter-v-kernel/tarball/0.0.1',
      packages=['jupyter_v_kernel'],
      scripts=['jupyter_v_kernel/install_v_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'V'],
      include_package_data=True
      )
