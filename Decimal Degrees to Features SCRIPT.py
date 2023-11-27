# Decimal Degrees to Features - Kurtis Eisenhuth 11/16/2023

import os
import re
import arcpy
import numpy as np
import pandas as pd
from mgrs import MGRS
from pyproj import Proj, transform

# set dataframe option to display all rows if needed
pd.set_option('display.max_rows', None)

def convert_dms_to_decimal(latitudes, longitudes):
    # convert degrees, minutes, seconds (DMS) to decimal degrees
    def dms_to_dd(degrees, minutes, seconds, direction):
        dd = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
        if direction in ['S', 'W']:
            dd *= -1
        return dd

    df_lat = latitudes.str.extract(r'(?P<d>[\d\.]+).*?(?P<m>[\d\.]+).*?(?P<s>[\d\.]+).*?(?P<h>[NSWE])')
    df_lon = longitudes.str.extract(r'(?P<d>[\d\.]+).*?(?P<m>[\d\.]+).*?(?P<s>[\d\.]+).*?(?P<h>[NSWE])')

    latitudes_dd = df_lat.apply(lambda row: dms_to_dd(row[0], row[1], row[2], row[3]), axis=1)
    longitudes_dd = df_lon.apply(lambda row: dms_to_dd(row[0], row[1], row[2], row[3]), axis=1)

    return latitudes_dd, longitudes_dd

def convert_ddm_to_decimal(latitudes, longitudes):
    def ddm_to_dd(coord_str):
        try:
            # extract degrees and minutes as floating-point numbers
            degrees, minutes = map(float, re.findall(r'(\d+\.\d+|\d+)', str(coord_str)))

            # determine the direction (N/S or E/W)
            direction_match = re.search(r'[NSWE]', str(coord_str), re.IGNORECASE)
            if direction_match:
                direction = direction_match.group().upper()
            else:
                raise ValueError("Direction not found in coordinate string.")

            # convert to decimal degrees
            dd = degrees + minutes / 60
            if direction in ['S', 'W']:
                dd *= -1

            return dd
        except Exception as e:
            print(f"Error converting coordinate {coord_str} to decimal degrees: {e}")
            return float('nan')

    # apply the ddm_to_dd function to each row and assign the result to the corresponding columns
    latitudes_dd = latitudes.apply(ddm_to_dd)
    longitudes_dd = longitudes.apply(ddm_to_dd)

    return latitudes_dd, longitudes_dd

def convert_mgrs_to_decimal(mgrs_coordinates):
    def mgrs_to_dd(mgrs):
        try:
            # example conversion using mgrs library
            mgrs_obj = MGRS()
            lat, lon = mgrs_obj.toLatLon(mgrs)
            return lat, lon
        except Exception as e:
            print(f"Error processing {mgrs}: {e}")
            return float('nan'), float('nan')

    lat_lon = mgrs_coordinates.apply(mgrs_to_dd)

    return lat_lon.apply(lambda x: x[0]), lat_lon.apply(lambda x: x[1])

def convert_usng_to_decimal(mgrs_coordinates):
    def usng_to_dd(mgrs):
        try:
            # example conversion using mgrs library
            mgrs_obj = MGRS()
            lat, lon = mgrs_obj.toLatLon(mgrs)
            return lat, lon
        except Exception as e:
            print(f"Error processing {mgrs}: {e}")
            return float('nan'), float('nan')

    lat_lon = mgrs_coordinates.apply(usng_to_dd)

    return lat_lon.apply(lambda x: x[0]), lat_lon.apply(lambda x: x[1])

def convert_utm_to_decimal(easting, northing, zone_hemisphere):
    try:
        zone, hemisphere = re.match(r'(\d+)\s*([NS])', zone_hemisphere).groups()

        if not (1 <= int(zone) <= 60) or hemisphere not in ['N', 'S']:
            raise ValueError("Invalid UTM Zone_Hemisphere format.")

        in_proj = Proj(proj='utm', zone=int(zone), datum='WGS84', hemisphere=hemisphere)
        out_proj = Proj(proj='latlong', datum='WGS84')
        lon, lat = transform(in_proj, out_proj, easting, northing)

        return lat, lon

    except ValueError as e:
        print(f"Error: {e}")
        return float('nan'), float('nan')
    
def save_to_csv(df, csv_path):
    # save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False, encoding='ISO-8859-1')
    print(f"CSV written to: {csv_path}")

def save_to_shapefile(df, shapefile_path):
    # save the DataFrame to a temporary CSV file
    temp_csv_path = 'C:/path/to/temp.csv'  # <-- SET THE APPROPRIATE TEMPORARY PATH HERE -->
    df.to_csv(temp_csv_path, index=False, encoding='ISO-8859-1')

    try:
        # create a temporary feature class from the CSV file
        temp_layer = arcpy.management.MakeXYEventLayer(temp_csv_path, 'Longitude_DD', 'Latitude_DD', 'temp_layer')

        # save the temporary layer as a shapefile
        arcpy.conversion.FeatureClassToFeatureClass(temp_layer, os.path.dirname(shapefile_path), os.path.basename(shapefile_path))
        print(f"Shapefile created at: {shapefile_path}")

    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
    finally:
        # clean up the temporary CSV file
        if os.path.exists(temp_csv_path):
            os.remove(temp_csv_path)

def convert_coordinates(input_file, csv_output_file, shapefile_output_file, input_format):
    # read the input CSV file into a DataFrame
    df = pd.read_csv(input_file, encoding='ISO-8859-1')

    # convert coordinates based on the input format
    if input_format.lower() == 'dms':
        df['Latitude_DD'], df['Longitude_DD'] = convert_dms_to_decimal(df['Latitude'], df['Longitude'])
    elif input_format.lower() == 'ddm':
        df['Latitude_DD'], df['Longitude_DD'] = convert_ddm_to_decimal(df['Latitude'], df['Longitude'])
    elif input_format.lower() == 'mgrs':
        df['Latitude_DD'], df['Longitude_DD'] = convert_mgrs_to_decimal(df['Location'])
    elif input_format.lower() == 'usng':
        df['Latitude_DD'], df['Longitude_DD'] = convert_usng_to_decimal(df['Location'])
    elif input_format.lower() == 'gar':
        df['Latitude_DD'], df['Longitude_DD'] = convert_gar_to_decimal(df['Location'])
    elif input_format.lower() == 'wgrs':
        df['Latitude_DD'], df['Longitude_DD'] = convert_wgrs_to_decimal(df['Location'])
    elif input_format.lower() == 'utm':
        df[['Latitude_DD', 'Longitude_DD']] = df.apply(
            lambda row: convert_utm_to_decimal(row['Easting'], row['Northing'], row['Zone_Hemisphere']),
            axis=1,
            result_type='expand'
        )
        # convert Zone_Hemisphere column to string
        df['Zone_Hemisphere'] = df['Zone_Hemisphere'].astype(str)
    else:
        print("Invalid input format. Supported formats: DMS, DDM, MGRS, USNG, GAR, WGRS, UTM")
        return

    # save the DataFrame with converted coordinates to a new CSV file
    save_to_csv(df, csv_output_file)

    # save the DataFrame with converted coordinates to a new shapefile
    save_to_shapefile(df, shapefile_output_file)

# run conversion function and output CSV and shapefile <-- REPLACE INPUT/OUTPUT FILE PATHS AND FORMAT HERE -->
convert_coordinates('C:/path/to/input.csv',
                    'C:/path/to/output.csv',
                    'C:/path/to/output.shp', 'dms')
