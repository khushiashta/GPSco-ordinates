from geopy.geocoders import Nominatim

def get_gps_coordinates(address):
    geolocator = Nominatim(user_agent="gps_app")
    location = geolocator.geocode(address)
    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude  
    else:
        return None, None

def main():
    address = input("Enter the address to get GPS coordinates: ")
    latitude, longitude = get_gps_coordinates(address)

    if latitude and longitude:
        print(f"GPS coordinates for '{address}':")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print(f"GPS coordinates not found for '{address}'.")

if __name__ == "__main__":
    main()