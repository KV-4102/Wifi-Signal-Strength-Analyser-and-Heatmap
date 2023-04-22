import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file path of the CSV file
file_path = "C:\\Users\\ASUS\\PycharmProjects\\WNFWIFIANALYSIS\\signal_strengthmain.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Create a heatmap of the signal strengths
sns.set_theme()
sns.set(rc={'figure.figsize':(12,10)})
sns.kdeplot(x=df['Distance'], y=df['Signal Strength'], cmap="viridis", shade=True, thresh=0.05)

# Save the heatmap as an image file
plt.savefig('signal_strength_heatmap.png')
plt.show()
