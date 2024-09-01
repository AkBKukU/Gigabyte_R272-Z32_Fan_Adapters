#!/usr/bin/python3
from solid2 import *
from solid2.extensions.bosl2 import arc_copies, ellipse

spacing=5.1
drive_width=11.8
drive_height=80
offset = drive_width + spacing
full_width = 83
fan_mount_wall=1
thickness=32+fan_mount_wall
tab_width=3
tab_depth=2
tab_len=8

fan_size = 80
fan_mount_pitch = 71.5

set_global_fn(72)

drive_tray = cube(drive_width,thickness,drive_height)

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
        mount_hole=5/2
        mount_pitch=p/2
        fan_radius = d/2
        fan_hole = (cylinder(fan_depth*2,fan_radius,fan_radius))
        fan_block = cube([d+2,d+2,fan_depth*4]).left(d/2+1).back(d/2+1).down(fan_depth*4-0.01)
        return (
                fan_hole +
                fan_block +
                cylinder(fan_depth*2,mount_hole,mount_hole).right(mount_pitch).forward(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).left(mount_pitch).forward(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).right(mount_pitch).back(mount_pitch) +
                cylinder(fan_depth*2,mount_hole,mount_hole).left(mount_pitch).back(mount_pitch)
        )




def fan_tray(drives=4):
    plate = cube(full_width,thickness,drive_height)

    return plate

difference()(
    fan_tray() -
    (rotate(90, 0, 0)(fan_mount(fan_size,fan_mount_pitch)).right(full_width/2).up(drive_height/2).forward(fan_mount_wall) )
).save_as_scad()
