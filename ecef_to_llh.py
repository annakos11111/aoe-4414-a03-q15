# ecef_to_llh.py
#
# Usage: python3 ecef_to_llh.py r_x_km r_y_km r_z_km
#  Converts ECEF coordinates to llh
# Parameters:
#  r_x_km : x-component of radius in km
#  r_y_km : y-component of radius in km
#  r_z_km : z-component of radius in km
# Output:
#  Outputs latitude in deg and height above ellipsoid in km
#
# Written by Anna Kosnic

# import Python modules
import sys # argv
import math as m

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
## function description
def calc_denom(ecc,lat_rad):
    return m.sqrt(1-ecc**2 *(m.sin(lat_rad))**2)

# initialize script arguments
r_x_km = float('nan') 
r_y_km = float('nan') 
r_z_km = float('nan')

# parse script arguments
if len(sys.argv)==4:
  r_x_km = float(sys.argv[1])
  r_y_km = float(sys.argv[2])
  r_z_km = float(sys.argv[3])
  ...
else:
  print(\
   'Usage: '\
   'python3 python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
  )
  exit()

## scripting below

# calculate longitude
lon_rad = m.atan2(r_y_km,r_x_km)
lon_deg = lon_rad * 180/m.pi

# inital guess
lat_rad = m.asin(r_z_km/m.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2))
r_lon_km = m.sqrt(r_x_km**2 + r_y_km**2)
prev_lat_rad = float('nan')

# iterative solver
count = 0
c_E = float('nan')

while (m.isnan(prev_lat_rad) or abs(lat_rad-prev_lat_rad>10e-7)) and count<5:
   denom = calc_denom(E_E, lat_rad)
   c_E = R_E_KM/denom
   prev_lat_rad = lat_rad
   lat_rad = m.atan((r_z_km + c_E*E_E**2 * m.sin(lat_rad)) / r_lon_km)
   count = count + 1

hae_km = r_lon_km/m.cos(lat_rad)-c_E

print('LON: ' +str(lon_deg) + ' deg')
print('LAT: ' +str(lat_rad*180/m.pi) + ' deg')
print('HAE: ' +str(hae_km) + ' km')