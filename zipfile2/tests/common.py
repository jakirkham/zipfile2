import os.path


HERE = os.path.dirname(__file__)

NOSE_EGG = os.path.join(HERE, "data", "nose.egg")
VTK_EGG = os.path.join(HERE, "data", "vtk.egg")
ZIP_WITH_SOFTLINK = os.path.join(HERE, "data", "zip_with_softlink.zip")

NOSE_SPEC_DEPEND = """\
metadata_version = '1.1'
name = 'nose'
version = '1.3.0'
build = 2

arch = 'amd64'
platform = 'darwin'
osdist = None
python = '2.7'
packages = []
"""