"""Data_Cleaning-Respiratory_Diseases.py
Author: Saad Khan
Overview:
    Cleaning dataset from Respiratory Diseases excel file
Dataset:
    http://ghdx.healthdata.org/record/ihme-data/united-states-chronic-respiratory-disease-mortality-rates-county-1980-2014
"""

import concurrent.futures
import pandas as pd

def format_sheet(sheet):

    """format_sheet(sheet) cleans a given sheet from the excel spreadsheet and saves result into directory

    sheet: name of excel spreedsheet

    """

    # Load spreadsheet
    df = pd.read_excel('respiratory_diseases_raw.xlsx', sheet_name = sheet)

    # Years are formuated into columns, df.melt will allow us to form years into rows
    df_formatted = df.melt(id_vars=['Location','FIPS'])
    df_formatted = df_formatted.rename(columns={'variable':'Year','value':'Mortality_Rate_Unformatted'})

    # Formating Mortality Rate into new columns through a split list
    df_formatted['Mortality_Rate_Unformatted'] = df_formatted['Mortality_Rate_Unformatted'].str.split(' ')

    # Mortality Rate
    df_formatted['Mortality_Rate'] = df_formatted['Mortality_Rate_Unformatted'].str[0]
    df_formatted['Mortality_Rate'] = df_formatted['Mortality_Rate'].astype(float)

    # Uncertainty Intervals for Mortality Rates
    df_formatted['Lower 95% Uncertainty Interval'] = df_formatted['Mortality_Rate_Unformatted'].str[1].str.replace('[\(]|,','')
    df_formatted['Higher 95% Uncertainty Interval'] = df_formatted['Mortality_Rate_Unformatted'].str[2].str.replace('[\)]|,','')
    df_formatted['Lower 95% Uncertainty Interval'] = df_formatted['Lower 95% Uncertainty Interval'].astype(float)
    df_formatted['Higher 95% Uncertainty Interval'] = df_formatted['Higher 95% Uncertainty Interval'].astype(float)

    # Drop unformatted mortality rate column
    del df_formatted['Mortality_Rate_Unformatted']

    # States have FIPS less than 56, we use this to split the locations into states and counties
    df_states = df_formatted[df_formatted['FIPS'] <= 56]
    df_counties = df_formatted[df_formatted['FIPS'] > 56]

    # Save dataframes as CSV into respective directories
    df_states.to_csv(f'./Cleaned/States/{sheet}.csv')
    df_counties.to_csv(f'./Cleaned/Counties/{sheet}.csv')

if __name__ == '__main__':

    # Load excel file with spreadsheet names. This will be iterated through for different respiratory
    # diseases to clean into respective counterparts.
    spread_sheet_df = pd.ExcelFile('respiratory_diseases_raw.xlsx')
    sheet_names = spread_sheet_df.sheet_names

    # Run data cleaning function for sheets with ProcessPoolExecutor for faster speed
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(format_sheet,sheet_names)
