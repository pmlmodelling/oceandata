
from bs4 import BeautifulSoup
import requests





def get_bathy(source = "etop2"):

    """
    Search for bathymetry data

    Parameters
    -------------
    source: str
        Bathymetry source
    "etop2" : Etop02

    str : thredds url

    -------------

    """

    if source not in ["etop2"]:
        raise ValueError(f"{source} is not a valid source")

    if source == "etop2":
        url = "https://ferret.pmel.noaa.gov/pmel/thredds/dodsC/data/PMEL/smith_sandwell_topo_v8_2.nc"

    return(url)






