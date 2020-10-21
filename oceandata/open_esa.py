from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_occci_sst(res="daily", years=range(1981, 2017), months=range(1, 13)):
    """
    Search for OCCCI daily data

    Parameters
    -------------
    years: int or list
        Years to select. Defaults to selecting all years
    months: int or list
        Months to select. Defaults to selecting all years


    Returns:
    list : a list of available thredds files.

    -------------

    """

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

    urls = pd.DataFrame({"date": pd.date_range("1981-09-01", periods=12905, freq="1D")})

    def extract_url(x):
        year = x.year
        month = str(x.month).zfill(2)
        day = str(x.day).zfill(2)
        return f"http://dap.ceda.ac.uk/thredds/dodsC/neodc/esacci/sst/data/CDR_v2/Analysis/L4/v2.1/{year}/{month}/{day}/{year}{month}{day}120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_CDR2.1-v02.0-fv01.0.nc"

    urls["url"] = [extract_url(x) for x in urls.date]

    if years is not None:
        urls = urls.query("date.dt.year in @years")

    months = urls.query("date.dt.month in @months")

    if len(urls) == 0:
        raise ValueError("You have not supplied a valid time selection!")

    files = list(urls.url)

    return files
