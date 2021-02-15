'''Portfolio optimization download data tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * os
    * typing

The module contains the following functions:
    * hist_function_header_print_data - prints info about the function running.
    * hist_start_folders - creates folders to save data and plots.
    * hist_initial_message - prints the initial message with basic information.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
from typing import List

# -----------------------------------------------------------------------------


def function_header_print_data(function_name: str, ticker: str,
                               time_step: str) -> None:
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param ticker: string of the abbreviation of the stock to be analyzed
     (i.e. 'AAPL').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function prints a message and does not return a value.
    """

    print('Portfolio Optimization')
    print(function_name)

    print(f'Downloading data for the ticker {ticker} in time steps of '
          + f'{time_step}')
    print()

# -----------------------------------------------------------------------------


def hist_start_folders(fx_pairs: List[str], years: List[str]) -> None:
    """Creates the initial folders to save the data and plots.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: List of the strings of the year to be analyzed
     (i.e ['2016', '2017']).
    :return: None -- The function creates folders and does not return a value.
    """
    try:
        os.mkdir(f'../../hist_data')
        os.mkdir(f'../../hist_plot')
        print('Folder to save data created')

    except FileExistsError as error:
        print('Folder exists. The folder was not created')
        print(error)

    for year in years:
        try:
            os.mkdir(f'../../hist_data/original_data_{year}')
            print('Folder to save data created')

        except FileExistsError as error:
            print('Folder exists. The folder was not created')
            print(error)

        for fx_pair in fx_pairs:

            try:
                os.mkdir(f'../../hist_data/original_data_{year}/{fx_pair}')
                print('Folder to save data created')

            except FileExistsError as error:
                print('Folder exists. The folder was not created')
                print(error)

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


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
