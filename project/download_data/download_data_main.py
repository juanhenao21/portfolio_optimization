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

import download_data_tools

# -----------------------------------------------------------------------------


def portfolio_download_data(ticker: str, time_step: str) -> None:
    """Downloads the prices of a ticker for several year in a time interval.

    :param ticker: string of the abbreviation of the stock to be analyzed
     (i.e. 'AAPL').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        function_name: str = portfolio_download_data.__name__
        download_data_tools \
            .function_header_print_data(function_name, ticker, time_step)

        # yf.pdr_override()
        # raw_data = pdr.get_data_yahoo(ticker, period='max', interval=time_step)

        raw_data = yf.download(tickers=ticker, period='max', interval='1d')

        print(raw_data)

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

    # Basic folders
    # hist_data_tools_download.hist_start_folders(fx_pairs_1, years_1)

    # Run analysis
    # Download data
    portfolio_download_data('AAPL', '1m')

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
