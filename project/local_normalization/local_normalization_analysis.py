'''Portfolio optimization local normalization analysis module.

The functions in the module use local normalization to compute the returns, the
normalized returns and the correlation matrix of financial time series.

This script requires the following modules:
    * pickle
    * typing
    * pandas
    * local_normalization_tools

The module contains the following functions:
    * ln_volatility_data - uses local normalization to compute the volatility
      of the time series.
    * ln_normalized_returns_data - uses local normalization to normalize the
      returns of the time series.
    * ln_correlation_matrix_data - uses local normalization to compute the
      correlation matrix of the normalized returns.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import pickle
from typing import List

import pandas as pd  # type: ignore

import local_normalization_tools

# -----------------------------------------------------------------------------


def ln_volatility_data(dates: List[str], time_step: str, window: str) -> None:
    """Uses local normalization to compute the volatility of the time series.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m').
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_volatility_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, dates, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        std_df: pd.DataFrame = data.rolling(window=int(window)).std().dropna()

        # Saving data
        local_normalization_tools \
            .save_data(std_df, function_name, dates, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def ln_normalized_returns_data(years: List[str], time_step: str,
                               window: str) -> None:
    """Uses local normalization to normalize the returns of the time series.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_normalized_returns_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, years, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{years[0]}_{years[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        data_win = data.iloc[int(window) - 1:]
        data_mean = data.rolling(window=int(window)).mean().dropna()
        data_std = data.rolling(window=int(window)).std().dropna()

        normalized_df: pd.DataFrame = (data_win - data_mean) / data_std

        # Saving data
        local_normalization_tools \
            .save_data(normalized_df, function_name, years, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def ln_correlation_matrix_data(years: List[str], time_step: str,
                               window: str) -> None:
    """uses local normalization to compute the correlation matrix of the
       normalized returns.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_correlation_matrix_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, years, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/local_normalization/ln_normalized_returns_data_{years[0]}'
            + f'_{years[1]}_step_{time_step}_win_{window}.pickle', 'rb'))

        corr_matrix_df: pd.DataFrame = data.corr()

        # Saving data
        local_normalization_tools \
            .save_data(corr_matrix_df, function_name, years, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

    except TypeError as error:
        print('To compute the correlation is needed at least to stocks')
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
