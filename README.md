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

## Supported Formats

- DMS (Degrees, Minutes, Seconds)
- DDM (Decimal Degrees, Minutes)
- UTM (Universal Transverse Mercator)
- MGRS (Military Grid Reference System)
- USNG (United States National Grid)

## Usage 

1. Clone the repository and/or download all relevant files (ADD RELEVANT FILE NAMES).

```bash
git clone https://github.com/kurtiseisenhuth/decimal-degrees-to-features.git
cd decimal-degrees-to-features
```
2. Install the required libraries using pip and the requirements.txt file. Make sure you have Python and 'pip' already installed, and that you have changed the directory to the location of the text file.

```bash
pip install -r requirements.txt
```

## Output
The script outputs a CSV file and, if the specified output location is a geodatabase, a feature class within the geodatabase.

## Note
- Ensure that all required dependencies are installed, and the script is executed within an environment with access to an ArcGIS installation.

- Feel free to contribute to this project by submitting issues or pull requests.

- Make sure to replace `"kurtiseisenhuth"` and `"decimal-degrees-to-features"` with your GitHub username and repository name, respectively. The users can now install the required libraries using the `pip install -r requirements.txt` command.




