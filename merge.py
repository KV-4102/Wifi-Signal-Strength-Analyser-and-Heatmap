import tkinter as tk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.contour import ContourSet

# Define the file path of the CSV file
file_path = "C:\\Users\\ASUS\\PycharmProjects\\WNFWIFIANALYSIS\\signal_strengthmain.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Create a new tkinter window
root = tk.Tk()
root.geometry("800x800")

# Create a matplotlib figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111)

# Create a heatmap of the signal strengths using seaborn
heatmap = sns.kdeplot(x=df['Distance'], y=df['Signal Strength'], cmap="viridis", fill=True, thresh=0.05, ax=ax)

# Remove the colorbar
if isinstance(heatmap, ContourSet):
    cbar = fig.colorbar(heatmap.collections[0])
    cbar.remove()

# Create a tkinter canvas to display the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Define a function to create the rectangle on the canvas
def create_rectangle():
    # Get the dimensions of the canvas
    canvas_width = canvas.get_tk_widget().winfo_width()
    canvas_height = canvas.get_tk_widget().winfo_height()

    # Calculate the position and size of the rectangle
    rect_size = 400
    rect_x = (canvas_width - rect_size) / 2
    rect_y = (canvas_height - rect_size) / 2

    # Draw the rectangle on the canvas
    canvas.get_tk_widget().create_rectangle(rect_x, rect_y, rect_x + rect_size, rect_y + rect_size, outline="black")

# Call the function to create the rectangle after the canvas has been packed
canvas.get_tk_widget().after(100, create_rectangle)

# Save the heatmap as an image file when the "Save" button is clicked
def save_heatmap():
    fig.savefig('signal_strength_heatmap.png')
    print("Heatmap saved as signal_strength_heatmap.png")

# Create a "Save" button to save the heatmap as an image file
save_button = tk.Button(root, text="Save", command=save_heatmap)
save_button.pack()

# Start the tkinter main loop
root.mainloop()
