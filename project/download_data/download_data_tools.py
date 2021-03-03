'''Portfolio optimization download data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * os
    * pickle
    * typing
    * pandas

The module contains the following functions:
    * save_data - saves the data downloaded.
    * function_header_print_data - prints info about the function running.
    * start_folders - creates folders to save data and plots.
    * initial_message - prints the initial message with basic information.
    * get_stocks - get the stocks of the S&P 500
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
import pickle
from typing import List

import pandas as pd  # type: ignore

# -----------------------------------------------------------------------------


def save_data(data: pd.DataFrame, year: str, time_step: str) -> None:
    """ Saves the data downloaded.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function prints a message and does not return a value.
    """

    # Saving data

    pickle.dump(data, open(f'../data/original_data/original_data_{year}'
                           + f'_step_{time_step}.pickle', 'wb'))

    print('Data Saved')
    print()

# -----------------------------------------------------------------------------


def function_header_print_data(function_name: str, tickers: List[str],
                               year: str, time_step: str) -> None:
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param ticker: string of the abbreviation of the stock to be analyzed
     (i.e. 'AAPL').
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function prints a message and does not return a value.
    """

    print('Portfolio Optimization')
    print(function_name)

    print(f'Downloading data for the tickers {tickers} from the year {year} to'
          + f' the present in time steps of {time_step}')
    print()

# -----------------------------------------------------------------------------


def start_folders() -> None:
    """Creates the initial folders to save the data and plots.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function creates folders and does not return a value.
    """
    try:
        os.mkdir(f'../data')
        os.mkdir(f'../plot')
        print('Folder to save data created')
        print()

    except FileExistsError as error:
        print('Folder exists. The folder was not created')
        print(error)
        print()

    try:
        os.mkdir(f'../data/original_data')
        print('Folder to save data created')
        print()

    except FileExistsError as error:
        print('Folder exists. The folder was not created')
        print(error)
        print()

# -----------------------------------------------------------------------------


def initial_message() -> None:
    """Prints the initial message with basic information.

    :return: None -- The function prints a message and does not return a value.
    """

    print()
    print('#####################')
    print('Download tickers data')
    print('#####################')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('* https://juanhenao21.github.io/')
    print('* https://github.com/juanhenao21/portfolio_optimization')
    # print('* https://forex-response_spread-year.readthedocs.io/en/latest/')
    print()

# -----------------------------------------------------------------------------


def get_stocks(sectors: List[str]) -> List:
    """Get the stocks from the S&P 500.

    :param sectors: List of the sectors to download the data (i.e. ['all'],
     ['Financials', 'Utilities']).
    :return: List -- The function returns a list with stocks symbols.
    """

    data = pd.read_html(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

    if sectors[0] == 'all':
        stocks = list(data['Symbol'])
    else:
        stocks = []
        for sector in sectors:
            stocks.extend(list(data[data['GICS Sector'] == sector]['Symbol']))

    return stocks

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
