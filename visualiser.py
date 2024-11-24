import numpy as np
import pyvista as pv
import multivector as mv

ORIGIN = np.array([0,0,0])

pl = pv.Plotter()
pl.window_size = (2000,1500)
# axis = pv.Axes(show_actor=True)
# pl.add_mesh(axis)
MAX_COORD = 0


def add(arr):

    for vec in arr:
        global MAX_COORD
        if vec.components[0] or vec.components[3] or vec.components[5:].any():
            raise ValueError("Input object not a vector.")
        # Extract the direction vector components
        direction = np.array([vec.components[1], vec.components[2], vec.components[4]])

        for i in direction:
            if i > MAX_COORD:
                MAX_COORD = i
        
        # Create and add the arrow to the plotter
        arrow = pv.Arrow(ORIGIN, direction, tip_radius=0.08, tip_length=0.3, shaft_radius=0.02)
        actor = pl.add_mesh(arrow)
    # pl.show()


def show():
    gridsize = MAX_COORD
    print(MAX_COORD)

    x_axis = pv.Line(ORIGIN - np.array([gridsize, 0, 0]), ORIGIN + np.array([gridsize, 0, 0]))
    y_axis = pv.Line(ORIGIN - np.array([0, gridsize, 0]), ORIGIN + np.array([0, gridsize, 0]))
    z_axis = pv.Line(ORIGIN - np.array([0, 0, gridsize]), ORIGIN + np.array([0, 0, gridsize]))
    pl.add_mesh(x_axis, color='grey', line_width=3)
    pl.add_mesh(y_axis, color='grey', line_width=3)
    pl.add_mesh(z_axis, color='grey', line_width=3)

    pl.add_point_labels([ORIGIN + np.array([gridsize + 0.3, 0, 0]),
                        ORIGIN + np.array([0, gridsize + 0.3, 0]),
                        ORIGIN + np.array([0, 0, gridsize + 0.3])],
                        ["X", "Y", "Z"], 
                        font_size=32,
                        text_color="black",
                        point_color="white",
                        point_size=0,
                        fill_shape=False,
                        shape_opacity=0,
                        justification_horizontal="center",
                        justification_vertical="center")

    # Set the camera position for a 3D perspective
    camera_position = [
        (gridsize*3, gridsize*3, gridsize*3),  # Camera location
        (0, 0, 0),     # Focal point (looking at the origin)
        (0, 0, 1),     # View up direction (Z-axis up)
    ]
    pl.camera_position = camera_position

    grid = pv.Plane(center=ORIGIN, direction=(0, 0, 1), i_size=MAX_COORD*2, j_size=MAX_COORD*2)
    pl.add_mesh(grid, color="lightgrey", style="wireframe", line_width=0.5)

    pl.show()

