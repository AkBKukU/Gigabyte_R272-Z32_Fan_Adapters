#!/usr/bin/python3
from solid2 import *

spacing=4.1
drive_width=21-(spacing*2)
offset = drive_width + spacing

set_global_fn(72)

drive_tray = cube(drive_width,4,77)

fan_block = drive_tray.left(0) + drive_tray.right(offset) + drive_tray.right(offset*2) + drive_tray.right(offset*3) + cube((drive_width*4+spacing*3)-2,4,70).right(1).up(3.5)

fan_hole = rotate(90, 0, 0)(cylinder(20,30,30))

difference()(fan_block - fan_hole.right((drive_width*4+spacing*3)/2).up(77/2).forward(10)).save_as_scad()
