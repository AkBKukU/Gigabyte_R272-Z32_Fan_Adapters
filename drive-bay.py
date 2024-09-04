#!/usr/bin/python3
from solid2 import *
from solid2.extensions.bosl2 import arc_copies, ellipse

spacing=5.1
drive_width=11.8
drive_height=77
offset = drive_width + spacing
full_width = (drive_width * 4 + spacing * 3)
thickness=20
fan_mount_wall=3
tab_width=3
tab_depth=2
tab_len=6
tab_bottom_inset=6
tab_top_inset=15
tab_top_len=3

fan_size = 60
fan_mount_pitch = 50

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



def fan_cover(radius=63,depth=10,thick=3,legs=6):

        support = rotate(90, 0, 0)(intersection()(cylinder(thick,depth,depth)-cylinder(thick+2,depth-thick,depth-thick).down(1),cube(depth*2).down(1)).down(thick/2) )
        cap = cylinder(thick,radius-depth,radius-depth)-cylinder(thick+2,radius-depth-thick,radius-depth-thick).down(1)
        return arc_copies(legs,radius-depth)(support)+cap.up(depth-thick)

def drive_slots(drives=4):
    plate = cube((drive_width*drives+spacing*drives),thickness,drive_height-spacing).left(spacing/2).up(spacing/2)
    for i in range(0,drives):
        plate += drive_tray.right(offset*i)
    return plate


def drive_latch_front(drives=4):
    plate = cube((drive_width*drives+spacing*drives),thickness,drive_height).left(spacing/2)

    #Bottom tabs
    for i in range(0,drives):
        plate += cube([tab_width,tab_len,tab_depth*2]).right((drive_width/2-tab_width/2)+(offset*i)).down(tab_depth).forward(tab_bottom_inset)

    #Bottom tabs Holes
    for i in range(0,drives):
        plate -= cube([spacing,thickness,spacing*2]).right((drive_width/2-spacing/2)+(offset*i)).down(spacing).forward(tab_bottom_inset+tab_len)

    #Top tabs
    for i in range(0,drives-1):
        plate += cube([tab_width,tab_top_len,tab_depth*2]).right((drive_width+spacing/2-tab_width/2)+(offset*i)).forward(tab_top_inset).up(drive_height-tab_depth*1.25)

    #Top tabs Holes
    for i in range(0,drives+2):
        plate -= cube([spacing,thickness,spacing*2]).right((-spacing)+(offset*i)).forward(tab_top_inset+tab_top_len).up(drive_height-spacing)
    return plate

difference()(
    drive_latch_front() -
    (rotate(90, 0, 0)(fan_mount(fan_size,fan_mount_pitch)).right(full_width/2).up(drive_height/2).forward(fan_mount_wall) ) +
    rotate(90, 0, 0)(fan_cover(radius=33,depth=15,thick=3,legs=6)).right(full_width/2).up(drive_height/2)
).save_as_scad()
