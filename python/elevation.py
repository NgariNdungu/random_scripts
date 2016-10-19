""" Return a list of points 'latitude, longitude, elevation' 

Usage:
    elevation imports your api key from API.py. The import can be commented
    out and replaced with:
    ev = 'your-api-key'
    
    >>> import elevation
    >>> elevation.get_elevation(coords)
    ['1, 36, 879.7288...']
    
    where coords is a string of a valid location as defined by the api e.g,
    '-1,36' or '-1,36|1,37'
            
Notes:
    elevation api sample response:    
    {
   "results" : [
      {
         "elevation" : 4411.941894531250,
         "location" : {
            "lat" : 36.5785810,
            "lng" : -118.2919940
         },
         "resolution" : 19.08790397644043
      },
      {
         "elevation" : 1381.861694335938,
         "location" : {
            "lat" : 36.41150289067028,
            "lng" : -117.5602607523847
         },
         "resolution" : 19.08790397644043
      },
      {
         "elevation" : -84.61699676513672,
         "location" : {
            "lat" : 36.239980,
            "lng" : -116.831710
         },
         "resolution" : 19.08790397644043
      }
   ],
   "status" : "OK"
    }
"""

import requests
from API import elevation as ev 

base_url = "https://maps.googleapis.com/maps/api/elevation/json"

def get_elevation(coords):
    response = requests.get(base_url, params={'locations':coords, 'key':ev})
    return_value = [] # list of locations and elevations
    if response.status_code == 200:
        for result in response.json()['results']:
            return_value.append("{0}, {1}, {2}".format(result['location']['lat'],
                result['location']['lng'], result['elevation']))
    return return_value

    
if __name__ == "__main__":
    print(get_elevation("-1.5,36"))
