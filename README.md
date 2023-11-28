# Decimal-Degrees-to-Features

Author: Kurtis Eisenhuth  
Date: November 16, 2023

## Overview

This is a coordinate conversion tool developed in Python using the ArcPy library. It supports conversion between various coordinate systems, including DMS, DDM, UTM, MGRS, and USNG. The use of this tool in ArcGIS Pro allows the user to upload a .csv of coordinates to convert to decimal degrees. Once converted, the tool exports a .csv of the converted coordinates, along with a shapefile or feature class of the plotted coordinates. The use of `Decimal Degrees to Features SCRIPT.py` in an IDE or open source web notebook allows the user to convert coordinates in a .csv to decimal degrees, then exports the converted values to a .csv, along with a shapefile to a local file.

## Prerequisites

- Python
- ArcGIS Pro 3.1.0 (with ArcPy library)
- NumPy
- Pandas
- MGRS library
- PyProj library
- IDE or Open Source Web Notebook (optional)

## Supported Input Coordinate Formats

- DMS (Degrees, Minutes, Seconds - 'Latitude' and 'Longitude')
- DDM (Decimal Degrees, Minutes - 'Latitude' and 'Longitude')
- UTM (Universal Transverse Mercator - 'Easting', 'Northing', and 'Zone_Hemisphere' [UTM Zone and Hemispheric Identifier Combined])
- MGRS (Military Grid Reference System - 'Location')
- USNG (United States National Grid - 'Location')

## Files
- requirements.txt - requisite package installation file
- Decimal Degrees to Features SCRIPT.py - Python file for use in an IDE or open source web notebook (Jupyter Notebook)
- DecimalDegreesToFeatures.zip - .atbx file for use in ArcGIS Pro (Python script embedded)
- Test Data.zip - .csv files containing supported input coordinates for testing

## Usage 

1. Clone the repository and/or download all relevant files.

```bash
git clone https://github.com/kurtiseisenhuth/decimal-degrees-to-features.git
cd decimal-degrees-to-features
```
 
2. Install the required libraries using pip and the requirements.txt file. Make sure you have Python and 'pip' already installed, and that you have changed the directory to the location of the text file.

If pip is not already on your machine, navigate to your Python command prompt and enter: 

```bash
python3 get-pip.py
```
Change the directory in you Python command prompt to the location of where you downloaded the Decimal-Degrees-to-Features files:

Example: 

```bash
cd "C:/Users/to/files..."
```

Install required packages: 

```bash
pip install -r requirements.txt
```

## Output
If using the tool in ArcGIS Pro, the script outputs a .csv file and, if the specified output location is a geodatabase, a feature class within the geodatabase (both the exported .csv file and feature class will be pushed to the geodatabase). If using the tool as a standalone script, it will ouput a .csv file and shapefile to the locations you update in the script (Lines 113, 168, and 169).

## Notes
- This is the current state of the tool as of November 2023. Next steps will involve introducing exception handling for errors in input coordinates.
 
- Ensure that all required dependencies are installed, and the script is executed within an environment with access to an ArcGIS installation.

- Feel free to contribute to this project by submitting issues or pull requests.

- Make sure to replace `"kurtiseisenhuth"` and `"decimal-degrees-to-features"` with your GitHub username and repository name, respectively. Users can now install the required libraries using the `pip install -r requirements.txt` command.




