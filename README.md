# Release snapshot of GAMer

GAMer is a surface mesh improvement library,tetrahedral mesh generation library
and Blender addon, included in the FEtk software umbrella. It depends on Maloc
a Minimal Abstraction Layer for Object-oriented C, which all modules in FEtk
depends on.  Maloc is provided in this snapshot.


## Installation

These installation instructions should work on any UNIX based platform.

Requirements: Installation requires python-3.4 with NumPy, swig-2.0.7 or later, and Blender-2.76b or later.

Edit the top level makefile adjust the following lines depending on your UNIX
platform:


On Linux or similar UNIX:

  # On a Linux platform, uncomment these lines and adjust as needed:
  export PYTHON := /opt/python3.4/bin/python3.4
  export LD_LIBRARY_PATH := $(BUILD_DIR)/lib:$(LD_LIBRARY_PATH)
  LDFLAGS := "-L/opt/python3.4/lib"
  INSTALL_DIR := ~/.config/blender/2.76


On MacOSX:

  # On a MacOSX platform, uncomment these lines and adjust as needed:
  export PYTHON := /opt/local/bin/python3.4
  export DYLD_LIBRARY_PATH := $(BUILD_DIR)/lib:$(DYLD_LIBRARY_PATH)
  LDFLAGS := -L/opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib
  INSTALL_DIR := ~/Library/Application\ Support/Blender/2.76


After these changes you are ready to build and install GAMer:

    make
    make install



### GAMer libraries and applications

The GAMer applications ImproveSurfMesh, MolecularMesh, and GenerateMesh are
built in the directory gamer_build_static/bin.  These applications reference
the GAMer libraries in gamer_build_static/lib.


## PyGAMer

PyGAMer is a Python wrapper of the core GAMer library. The gamer python module
is built in gamer_build_static/lib/python3.4/site-packages/gamer

Make sure to set LD_LIBRARY_PATH or (DYLD_LIBRARY_PATH on Mac) and
PYTHONPATH before you run any programs or try using PyGAMer

    export BUILD_DIR=your_path_to/gamer_build_static
    export LD_LIBRARY_PATH=$BUILD_DIR/lib:$LD_LIBRARY_PATH
    export PYTHONPATH=$BUILD_DIR/lib/python2.6/site-packages:$PYTHONPATH

On Mac:

    export BUILD_DIR=your_path_to/gamer_build_static
    export DYLD_LIBRARY_PATH=$BUILD_DIR/lib:$DYLD_LIBRARY_PATH
    export PYTHONPATH=$BUILD_DIR/lib/python3.4/site-packages:$PYTHONPATH


To test the main functionality you can run the test script in gamer/swig/test.

    cd gamer/swig/test
    python gamer_test.py


## Blender addon

A Blender addon for GAMer is provided in the gamer_addon subdirectory.
