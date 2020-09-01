
from bs4 import BeautifulSoup
import requests





def get_occci(var = None, years = None, months = range(1, 13)):
    """
    Search for OCCCI daily data

    Parameters
    -------------
    var: str
        variable to search for. Must be one of "chlor_a" etc.
    years: int or list
        years to select.
    months: int or list
        months to select.


    Returns:
    list : a list of available thredds files.

    -------------

    """

    if type(years) is int:
       years = [years]

    if type(months) is int:
       months = [months]

    if type(years) is not list:
        return TypeError("years is not a list")

    if type(months) is not list:
        return TypeError("months is not a list")


    ext = "nc"
    ensemble = []
    for yy in years:
        url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v5.0-release/geographic/{yy}/catalog.html'
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
    chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

    files = []

    for cc in chunk:
        year = int(cc[0:4])
        url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v5.0-release/geographic/{year}/ESACCI-OC-L3S-OC_PRODUCTS-MERGED-1D_DAILY_4km_GEO_PML_OCx_QAA-{cc}-fv5.0.nc"
        files.append(url)



    if var not in ["chlor_a"]:
        raise ValueError("Please supply a valid variable!")

    return(files)






