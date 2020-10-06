
from bs4 import BeautifulSoup
import requests





def get_occci(res = "daily", years = None, months = range(1, 13)):
    """
    Search for OCCCI daily data

    Parameters
    -------------
    res : str
        temporal resolution. Must be one of "daily", "monthly" or "8day"
    years: int or list
        years to select.
    months: int or list
        months to select.


    Returns:
    list : a list of available thredds files.

    -------------

    """

    if res not in ["daily", "monthly", "8day"]:
        raise ValueError("Please supply a valid temporal resolution!")

    if type(years) is int:
       years = [years]

    if type(months) is int:
       months = [months]

    if type(months) is range:
        months = list(months)


    if type(years) is range:
        months = list(years)

    if type(years) is not list:
        return TypeError("years is not a list")

    if type(months) is not list:
        return TypeError("months is not a list")


    ext = "nc"
    ensemble = []
    for yy in years:
        url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v4.2-release/geographic/{res}/chlor_a/{yy}/catalog.html'
        #url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v4.2-release/geographic/{yy}/catalog.html'
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
    chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

    files = []

    for cc in chunk:
        year = int(cc[0:4])
        if res is "daily":
            part1 = "1D"
        if res is "monthly":
            part1 = "1M"
        if res is "8day":
            part1 = "8D"
        if res is "8day":
            part2 = "DAILY"
        else:
            part2 = res.upper()
        url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v4.2-release/geographic/{res}/chlor_a/{year}/ESACCI-OC-L3S-CHLOR_A-MERGED-{part1}_{part2}_4km_GEO_PML_OCx-{cc}-fv4.2.nc"
        files.append(url)

    return(files)






