'''Portfolio optimization correlation matrix analysis module.

The functions in the module compute the returns, the normalized returns and the
correlation matrix of financial time series.

This script requires the following modules:
    * pickle
    * typing
    * pandas
    * correlation_matrix_tools

The module contains the following functions:
    * returns_data - computes the returns of the time series.
    * volatility_data - computes the volatility in a time window of the time
     series.
    * normalized_returns_data - normalizes the returns of the time series.
    * correlation_matrix_data - computes the correlation matrix of the
     normalized returns.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import pickle
from typing import List

import pandas as pd  # type: ignore

import correlation_matrix_tools

# -----------------------------------------------------------------------------


def returns_data(dates: List[str], time_step: str) -> None:
    """Computes the returns of the time series.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = returns_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, dates, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/original_data/original_data_{dates[0]}_{dates[1]}_step'
            + f'_{time_step}.pickle', 'rb'))

        returns_df: pd.DataFrame = data.pct_change().dropna()

        # Saving data
        correlation_matrix_tools \
            .save_data(returns_df, function_name, dates, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def volatility_data(dates: List[str], time_step: str, window: str) -> None:
    """Computes the volatility in a time window of the time series.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = volatility_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, dates, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        std_df: pd.DataFrame = data.rolling(window=int(window)).std().dropna()

        # Saving data
        correlation_matrix_tools \
            .save_data(std_df, function_name + f'_win_{window}', dates,
                       time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def normalized_returns_data(years: List[str], time_step: str) -> None:
    """Normalizes the returns of the time series.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, years, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{years[0]}_{years[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        normalized_df: pd.DataFrame = (data - data.mean()) / data.std()

        # Saving data
        correlation_matrix_tools \
            .save_data(normalized_df, function_name, years, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def correlation_matrix_data(years: List[str], time_step: str) -> None:
    """Computes the correlation matrix of the normalized returns.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = correlation_matrix_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, years, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{years[0]}'
            + f'_{years[1]}_step_{time_step}.pickle', 'rb'))

        corr_matrix_df: pd.DataFrame = data.corr()

        # Saving data
        correlation_matrix_tools \
            .save_data(corr_matrix_df, function_name, years, time_step)

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
