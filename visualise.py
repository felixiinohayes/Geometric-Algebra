import numpy as np
import pyvista as pv
import multivector as mv
from pyvista import examples
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageWithDrawerLayout
from trame.widgets import vuetify3

pv.OFF_SCREEN = False
server = get_server()
state, ctrl = server.state, server.controller

pl = pv.Plotter()

@ctrl.add("add_bivector")
def add_bivector():
    vertices = np.array([
        [0,0,0],
        [1,0,0],
        [1,1,0],
        [0,1,0],
    ])
    faces = np.array([4,0,1,2,3])
    bivector = pv.PolyData(vertices, [faces])

    pl.add_mesh(bivector, color="cyan", opacity=0.7, edge_color="black", show_edges=True)
    
state.x = 2
state.y = 0
state.z = 0

vector_actor = None
@state.change("x", "y", "z")
def update_vector(x, y, z, **kwargs):
    global vector_actor
    if vector_actor:
        pl.remove_actor(vector_actor)
    vector_actor = pl.add_arrows(np.array([0,0,0]), np.array([x, y, z]), )


bivector = pv.PolyData()
pl.camera.focal_point = (0,0,0)

pl.add_arrows(np.array([0,0,0]), np.array([1,0,0]))
pl.add_arrows(np.array([0,0,0]), np.array([0,1,0]))
pl.add_arrows(np.array([0,0,0]), np.array([0,0,1]))
pl.show_axes()

update_vector(state.x, state.y, state.z)

with SinglePageWithDrawerLayout(server) as layout:
    layout.title.set_text("Geometric Algebra Visualisation")
    with layout.drawer:
        layout.toolbar.dense = True
        with vuetify3.VContainer(fluid=True, classes="pa-2 justify-center align-center"):
            vuetify3.VSlider(
                v_model=("x", 0),
                label="X",
                min=-10, max=10, step=1,
                classes="mb-3",
                style="height: 20px; margin-right: 20px"
            )
            vuetify3.VSlider(
                v_model=("y", 0),
                label="Y",
                min=-10, max=10, step=1,
                vertical=True,
                style="height: 120px; margin-right: 20px"

            )
            vuetify3.VSlider(
                v_model=("z", 0),
                label="Z",
                min=-10, max=10, step=1,
                vertical=True,
                style="height: 120px; margin-right: 20px"
            )
        with vuetify3.VContainer(fluid=True, classes="pa-1 d-flex justify-center align-center"):
            vuetify3.VBtn("Add Vector", click=ctrl.add_vector, color="primary")
    with layout.content:
        view = plotter_ui(pl)


server.start(open_browser=False)