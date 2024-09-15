#!/usr/bin/python3
from solid2 import *
from solid2.extensions.bosl2 import arc_copies, ellipse

drive_width=11.8
drive_height=(76-70)/2
drive_len=100

wall=2

screw_inset=14
screw_edge=3 # To Center
screw_diameter=2.5
screw_pitch=76+(screw_diameter/2)

set_global_fn(12)


(
        cube([drive_width,drive_len,drive_height])+
        translate([screw_edge,screw_inset,drive_height])
                (sphere(d=screw_diameter))+
        translate([screw_edge,screw_inset+screw_pitch,drive_height])
                (sphere(d=screw_diameter))+
        translate([screw_edge,screw_inset,drive_height+1])
                (sphere(d=screw_diameter))+
        translate([screw_edge,screw_inset+screw_pitch,drive_height+1])
                (sphere(d=screw_diameter))-
        translate([drive_width/2,0,0])(
                rotate(0,0,45)(cube([15,15,50],center=True)))-
        translate([drive_width/2,screw_inset+screw_pitch/2,0])(
                (cube([drive_width-wall*2,screw_pitch-wall*4,50],center=True)))
).save_as_scad()
