#!/usr/bin/python3
from solid2 import *
from solid2.extensions.bosl2 import arc_copies, ellipse

spacing=5.1
drive_width=11.8
drive_height=77
offset = drive_width + spacing
full_width = (drive_width * 4 + spacing * 3)

set_global_fn(72)

drive_tray = cube(drive_width,4,drive_height)

fan_block = (
        cube((drive_width*4+spacing*4),4,70).left(spacing/2).up(3.5) +
        drive_tray.left(0) +
        drive_tray.right(offset) +
        drive_tray.right(offset*2) +
        drive_tray.right(offset*3)
)

print("Len: "+str(drive_width * 4 + spacing * 3))

def fan_mount(d=80,p=71.5):
        fan_depth = 25
        mount_hole=4.5/2
        mount_pitch=p/2
        fan_radius = d/2
        fan_hole = (cylinder(fan_depth*2,fan_radius,fan_radius))
        return (
                fan_hole +
                cylinder(fan_depth*2,mount_hole,mount_hole).right(mount_pitch).forward(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).left(mount_pitch).forward(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).right(mount_pitch).back(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).left(mount_pitch).back(mount_pitch)
        )


#

def fan_cover(radius=63,depth=10,thick=3,legs=6):

        support = rotate(90, 0, 0)(intersection()(cylinder(thick,depth,depth)-cylinder(thick+2,depth-thick,depth-thick).down(1),cube(depth*2).down(1)).down(thick/2) )
        cap = cylinder(thick,radius-depth,radius-depth)-cylinder(thick+2,radius-depth-thick,radius-depth-thick).down(1)
        return arc_copies(legs,radius-depth)(support)+cap.up(depth-thick)

difference()(fan_block - (rotate(90, 0, 0)(fan_mount(60,50)).right(full_width/2).up(drive_height/2).forward(10) ) +
             rotate(90, 0, 0)(fan_cover(radius=33,depth=15,thick=3,legs=6)).right(full_width/2).up(drive_height/2)
             ).save_as_scad()
