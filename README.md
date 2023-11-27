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

## Usage 

1. Clone the repository.

```bash
git clone https://github.com/kurtiseisenhuth/decimal-degrees-to-features.git
cd decimal-degrees-to-features
```
2. Install the required libraries using pip. Make sure you have Python and 'pip' installed.

```bash
pip install -r requirements.txt
```

3. 


