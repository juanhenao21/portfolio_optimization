'''Portfolio optimization correlation matrix analysis module.

The functions in the module compute the returns, the normalized returns and the
correlation matrix of financial time series.

This script requires the following modules:
    * pickle
    * pandas
    * correlation_matrix_tools

The module contains the following functions:
    * returns - computes the returns of the time series.
    * normalized_returns - normalizes the returns of the time series.
    * correlation_matrix - computes the correlation matrix of the normalized
      returns.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import pickle

import pandas as pd  # type: ignore

import correlation_matrix_tools

# -----------------------------------------------------------------------------


def returns_data(year: str, time_step: str) -> None:
    """Computes the returns of the time series.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = returns_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, year, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/original_data/original_data_{year}_step_{time_step}'
            + f'.pickle', 'rb'))

        returns_df: pd.DataFrame = data.pct_change().dropna()

        # Saving data
        correlation_matrix_tools \
            .save_data(returns_df, function_name, year, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def normalized_returns_data(year: str, time_step: str) -> None:
    """Normalizes the returns of the time series.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, year, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{year}_step_{time_step}'
            + f'.pickle', 'rb'))

        normalized_df: pd.DataFrame = (data - data.mean()) / data.std()

        # Saving data
        correlation_matrix_tools \
            .save_data(normalized_df, function_name, year, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def correlation_matrix_data(year: str, time_step: str) -> None:
    """Computes the correlation matrix of the normalized returns.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = correlation_matrix_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, year, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{year}_step'
            + f'_{time_step}.pickle', 'rb'))

        corr_matrix_df: pd.DataFrame = data.corr()

        # Saving data
        correlation_matrix_tools \
            .save_data(corr_matrix_df, function_name, year, time_step)

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
