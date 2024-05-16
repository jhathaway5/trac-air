import colorlog
from src.fetch_data import get_aircraft_data_region
from src.display_data import display_aircraft_data, plot_aircraft_positions

def setup_logging():
    """Set up the logging configuration with colored output."""
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s'))

    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel('INFO')
    return logger

def main():
    # Setup logging
    logger = setup_logging()
    
    # Define the region and delta size
    center_latitude = 36.1700
    center_longitude = -95.9000
    delta_size = 1.500  # Adjust this value to bump up or down the region size
    
    min_latitude = center_latitude - delta_size
    max_latitude = center_latitude + delta_size
    min_longitude = center_longitude - 2.0*delta_size
    max_longitude = center_longitude + 2.0*delta_size
    
    logger.info(f"Using delta size: {delta_size}")
    logger.info(f"Region boundaries: lat({min_latitude} to {max_latitude}), lon({min_longitude} to {max_longitude})")
    
    # Fetch data
    aircraft_data = get_aircraft_data_region(min_latitude, max_latitude, min_longitude, max_longitude)
    
    # Display and plot data
    if aircraft_data:
        display_aircraft_data(aircraft_data)
        plot_aircraft_positions(aircraft_data, min_latitude, max_latitude, min_longitude, max_longitude)
    else:
        logger.warning("No aircraft data available for the specified region.")

if __name__ == "__main__":
    main()