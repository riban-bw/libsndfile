#!/usr/bin/python3
""" Script to build Zynthian patched libsndfile1 library """

from platform import uname
from os import mkdir, chdir, system, rename
import shutil
from glob import glob

arch = uname().machine
try:
    shutil.rmtree("zynbuild")
except:
    pass

mkdir("zynbuild")
chdir("zynbuild")
system('cmake -DBUILD_SHARED_LIBS=RELEASE -DBUILD_SHARED_LIBS=ON -DBUILD_PROGRAMS=OFF -DBUILD_EXAMPLES=OFF -DINSTALL_MANPAGES=OFF -DBUILD_TESTING=OFF -DCPACK_DEBIAN_PACKAGE_MAINTAINER=Zynthian -DCPACK_DEBIAN_PACKAGE_NAME=libsndfile1-zyndev -DCPACK_DEBIAN_PACKAGE_DESCRIPTION="libsndfile1-dev and libsndfile1 with Zynthian patches" ..')
system('cmake --build .')
system('cpack -G DEB')
deb_files = glob("libsndfile-*-Linux.deb")
for fn1 in deb_files:
    fn2 = fn1.replace("Linux", f"zynthian-{arch}")
    rename(fn1, fn2)

