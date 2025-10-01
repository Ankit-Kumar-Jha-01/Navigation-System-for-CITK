import tkinter as tk
from tkinter import PhotoImage
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image

root = tk.Tk()
root.title("Image in Tkinter")

image = tk.PhotoImage(file="project_img.png") 

image_label = tk.Label(root, image=image)
image_label.pack()

root.mainloop()

def plot_network_graph():
    G = nx.Graph()
   
    G.add_edge("1","3",weight=4)
    G.add_edge("3","4",weight=4)
    G.add_edge("2","4",weight=4)
    G.add_edge("3","5",weight=4)
    G.add_edge("5","7",weight=4)
    G.add_edge("4","6",weight=4)
    G.add_edge("5","6",weight=4)
    G.add_edge("6","12",weight=4)
    G.add_edge("11","12",weight=4)
    G.add_edge("10","11",weight=4)
    G.add_edge("9","10",weight=4)
    G.add_edge("8","9",weight=4)
    G.add_edge("4","2",weight=4)
    G.add_edge("8","13",weight=4)
    G.add_edge("13","14",weight=4)
    G.add_edge("14","15",weight=4)
    G.add_edge("15","16",weight=4)
    G.add_edge("15","22",weight=4)
    G.add_edge("16","17",weight=4)
    G.add_edge("17","18",weight=4)
    G.add_edge("18","19",weight=4)
    G.add_edge("19","20",weight=4)
    G.add_edge("20","21",weight=4)
    G.add_edge("21","22",weight=4)
    G.add_edge("7","24",weight=4)
    G.add_edge("24","23",weight=4)
    G.add_edge("4","25",weight=4)
    G.add_edge("3","26",weight=4)
    G.add_edge("26","27",weight=4)
    G.add_edge("27","28",weight=4)
    G.add_edge("28","29",weight=4)
    G.add_edge("29","30",weight=4)
    G.add_edge("30","31",weight=4)
    G.add_edge("31","32",weight=4)
    G.add_edge("32","33",weight=4)
    G.add_edge("33","34",weight=4)
    G.add_edge("34","35",weight=4)
    G.add_edge("35","36",weight=4)
    G.add_edge("36","37",weight=4)
    G.add_edge("38","39",weight=4)
    G.add_edge("39","40",weight=4)
    G.add_edge("39","22",weight=4)
    G.add_edge("12","41",weight=4)
    G.add_edge("41","42",weight=4)
    G.add_edge("41","50",weight=4)
    G.add_edge("50","49",weight=4)
    G.add_edge("49","48",weight=4)
    G.add_edge("42","43",weight=4)
    G.add_edge("43","44",weight=4)
    G.add_edge("44","45",weight=4)
    G.add_edge("45","48",weight=4)
    G.add_edge("45","46",weight=4)
    G.add_edge("46","47",weight=4)
    G.add_edge("47","9",weight=4)
    G.add_edge("43","50",weight=4)

    current_location = current_location_entry.get()
    destination = destination_entry.get()

    try:
        shortest_path = nx.shortest_path(G, source=current_location, target=destination, weight="weight")
        shortest_path_length = nx.shortest_path_length(G, source=current_location, target=destination, weight="weight")

        node_positions = {
            "1": (-102.6, -94.2),
            "3": (-103.1, -69.5),
            "5": (-103.1, -52.7),
            "7": (-103.1, -8.8),
            "8": (-103.1, 39.8),
            "13": (-103.1, 56.1),
            "14": (-91.4, 65.5),
            "15": (-50.8, 65.5),
            "22": (19.2, 65.5),
            "17": (-52.2, 116.8),
            "18": (-33.1, 128),
            "19": (-15.8, 138.3),
            "20": (2.4, 129.9),
            "21": (17.8, 122),
            "22": (19.2, 65.9),
            "9": (-129.3, 38.9),
            "10": (-129.3, 12.2),
            "11": (-129.3, -14.8),
            "12": (-129.3, -26.5),
            "6": (-129.3, -53.1),
            "4": (-129.3, -69.9),
            "25": (-158.8, -70.8),
            "2":(-129.4, -94),
            "16":(-51.2, 80.9),
            "23":(-103, 28.1),
            "24":(-103, 5.2),
            "26": (-72.6, -70.8),
            "27": (-23, -70.8),
            "28": (0.5, -70.8),
            "29": (7, -77.9),
            "30": (47.1, -71.3),
            "31": (61.1, -61.8),
            "32": (76.7, -59.3),
            "33": (76.7, -23.8),
            "34": (70.6, -14.7),
            "35": (72.1, 3.8),
            "36": (78.2, 9.3),
            "37": (80.2, 56.4),
            "38": (50.6, 57.4),
            "39": (50.6, 65.4),
            "40": (83.2, 65.4),
            "41": (-195.3, -25.8),
            "42": (-233.3, -25.8),
            "43": (-233.3, -9.2),
            "44": (-232.9, 38.8),
            "45": (-193.8, 38.8),
            "46": (-172.3, 40.3),
            "47": (-145.7, 39.8),
            "48": (-194.3, 30.8),
            "49": (-193.8, 1.3),
            "50": (-194.8, -9.2)
    
        }
        
        fig, ax = plt.subplots()

        background_image = Image.open("project_img.png")  
        
        ax.imshow(background_image,extent=[-350,200,-100,170]) 

        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_nodes(G, pos=node_positions, nodelist=shortest_path, node_color='green', node_size=30)
        nx.draw_networkx_edges(G, pos=node_positions, edgelist=path_edges, edge_color='darkblue', width=5)

        plt.axis('off') 
        plt.show()

        print("Shortest path:", shortest_path)
        print("Shortest path length:", shortest_path_length)
    except nx.NetworkXNoPath:
        print("No path found between the locations.")
    except nx.NodeNotFound:
        print("One or both of the locations are not in the graph.")

root = tk.Tk()
root.title("Network Graph with Background Image")

current_location_label = tk.Label(root, text="Enter your current location in no:")
current_location_label.pack()
current_location_entry = tk.Entry(root)
current_location_entry.pack()

destination_label = tk.Label(root, text="Enter your destination in no:")
destination_label.pack()
destination_entry = tk.Entry(root)
destination_entry.pack()

plot_button = tk.Button(root, text="Plot Network Graph", command=plot_network_graph)
plot_button.pack()
 
root.mainloop()