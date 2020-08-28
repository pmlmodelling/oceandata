



def get_woa(var = None, years = None, months = range(1, 13)):

   """
   Search for World Ocean Atlas 2018 data

   Parameters
   -------------
   var: str
       variable to search for. Must be one of "temperature", "salinity", "silicate", "phosphate" or "nitrate"
   years: int or list
       years to select. WOA data is decadal, so the decade with the year will be identified. Only relevant for temperature and salinity. The others are available as climatologies.
   months: int or list
       months to select.


   Returns:
   list : a list of available thredds files.

   -------------

   """


    if var not in ["temperature", "salinity", "silicate", "phosphate", "nitrate"]:
        raise ValueError("Please supply a valid variable!")

    if type(months) is int:
        months = [months]

    for mm in months:
        if mm not in range(1, 13):
            raise ValueError(f"month {mm} is not valid!")

    if var in ["nitrate", "silicate", "phosphate"]:
        ensemble = []
        print(f"{var} is only available as a climatological average")

        for mm in months:
            month = str(mm).ljust(2, '0')
            if var == "nitrate":
                url = f"https://data.nodc.noaa.gov/thredds/dodsC/ncei/woa/nitrate/all/1.00/woa18_all_n{month}_01.nc"
            if var == "silicate":
                url = f"https://data.nodc.noaa.gov/thredds/dodsC/ncei/woa/silicate/all/1.00/woa18_all_i{month}_01.nc"
            if var == "phosphate":
                url = f"https://data.nodc.noaa.gov/thredds/dodsC/ncei/woa/phosphate/all/1.00/woa18_all_p{month}_01.nc"
            ensemble.append(url)

        return(ensemble)

    if type(var) is None:
        raise ValueError("No var supplied!")

    if type(var) is not str:
        raise ValueError("var is not a string")


    if type(years) is int:
        years = [years]

    if type(years) is not list:
        raise ValueError("Please supply either one or two years")


    periods = []

    for yy in years:
        if yy < 1955 or yy > 2017:
            raise ValueError(f"{yy} is not valid!")
        if (yy >= 1955) and (yy < 1965):
            periods.append("5564")

        if (yy >= 1965) and (yy < 1975):
            periods.append("6574")

        if (yy >= 1975) and (yy < 1985):
            periods.append("7584")

        if (yy >= 1985) and (yy < 1995):
            periods.append("8594")
        if (yy >= 1995) and (yy < 2005):
            periods.append("95A4")
        if (yy >= 2005) and (yy < 2018):
            periods.append("A5B7")

    if periods is []:
        raise ValueError("Please supply valid years")

    ensemble = []


    for mm in months:
        for pp in periods:
            month = str(mm).ljust(2, '0')

            if var == "temperature":
                url = f"https://data.nodc.noaa.gov/thredds/dodsC/ncei/woa/{var}/{pp}/1.00/woa18_{pp}_t{month}_01.nc"

            if var == "salinity":
                url = f"https://data.nodc.noaa.gov/thredds/dodsC/ncei/woa/{var}/{pp}/1.00/woa18_{pp}_s{month}_01.nc"


            ensemble.append(url)

    return(ensemble)






