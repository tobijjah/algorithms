import bpy
from sklearn.datasets import make_blobs


def create_dots(X, Y, materials, size=0.1):
    for coords, label in zip(X, Y):
        x, y, z = coords

        bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, z), size=size)
        dot = bpy.context.object

        dot.data.materials.append(materials[label])


def create_hyperplane(name, weights, bias, x_min, x_max, y_min, y_max):
    z_min = -(x_min*weights[0])/weights[2] - (y_min*weights[1])/weights[2] - bias
    z_max = -(x_max*weights[0])/weights[2] - (y_max*weights[1])/weights[2] - bias

    vertices = [
        (x_min, y_min, z_min),
        (x_max, y_min, z_max),
        (x_max, y_max, z_max),
        (x_min, y_max, z_min),
    ]
    faces = [(0, 1, 2, 3)]

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.objects.link(obj)

    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)

    return obj


if __name__ == '__main__':
    X, Y = make_blobs(n_samples=60, n_features=3, centers=2)

    red = bpy.data.materials.new('red')
    red.diffuse_color = 1., 0., 0.
    blue = bpy.data.materials.new('blue')
    blue.diffuse_color = 0., 0., 1.

    create_dots(Y, X, [red, blue])
