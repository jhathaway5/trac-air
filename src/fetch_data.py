import requests
import colorlog

# Use the root logger configured in main.py
logger = colorlog.getLogger()

def get_aircraft_data_region(min_latitude=36.0200, max_latitude=36.3200, min_longitude=-96.0500, max_longitude=-95.7500):
    """
    Fetch aircraft data for a specific region defined by latitude and longitude boundaries.
    Default coordinates are set to be twice as large around Tulsa International Airport.

    Parameters:
    min_latitude (float): Minimum latitude (southern boundary)
    max_latitude (float): Maximum latitude (northern boundary)
    min_longitude (float): Minimum longitude (western boundary)
    max_longitude (float): Maximum longitude (eastern boundary)

    Returns:
    list: List of aircraft states in the specified region, or None if no data found.
    """
    logger.info(f"Fetching aircraft data for enlarged region: lat({min_latitude} to {max_latitude}), lon({min_longitude} to {max_longitude})")
    
    url = f"https://opensky-network.org/api/states/all?lamin={min_latitude}&lamax={max_latitude}&lomin={min_longitude}&lomax={max_longitude}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        aircraft_data = response.json().get('states', [])

        if not aircraft_data:
            logger.warning("No aircraft data found for the specified region.")
            return None
        return aircraft_data
    except requests.RequestException as e:
        logger.error(f"Error fetching aircraft data: {e}")
        return None