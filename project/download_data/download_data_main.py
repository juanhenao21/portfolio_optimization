'''Portfolio optimization download data main module.

The functions in the module download data from Yahoo! Finance for several years
in several intervals.

This script requires the following modules:
    * os
    * typing
    * pandas
    * yfinance
    * datetime
    * download_data_tools

The module contains the following functions:
    * portfolio_download_data - download data of a ticker.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
from typing import List

import pandas as pd  # type: ignore
import yfinance as yf  # type: ignore
from datetime import datetime as dt

import download_data_tools

# -----------------------------------------------------------------------------


def portfolio_download_data(tickers: List[str], year: int,
                            time_step: str) -> None:
    """Downloads the prices of a ticker for several year in a time interval.

    :param tickers: list of the string abbreviation of the stocks to be
     analyzed (i.e. ['AAPL', 'MSFT']).
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        function_name: str = portfolio_download_data.__name__
        download_data_tools \
            .function_header_print_data(function_name, tickers, year,
                                        time_step)

        init_date = dt(year=year, month=1, day=1)

        # Not all the periods can be combined with the time steps.
        raw_data = yf.download(tickers=tickers, start=init_date,
                               interval=time_step)['Adj Close']

        # Remove stocks that do not have data from the initial date
        filter_data = raw_data.dropna(axis=1, thresh=len(raw_data) - 10) \
                                     .fillna(method='ffill')

        download_data_tools.save_data(filter_data, year, time_step)

    except AssertionError as error:
        print('No data')
        print(error)

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    download_data_tools.initial_message()

    # S&P 500 companies, initial year and time step
    stocks = download_data_tools.get_stocks(['Financials'])
    year = '1980'
    time_step = '1d'
    # print(stocks)

    # Basic folders
    download_data_tools.start_folders(year, time_step)

    # Run analysis
    # Download data
    portfolio_download_data(stocks, year, time_step)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
