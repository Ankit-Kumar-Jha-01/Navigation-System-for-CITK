<div align="center">

# 🧭 Campus/Facility Navigation System

### A graph-based shortest-path navigator with a Tkinter GUI and image-overlaid visualization

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Algorithms-orange?style=for-the-badge)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-yellowgreen?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-7B68EE?style=for-the-badge)](https://python-pillow.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

</div>

---

## 📖 Overview

This project is a **desktop navigation tool** that finds the shortest route between two points on a fixed map (e.g. a campus, building, or facility floor plan) and displays it visually on top of the map image.

- The map is modeled as a **weighted graph** using `networkx`, where each node is a location/junction number and each edge is a walkable path.
- The user enters a **start node** and a **destination node** through a simple **Tkinter GUI**.
- **Dijkstra's algorithm** (`nx.shortest_path`) computes the shortest route.
- The route is drawn with `matplotlib`, overlaid on the real map image (`project_img.png`) so the path is easy to follow visually.

> 💡 Think of it as a lightweight, offline "Google Maps" for a single custom location.

---

## ⚙️ Requirements

| Package | Purpose |
|---|---|
| `tkinter` | GUI window, input fields, and button |
| `networkx` | Graph construction and shortest-path computation |
| `matplotlib` | Plotting the graph/route over the background image |
| `Pillow` (`PIL`) | Loading the background map image |

Install everything with:

```bash
pip install networkx matplotlib pillow
```

> `tkinter` ships with most standard Python installations. On Linux, if it's missing, install it via `sudo apt-get install python3-tk`.

---

## 🗂️ Project Structure

```
navigation-system/
├── Navigation_system.py     # Main application script
├── campus_img.png            # Background map image (required, same folder as script)
└── README.md                 # Project documentation
```

> ⚠️ `campus_img.png` must exist in the same directory as the script — it's used both as the GUI icon image and as the background for the route plot.

---

## 🗺️ Data

<div align="center">

### Campus Map — `campus_img.png`

![Campus Map](https://raw.githubusercontent.com/Ankit-Kumar-Jha-01/Navigation-System-for-CITK/main/campus_img.png)

*[View on GitHub](https://github.com/Ankit-Kumar-Jha-01/Navigation-System-for-CITK/blob/main/campus_img.png)*

</div>

This is the background image used for the GUI and for plotting routes. Every node's `(x, y)` coordinate in `node_positions` is aligned to a real spot on this map.

The "map" itself is hand-coded as a set of **50 nodes** (numbered `1`–`50`) connected by **weighted edges**, defined directly inside `plot_network_graph()`:

```python
G.add_edge("1", "3", weight=4)
G.add_edge("3", "4", weight=4)
...
```

- Each node also has a fixed **(x, y) pixel coordinate** in the `node_positions` dictionary, aligning it with the corresponding spot on `project_img.png`.
- All edges currently share the same weight (`4`), so the "shortest path" is effectively the path with the **fewest hops**. Weights can be customized per edge to reflect real distances.

---

## 🚀 Installation

1. **Clone or download** the project files.
2. Place your map image in the project folder and name it `campus_img.png`.
3. Install dependencies:
   ```bash
   pip install networkx matplotlib pillow
   ```
4. Run the script:
   ```bash
   python Navigation_system.py
   ```

---

## 🧩 Project Methodology

1. **Graph Modeling** — The physical layout is abstracted into a graph: junctions/rooms become nodes, and walkable connections between them become weighted edges.
2. **User Input** — A Tkinter form collects the current location and destination as node numbers.
3. **Pathfinding** — `networkx.shortest_path()` runs Dijkstra's algorithm on the weighted graph to compute the optimal route and its total length.
4. **Error Handling** — The app gracefully handles:
   - `NetworkXNoPath` — no route exists between the two nodes
   - `NodeNotFound` — an entered node number doesn't exist in the graph
5. **Rendering** — The resulting path's nodes and edges are drawn in a distinct color (`green` nodes, `darkblue` edges) directly on top of the map image using `matplotlib.imshow()` + `networkx.draw_networkx_*`.

---

## 📊 Visualization

- The full map image is loaded as the plot background via `ax.imshow(background_image, extent=[...])`, aligning pixel coordinates with node positions.
- Only the nodes/edges belonging to the **shortest path** are highlighted, keeping the visualization clean and easy to read.
- Axes are hidden (`plt.axis('off')`) for a clean, map-like presentation.
- The computed path and its length are also printed to the console for quick reference.

<div align="center">

<table>
<tr>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/Ankit-Kumar-Jha-01/Navigation-System-for-CITK/main/visualization-images/location%20of%20current%20and%20destination.png" width="100%"><br>
<sub><b>Location Input</b><br>Current location and destination are entered as node numbers, not place names — string-based location search is planned for a future version.</sub>
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/Ankit-Kumar-Jha-01/Navigation-System-for-CITK/main/visualization-images/route%20theory.png" width="100%"><br>
<sub><b>Route Computation</b><br>Console output of the computed shortest path — the sequence of visited nodes and the total path length.</sub>
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/Ankit-Kumar-Jha-01/Navigation-System-for-CITK/main/visualization-images/route%20visualization.png" width="100%"><br>
<sub><b>Route on Map</b><br>The shortest path rendered visually on the campus map, tracing the route from current location to destination.</sub>
</td>
</tr>
</table>

</div>

---

## 🛠️ Technology Used

- **Python** — core language
- **Tkinter** — GUI (input fields, button, image display)
- **NetworkX** — graph representation and shortest-path algorithm
- **Matplotlib** — path/route visualization
- **Pillow (PIL)** — image loading for the map background

---

## 🔮 Future Improvements

- [ ] Fix the duplicate `root = tk.Tk()` / `root.mainloop()` calls so the app runs as a single cohesive window instead of two separate ones.
- [ ] Load node/edge data from an external file (JSON/CSV) instead of hardcoding it, for easier map updates.
- [ ] Add a dropdown or map-click interface instead of manual node-number entry.
- [ ] Support real-world distances/weights (e.g. meters) for more accurate routing.
- [ ] Add multiple route options (alternate paths, fastest vs. shortest).
- [ ] Package as a standalone executable (PyInstaller) for easier distribution.
- [ ] Add unit tests for pathfinding logic.
- [ ] Migrate to a modern GUI framework (e.g. PyQt, Kivy) or a web-based interface (Flask/Streamlit) for richer interactivity.

---

<div align="center">

Made with 🧭 and Python

</div>
