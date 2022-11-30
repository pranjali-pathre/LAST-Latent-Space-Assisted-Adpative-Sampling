import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import numpy as np
import numpy as np
import matplotlib.animation as animation
import base64

def render_mol(protein):
    view = py3Dmol.view(width=400,height=500)
    view.setBackgroundColor('white')
    print(protein)
    view.addModel(protein,'pdb')
    view.setStyle({"stick" : {}})

    view.zoomTo()
    showmol(view, height = 800,width=1000)

uploaded_itr = st.number_input("Iterations", 0, 30)
uploaded_pat = st.number_input("Patience", 0, 10)
uploaded_pdb = st.sidebar.file_uploader("Choose protein .pdb file")
uploaded_top = st.sidebar.file_uploader("Choose protein .prmtop file")
uploaded_inp = st.sidebar.file_uploader("Choose protein .inpcrd file")

res1 = None
res2 = None
res3 = None

if(uploaded_pdb is not None):
    pdb = {"file": uploaded_pdb.getvalue()}
    pdb_vis = pdb["file"].decode("utf-8")
    res1 = requests.post(f"http://localhost:1016/uploadpdb/", files=pdb)

if(uploaded_top is not None):
    top = {"file": uploaded_top.getvalue()}
    res2 = requests.post(f"http://localhost:1016/uploadtop/", files=top)

if(uploaded_inp is not None):
    inp = {"file": uploaded_inp.getvalue()}
    res3 = requests.post(f"http://localhost:1016/uploadinp/", files=inp)

if(res1 is not None and res2 is not None and res3 is not None):
    tab1, tab2 = st.tabs(["Molecule", "Latent Space"])

    with tab1:
        st.header("Input Molecule")
        render_mol(pdb_vis)

    with tab2:
        st.header("Latent Space Visualization over iterations")
        res = requests.post(f"http://localhost:1016/run/")
        print(res)
        coords_list = res.json().get("response")
        print(len(coords_list))
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        data_all = []
        for nn in range(0, len(coords_list)):
            data_all.append(np.array(coords_list[nn]))
        fig, ax = plt.subplots()
        marker_size = 10
        def animate(i):
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_title("Iteration " + str(i+1))
            s = ax.scatter(data_all[i][:, 0], data_all[i][:, 1], s=marker_size)
        plt.grid(b=None)
        ani = animation.FuncAnimation(fig, animate, interval=1000, frames=range(4))
        ani.save('animation.gif', writer='pillow')
        file_ = open("animation.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src = "data:image/gif;base64,{data_url}" alt="Latent Space">',
            unsafe_allow_html=True,
        )