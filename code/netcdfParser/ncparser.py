import netCDF4 as nc
import pandas as pd
import requests

def cdf2df(url):
    data = requests.get(url).content
    nc_file = nc.Dataset('wodfile', memory=data)  # filename is not used as far as I can tell
    # nc_file = nc.Dataset('/home/fils/wod_osd_1909.nc')  # local file example for faster testing if you wish

    # Get the metadata
    metadata = nc_file.ncattrs()
    # print(metadata)

    # Print the metadata
    metadata_dict = {}
    for key in metadata:
        # print("{}  :\t {}".format(key, nc_file.getncattr(key)))
        metadata_dict[key] = str("{}".format(nc_file.getncattr(key)))

    # print(metadata_dict)

    df = pd.DataFrame(metadata_dict, index=[0])
    return df

if __name__ == '__main__':

    urls = ['https://noaa-wod-pds.s3.amazonaws.com/1909/wod_osd_1909.nc',
        'https://noaa-wod-pds.s3.amazonaws.com/2020/wod_drb_2020.nc' ]

    df_final = pd.DataFrame()

    for u in urls:
        df = cdf2df(u)
        df_final = df_final.append(df)

    print(df_final)
