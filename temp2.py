from numpy import *
from netCDF4 import *



srcDir  = "/home/utsumi/mnt/wellshare/data/MERGIR/2014/0401"
srcPath = srcDir + "/merg_2014040100_4km-pixel.nc4"

nc = Dataset(srcPath, "r", format="NETCDF")

Lat = nc.variables["lat"]
Lon = nc.variables["lon"]
Time= nc.variables["time"]
Tb  = nc.variables["Tb"]
