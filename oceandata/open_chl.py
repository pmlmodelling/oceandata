
from bs4 import BeautifulSoup
import requests





def get_occci(var = None, res = "daily", years = None, months = range(1, 13), version = "6.0"):
    """
    Search for OCCCI daily data

    Parameters
    -------------
    var : str
        The variable to search for. This must be one of "chl", "kd", "iop" and "rrs".
    res : str
        temporal resolution. Must be one of "daily", "monthly" or "8day"
    years: int or list
        years to select.
    months: int or list
        months to select.
    version : str
        OCCCI version. Select one of "4.2", "5.0" and "6.0" 

    Returns:
    list : a list of available thredds files.

    -------------

    """

    if not isinstance(version, str):
        raise TypeError("version must be a str")

    if version not in ["4.2", "5.0", "6.0"]:
            raise ValueError(f"version is not valid: {version}")

    if var is None:
        raise ValueError("Please supply a variable!")

    if type(var) is not str:
        raise ValueError("Please supply a string for var!")

    if var not in ["chl", "kd", "rrs", "iop"]:
        raise ValueError(f"{var} is not a valid var")

    if res not in ["daily", "monthly", "8day"]:
        raise ValueError("Please supply a valid temporal resolution!")

    if years is None:
        raise ValueError("Please supply years required!")

    if type(years) is int:
       years = [years]

    if type(months) is int:
       months = [months]

    if type(months) is range:
        months = list(months)

    if type(years) is range:
        years = list(years)

    if type(years) is not list:
        return TypeError("years is not a list")

    if type(months) is not list:
        return TypeError("months is not a list")


    ext = "nc"

    if var == "chl":
        ensemble = []
        for yy in years:
            url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v{version}-release/geographic/{res}/chlor_a/{yy}/catalog.html'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
        chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

        files = []

        for cc in chunk:
            year = int(cc[0:4])
            if res == "daily":
                part1 = "1D"
            if res == "monthly":
                part1 = "1M"
            if res == "8day":
                part1 = "8D"
            else:
                part2 = res.upper()
            url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v{version}-release/geographic/{res}/chlor_a/{year}/ESACCI-OC-L3S-CHLOR_A-MERGED-{part1}_{part2}_4km_GEO_PML_OCx-{cc}-fv{version}.nc"
            files.append(url)

        return(files)

    if var == "rrs":
        ensemble = []
        for yy in years:
            url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v4.2-release/geographic/{res}/rrs/{yy}/catalog.html'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
        chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

        files = []

        for cc in chunk:
            year = int(cc[0:4])
            if res == "daily":
                part1 = "1D"
            if res == "monthly":
                part1 = "1M"
            if res == "8day":
                part1 = "8D"
            else:
                part2 = res.upper()
            #url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v4.2-release/geographic/{res}/kd/{year}/ESACCI-OC-L3S-CHLOR_A-MERGED-{part1}_{part2}_4km_GEO_PML_OCx-{cc}-fv4.2.nc"
            url = f"https://www.oceancolour.org/thredds/dodsC/cci/v{version}-release/geographic/{res}/rrs/{year}/ESACCI-OC-L3S-RRS-MERGED-{part1}_{part2}_4km_GEO_PML_RRS-{cc}-fv{version}.nc"

            files.append(url)

        return(files)

    if var == "kd":
        ensemble = []
        for yy in years:
            url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v4.2-release/geographic/{res}/kd/{yy}/catalog.html'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
        chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

        files = []

        for cc in chunk:
            year = int(cc[0:4])
            if res == "daily":
                part1 = "1D"
            if res == "monthly":
                part1 = "1M"
            if res == "8day":
                part1 = "8D"
            else:
                part2 = res.upper()
            #url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v4.2-release/geographic/{res}/kd/{year}/ESACCI-OC-L3S-CHLOR_A-MERGED-{part1}_{part2}_4km_GEO_PML_OCx-{cc}-fv4.2.nc"
            url = f"https://www.oceancolour.org/thredds/dodsC/cci/v{version}-release/geographic/{res}/kd/{year}/ESACCI-OC-L3S-K_490-MERGED-{part1}_{part2}_4km_GEO_PML_KD490_Lee-{cc}-fv{version}.nc"

            files.append(url)

        return(files)

    if var == "iop":
        ensemble = []
        for yy in years:
            url = f'https://rsg.pml.ac.uk/thredds/catalog/cci/v4.2-release/geographic/{res}/iop/{yy}/catalog.html'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            ensemble+=[url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        ensemble = [ff for ff in ensemble if int(ff.split("/")[-1].split("_")[-1].split("-")[1][4:6]) in months]
        chunk = [ff.split("/")[-1].split("_")[-1].split("-")[1] for ff in ensemble]

        files = []

        for cc in chunk:
            year = int(cc[0:4])
            if res == "daily":
                part1 = "1D"
            if res == "monthly":
                part1 = "1M"
            if res == "8day":
                part1 = "8D"
            else:
                part2 = res.upper()
            #url = f"https://rsg.pml.ac.uk/thredds/dodsC/cci/v4.2-release/geographic/{res}/kd/{year}/ESACCI-OC-L3S-CHLOR_A-MERGED-{part1}_{part2}_4km_GEO_PML_OCx-{cc}-fv4.2.nc"
            url = f"https://www.oceancolour.org/thredds/dodsC/cci/v{version}-release/geographic/{res}/iop/{year}/ESACCI-OC-L3S-IOP-MERGED-{part1}_{part2}_4km_GEO_PML_OCx_QAA-{cc}-fv{version}.nc"

            files.append(url)

        return(files)

