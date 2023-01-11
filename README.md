# oceandata
Methods to access oceanographic data available through the likes of thredds servers.


## Installation

Install the development version using using pip:
```sh
pip install git+https://github.com/pmlmodelling/oceandata.git
```


## Examples of usage

### Finding OCCCI Ocean Colour data 

If you wanted to get OCCCI Chlorophyll data, you can use the `get_occci` function. This requires you to specify the variable, the years required, OCCCI version and the temporal resolution.

So, if you wanted monthly chlorophyll for 1997 through to 2023 from v6.0 of OCCCI, you can run the following::

```
import oceandata as oc
files = oc.get_occci(var= "chl", years = range(1997, 2023), version = "6.0", res = "monthly")
```

This will provide you with a list of OPeNDAP paths for the monthly files. You can then use nctoolkit's `open_thredds` method to work directly with these files.

