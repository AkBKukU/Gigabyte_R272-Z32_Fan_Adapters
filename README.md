# Gigabyte_R272-Z32_Fan_Adapters


![The fan brackets](doc/ServerFans.jpg "A photo of fans installed in the server")

These are two fan adapters for installing standard sized 80mm and 60mm fans in a 2U Gigabyte R272-Z32 server. These should also be compatible with other servers in the right circumstances.

The design files are written in SolidPython2 using BOSL2 for OpenSCAD. To use them:

1. Install the python dependencies with `pip` an install OpenSCAD
2. Run the py files to generate SCAD files
3. Open the files in OpenSCAD
4. Press F6 to create a solid model and then export it as an STL.

You are now ready to slice and print the files!

## fan-wall

This is a simple plate that adapts an 80x80x25mm fan to fit in the space of the original 80x80x38mm fans with the slide rails. It is setup assuming you are going to route the fan cables through the existing metal grills due to the originals having a custom cable solution.

## drive-bay

These are additional fan mounts that can be installed in the front of the server to add 60x60x25mm fans. These are installed in the U.2 drive bays but *do not* protrude into the space where the drives fit. If you don't use the original sleds to mount the drives you can have the drives behind the fans.

This project was made possible by [Noctua](https://noctua.at/) by providing the fans used.