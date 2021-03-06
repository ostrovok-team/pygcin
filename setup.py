import glob
import os
import shutil
from setuptools import setup
from setuptools.command.develop import develop
from subprocess import check_call

DESCRIPTION = 'Python wrapper for gcin (http://github.com/4u/gcin'

def install_deps():
    print "Installing dependencies"
    cdir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cdir)
    shutil.rmtree('pygcin/gcin', ignore_errors=True)
    check_call(['git', 'submodule', 'update', '--init', '--force'])
    os.chdir(os.path.join(cdir, 'pygcin/gcin'))
    for filename in glob.glob('.git*'):
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            shutil.rmtree(filename)
    check_call(['npm', 'install', '.'])
    os.chdir(cdir)

class do_develop(develop):
    def run(self):
        install_deps()
        develop.run(self)


setup(
    cmdclass={'develop': do_develop,},
    name='pygcin',
    version='0.11',
    packages=['pygcin'],
    package_dir={'pygcin': '.'},
    package_data={'pygcin': ['pygcin/*']},
    author='Yasha Borevich',
    author_email='j.borevich@gmail.com',
    url='http://github.com/ostrovok-team/pygcin',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    platforms='any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

