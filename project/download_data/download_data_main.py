'''Portfolio optimization download data main module.

The functions in the module download data from Yahoo! Finance for several years
in several intervals.

This script requires the following modules:
    * os
    * typing
    * yfinance
    * pandas
    * pandas_datareader

The module contains the following functions:
    * portfolio_download_data - download data of a ticker.
    * portfolio_download_all_data - downloads all the tickers data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
from typing import List

import pandas as pd  # type: ignore
import pandas_datareader as pdr  # type: ignore
import yfinance as yf  # type: ignore
from datetime import datetime as dt

import download_data_tools

# -----------------------------------------------------------------------------


def portfolio_download_data(ticker: str, year: int, time_step: str) -> None:
    """Downloads the prices of a ticker for several year in a time interval.

    :param ticker: string of the abbreviation of the stock to be analyzed
     (i.e. 'AAPL').
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        function_name: str = portfolio_download_data.__name__
        download_data_tools \
            .function_header_print_data(function_name, ticker, year,
                                        time_step)

        init_date = dt(year=year, month=1, day=1)

        # Not all the periods can be combined with the time steps.
        raw_data = yf.download(tickers='AIG', start=init_date,
                               interval=time_step)['Adj Close']

        print(raw_data.isnull().sum())
        # print(raw_data.dropna(axis=1, how='any'))
        # print(type(raw_data))

    except AssertionError as error:
        print('No data')
        print(error)

# -----------------------------------------------------------------------------


def hist_download_all_data(fx_pairs: List[str], years: List[str]) -> None:
    """Downloads all the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of the strings of the years to be analyzed
     (i.e. ['2016', '2017]).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    with mp.Pool(processes=mp.cpu_count()) as pool:
        pool.starmap(hist_download_data, iprod(fx_pairs, years))

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    download_data_tools.initial_message()

    # S&P 500 companies, period and time step
    stocks = download_data_tools.get_stocks(['Financials'])
    # print(stocks)
    # Basic folders
    # hist_data_tools_download.hist_start_folders(fx_pairs_1, years_1)

    # Run analysis
    # Download data
    portfolio_download_data(stocks, 1980, '1d')

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
