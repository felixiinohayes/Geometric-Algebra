import numpy as np
import pyvista as pv
import multivector as mv

ORIGIN = np.array([0,0,0])
MAX_COORD = 0
NUM_VECS = 0

class Scene:
    def __init__(self):
        self.pl = pv.Plotter()
        self.pl.window_size = (2000,1500)

    def plot(self,vec):
        global MAX_COORD
        MAX_COORD = max(vec.components)
        if vec.components[1] or vec.components[2] or vec.components[4]:
            self.plot_vector([vec.components[1], vec.components[2], vec.components[4]])
        if vec.components[3] or vec.components[5] or vec.components[6]:
            print(vec.components)
            self.plot_bivector([vec.components[3], vec.components[5], vec.components[6]])

        # pl.show()

    def plot_vector(self, coords):
        global MAX_COORD
        # Extract the direction and magnitude of vector
        direction = np.array(coords)
        magnitude = np.linalg.norm(coords)
        
        line = pv.Line(ORIGIN, coords)
        end = pv.Sphere(radius=0.04, center=coords)
        self.pl.add_mesh(line, color='red', line_width=5)
        self.pl.add_mesh(end, color='red')
        self.pl.add_text(str(coords), position=[40, 10 + 50*NUM_VECS])
        self.pl.add_point_labels(
        [coords],   # Position of the label
        [f"({float(coords[0])}, {float(coords[1])}, {float(coords[2])})"],    # Label text
        font_size=20,
        text_color="black",
        point_color="white",
        point_size=10,
        fill_shape=False,
        shape_opacity=0,)

    def plot_bivector(self, coords):
        a12, a13, a23 = coords

        plane_vectors = {
            'e12': (np.array([1, 0, 0]), np.array([0, 1, 0]), a12),
            'e13': (np.array([1, 0, 0]), np.array([0, 0, 1]), a13),
            'e23': (np.array([0, 1, 0]), np.array([0, 0, 1]), a23),
        }

        for key, (v1, v2, magnitude) in plane_vectors.items():
            corners = np.array([
                ORIGIN,
                ORIGIN + magnitude * v1,
                ORIGIN + magnitude * (v1 + v2),
                ORIGIN + magnitude * v2
            ])
            faces = [[4, 0, 1, 2, 3]]  # Define the parallelogram face

            parallelogram = pv.PolyData(corners, faces)
            color = 'blue' if magnitude > 0 else 'orange'  # Positive or negative magnitude
            self.pl.add_mesh(parallelogram, color=color, opacity=0.6)


    def show(self):
        gridsize = MAX_COORD*2

        x_axis = pv.Line(ORIGIN - np.array([gridsize, 0, 0]), ORIGIN + np.array([gridsize, 0, 0]))
        y_axis = pv.Line(ORIGIN - np.array([0, gridsize, 0]), ORIGIN + np.array([0, gridsize, 0]))
        z_axis = pv.Line(ORIGIN - np.array([0, 0, gridsize]), ORIGIN + np.array([0, 0, gridsize]))
        self.pl.add_mesh(x_axis, color='grey', line_width=3)
        self.pl.add_mesh(y_axis, color='grey', line_width=3)
        self.pl.add_mesh(z_axis, color='grey', line_width=3)

        self.pl.add_point_labels([ORIGIN + np.array([gridsize + 0.3, 0, 0]),
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
            (gridsize*2, gridsize*2, gridsize*2),  # Camera location
            (0, 0, 0),     # Focal point (looking at the origin)
            (0, 0, 1),     # View up direction (Z-axis up)
        ]
        self.pl.camera_position = camera_position

        grid = pv.Plane(center=ORIGIN, direction=(0, 0, 1), i_size=gridsize*2, j_size=gridsize*2)
        self.pl.add_mesh(grid, color="lightgrey", style="wireframe", line_width=0.5)

        self.pl.show()

