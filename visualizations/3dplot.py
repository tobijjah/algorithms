"""
Visualizes bivariate normal distribution in blender
"""
import bpy
import numpy as np
from bisect import bisect_left
from matplotlib.mlab import bivariate_normal

# mean an standard deviation of X and Y sample population
mu_x = 7.5
sigma_x = 2.5

mu_y = 7.5
sigma_y = 2.5

x_interval = np.linspace(0, 15, 16)
y_interval = np.linspace(-0, 15, 16)

X, Y = np.meshgrid(x_interval, y_interval)
Z = bivariate_normal(X, Y, sigma_x, sigma_y, mu_x, mu_y)
Z = np.round(Z * 1000, 3)  # probability densities under pdf never > 1, just move the decimal dot to get a greater Z

# 4 class histogram colorization, next time use quartiles with np.percentile
_, bins = np.histogram(Z, bins=4)

color_definitions = [
    ('ligthgray', (.871, .871, .871)),
    ('blue1', (.342, .591, .753)),
    ('blue2', (.147, .423, .672)),
    ('blue3', (.015, .165, .462)),
    ('blue4', (.002, .082, .332)),
]

# create materials
for name, rgb in color_definitions:
    material = bpy.data.materials.new(name)
    material.diffuse_color = rgb

# create cubes
for rows in zip(X, Y, Z):
    xs, ys, zs = rows
    for coords in zip(xs, ys, zs):
        x, y, z = coords
        if z > 0:
            bpy.ops.mesh.primitive_cube_add(radius=.45, location=(x, y, 0))
            xd, yd, zd = bpy.context.object.dimensions
            bpy.context.object.dimensions = xd, yd, z
            bpy.context.object.delta_location = 0, 0, z/2

            material_name = color_definitions[bisect_left(bins, z)][0]
            material = bpy.data.materials[material_name]
            bpy.context.object.data.materials.append(material)

# add plane below the cubes
bpy.ops.mesh.primitive_cube_add(location=(np.median(x_interval), np.median(y_interval), 0))
bpy.context.object.dimensions = (
    abs(np.max(x_interval)-np.min(x_interval))+2,
    abs(np.max(y_interval)-np.min(y_interval))+2,
    .2
)
bpy.context.object.delta_location = 0, 0, -.1
bpy.context.object.data.materials.append(bpy.data.materials['ligthgray'])