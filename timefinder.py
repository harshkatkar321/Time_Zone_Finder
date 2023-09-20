# importing module

from geopy.geocoders import Nominatim

from timezonefinder import TimezoneFinder


# Function Declaration

def time_zone(lad):

# initialize Nominatim API

    geolocator = Nominatim(user_agent="geoapiExercises")

# input as a geek
    

    print("Location address:", lad)

#  Finding the location
    location = geolocator.geocode(lad)  

# Initialize function to find the timezone  

    obj = TimezoneFinder()

# returns timezone

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


    timezone = pytz.timezone(result)

    # Computing the time

    now = datetime.now(timezone)

    return now.strftime('%H:%M:%S'), timezone.zone

lad = input()

# Storing function inside variable 
# Calling function
print(time_zone(lad))