import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file path of the CSV file
file_path = "C:\\Users\\ASUS\\PycharmProjects\\WNFWIFIANALYSIS\\signal_strengthmain.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Create a circular heatmap of the signal strengths
sns.set_theme()
sns.set(rc={'figure.figsize':(12,10)})
sns.jointplot(x=df['Distance'], y=df['Signal Strength'], kind="hex", cmap="YlGnBu")

# Save the circular heatmap as an image file
plt.savefig('circular_signal_strength_heatmap.png')

# Display the circular heatmap
plt.show()
