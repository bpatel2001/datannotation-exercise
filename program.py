import pandas as pd
import numpy as np

#Reading in the data usig pandas with utf-8 encoding
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
tables = pd.read_html(url, encoding='utf-8')
df = tables[0]

# Set the first row as the column names instead of the auto-generated column names (0,1,2,3...)
df.columns = df.iloc[0] 
df = df[1:].reset_index(drop=True) 

# Convert the x and y coordinates to integers
df['x-coordinate'] = pd.to_numeric(df['x-coordinate'], errors='coerce').astype(int)
df['y-coordinate'] = pd.to_numeric(df['y-coordinate'], errors='coerce').astype(int)

# Get the maximum x and y coordinates
max_x = int(df['x-coordinate'].max())
max_y = int(df['y-coordinate'].max())

# Initialize an empty array with the maximum x and y coordinates, and fill with spaces
array = np.empty((max_y+1, max_x+1), dtype=object)  
array[:] = ' '  

# Creating a list of tuples containing the x and y coordinates, as well as the character.
coordinates_df = df[['x-coordinate', 'y-coordinate', 'Character']]
coordinates_list = list(df[['x-coordinate', 'y-coordinate', 'Character']].itertuples(index=False, name=None))

# Filling the array with the data from the list of tuples
for i in coordinates_list:
    # Need to flip the y-axis during assignment, since the data is bottom-left origin
    adjusted_y = max_y - i[1]  
    array[adjusted_y, i[0]] = i[2]

# Joining the 2D array into a single string
formatted_array = '\n'.join([''.join(row) for row in array])
print(formatted_array) 
