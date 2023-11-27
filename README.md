# Decimal-Degrees-to-Features

Author: Kurtis Eisenhuth  
Date: November 16, 2023

## Overview

This is a coordinate conversion tool developed in Python using the ArcPy library. It supports conversion between various coordinate systems, including DMS, DDM, UTM, MGRS, and USNG. The use of this tool in ArcGIS Pro allows the user to upload a .csv of coordinates to convert to decimal degrees - once converted, the tool exports a .csv of the converted coordinates, along with a shapefile or feature class of the plotted coordinates. 

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

1. Clone the repository OR download all relevant files.

```bash
git clone https://github.com/kurtiseisenhuth/decimal-degrees-to-features.git
cd decimal-degrees-to-features
```
2. Install the required libraries using pip and the requirements.txt file. Make sure you have Python and 'pip' already installed, and that you have changed the directory to the location of the text file.

```bash
pip install -r requirements.txt
```

3. 


