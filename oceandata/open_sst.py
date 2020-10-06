



def get_sst(source = "cobe2"):
   """
   Search for World Ocean Atlas 2018 data

   Parameters
   -------------
   source: str
       source of sst data. Options are "cobe1" and "cobe2". Defaults to "cobe2"

   cobe1: https://www.psl.noaa.gov/data/gridded/data.cobe.html
   cobe2: https://www.psl.noaa.gov/data/gridded/data.cobe.html

   Returns:
   list : a list of available thredds files.

   -------------

   """


   if source == "cobe1":
       return "https://psl.noaa.gov/thredds/dodsC/Datasets/COBE/sst.mon.mean.nc"

   if source == "cobe2":
       return "https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.mean.nc"







