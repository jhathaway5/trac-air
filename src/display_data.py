from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def display_aircraft_data(aircraft_data):
    """
    Display aircraft data in a readable format.

    Parameters:
    aircraft_data (list): List of aircraft states to display.
    """
    print("Listing detected aircraft:")
    for aircraft in aircraft_data:
        print(f"Aircraft {aircraft[0]} is at latitude {aircraft[6]} and longitude {aircraft[5]}")

def plot_aircraft_positions(aircraft_data, min_latitude, max_latitude, min_longitude, max_longitude):
    """
    Plot the positions of aircraft on a map and annotate them.

    Parameters:
    aircraft_data (list): List of aircraft states, where each state includes longitude and latitude.
    min_latitude (float): Minimum latitude (southern boundary).
    max_latitude (float): Maximum latitude (northern boundary).
    min_longitude (float): Minimum longitude (western boundary).
    max_longitude (float): Maximum longitude (eastern boundary).
    """
    # Create a new map
    plt.figure(figsize=(10, 10))
    m = Basemap(projection='merc', llcrnrlat=min_latitude, urcrnrlat=max_latitude,
                llcrnrlon=min_longitude, urcrnrlon=max_longitude, resolution='h')
    
    # draw topography
    m.shadedrelief(scale=0.5)
    
    # Draw coastlines, countries, states, and boundaries
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral', lake_color='aqua')
    
    # Draw rivers and lakes
    m.drawrivers(color='blue')
    m.drawlsmask(land_color='coral', ocean_color='aqua', lakes=True)
    
    # Draw streets using available shapefiles
    # Replace '/path/to/shapefiles' with the actual path to your shapefile
    # m.readshapefile('/path/to/shapefiles', 'streets', drawbounds=True, color='gray')
    
    # Plot and annotate each aircraft
    for aircraft in aircraft_data:
        lon, lat = aircraft[5], aircraft[6]  # Assuming the longitude is at index 5 and latitude at index 6
        x, y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=5)  # 'bo' for blue dot, markersize for the size of the dot
        plt.annotate(aircraft[0], (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='black')

    plt.title('Aircraft Positions')
    plt.show()