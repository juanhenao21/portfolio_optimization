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


def portfolio_download_data(tickers: List[str], dates: List[str],
                            time_step: str) -> None:
    """Downloads the prices of a ticker for an interval of years in a time
       step.

    :param tickers: list of the string abbreviation of the stocks to be
     analyzed (i.e. ['AAPL', 'MSFT']).
    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:
        function_name: str = portfolio_download_data.__name__
        download_data_tools \
            .function_header_print_data(function_name, tickers, dates,
                                        time_step)

        init_year = int(dates[0].split('-')[0])
        init_month = int(dates[0].split('-')[1])
        fin_year = int(dates[1].split('-')[0])
        fin_month = int(dates[1].split('-')[1])

        init_date: dt = dt(year=init_year, month=init_month, day=1)
        fin_date: dt = dt(year=fin_year, month=fin_month, day=1)

        # Not all the periods can be combined with the time steps.
        raw_data: pd.DataFrame = \
            yf.download(tickers=tickers, start=init_date, end=fin_date,
                        interval=time_step)['Adj Close']

        if raw_data.isnull().values.any():
            # Remove stocks that do not have data from the initial date
            raw_data = raw_data.dropna(axis=1, thresh=len(raw_data) - 10) \
                .fillna(method='ffill')

        download_data_tools.save_data(raw_data, dates, time_step)

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
    stocks: List[str] = download_data_tools.get_stocks(['all'])
    dates: List[str] = ['2006-01', '2006-03']
    time_step: str = '1d'

    # Basic folders
    download_data_tools.start_folders()

    # Run analysis
    # Download data
    portfolio_download_data(stocks, dates, time_step)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
