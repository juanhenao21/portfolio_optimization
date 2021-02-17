'''Portfolio optimization correlation matrix analysis module.

The functions in the module compute the returns, the normalized returns and the
correlation matrix of financial time series.

This script requires the following modules:
    * os
    * pickle
    * typing
    * pandas
    * correlation_matrix_tools

The module contains the following functions:
    * returns - computes the returns of the time series.
    * normalized_returns - normalize the returns of the time series.
    * correlation_matrix - compute the correlation matrix of the normalized
      returns.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import os
import pickle
from typing import List

import pandas as pd  # type: ignore
from matplotlib import pyplot as plt

import correlation_matrix_tools

# -----------------------------------------------------------------------------


def returns(year: str, time_step: str) -> None:
    """computes the returns of the time series.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = returns.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, year, 'returns')

    try:

        # Load data
        data = pickle.load(open(
                    f'../data/original_data/original_data_{year}_step'
                    + f'_{time_step}.pickle', 'rb'))

        data_returns = data.pct_change().dropna()

        # Saving data
        correlation_matrix_tools \
            .save_data(data_returns, function_name, year, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def hist_fx_correlations_physical_data(year: str, interval: str) -> None:
    """Computes the correlation matrix in an interval of time.

    :param year: string of the year to be analyzed (i.e. '2016').
    :param interval: string of the interval to be analyzed (i.e. 'week',
     'month', 'quarter', 'year')
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = hist_fx_correlations_physical_data.__name__
    hist_data_tools_matrices_physical \
        .hist_function_header_print_data(function_name, year, 'corr')

    try:
        # Load data
        fx_returns: pd.DataFrame = pickle.load(open(
                        f'../../hist_data/matrices_physical_{year}/hist_fx'
                        + f'_matrices_physical_data/hist_fx_returns_matrices'
                        + f'_physical_data_{year}.pickle', 'rb'))

        freq: str
        periods: int
        if interval == 'week':
            freq = 'W'
            periods = 52
        elif interval == 'month':
            freq = 'MS'
            periods = 12
        else:
            freq = 'QS'
            periods = 4

        if interval == 'year':
            corr: pd.DataFrame = fx_returns.corr()
            hist_data_tools_matrices_physical \
                .hist_save_data(corr, year, interval, '01')

        else:
            time_int: pd.DatetimeIndex = \
                pd.date_range(f'{year}-01-01', periods=periods, freq=freq)

            t_idx: int
            t_idx_str: str
            for t_idx in range(1, periods):
                corr = fx_returns[time_int[t_idx - 1]: time_int[t_idx]].corr()

                if t_idx < 10:
                    t_idx_str = f'0{t_idx}'
                else:
                    t_idx_str = f'{t_idx}'

                hist_data_tools_matrices_physical \
                    .hist_save_data(corr, year, interval, t_idx_str)

            corr = fx_returns[time_int[-1]:].corr()

            if t_idx < 10:
                t_idx_str = f'0{t_idx + 1}'
            else:
                t_idx_str = f'{t_idx + 1}'

            hist_data_tools_matrices_physical \
                .hist_save_data(corr, year, interval, t_idx_str)

        del fx_returns
        del corr

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# ----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
