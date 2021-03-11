'''Portfolio optimization local normalization analysis module.

The functions in the module use local normalization to compute the returns, the
normalized returns and the correlation matrix of financial time series.

This script requires the following modules:
    * pickle
    * typing
    * numpy
    * pandas
    * local_normalization_tools

The module contains the following functions:
    * ln_volatility_data - uses local normalization to compute the volatility
      of the time series.
    * ln_normalized_returns_data - uses local normalization to normalize the
      returns of the time series.
    * ln_correlation_matrix_data - uses local normalization to compute the
      correlation matrix of the normalized returns.
    * ln_aggregated_dist_returns_pair_data - uses local normalization to
      compute the aggregated distribution of returns for a pair of stocks.
    * ln_aggregated_dist_returns_market_data - uses local normalization to
      compute the aggregated distribution of returns for a market.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

import pickle
from typing import List, Tuple

import numpy as np  # type: ignore
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


def ln_normalized_returns_data(dates: List[str], time_step: str,
                               window: str) -> None:
    """Uses local normalization to normalize the returns of the time series.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_normalized_returns_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, dates, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        data_win = data.iloc[int(window) - 1:]
        data_mean = data.rolling(window=int(window)).mean().dropna()
        data_std = data.rolling(window=int(window)).std().dropna()

        normalized_df: pd.DataFrame = (data_win - data_mean) / data_std

        # Saving data
        local_normalization_tools \
            .save_data(normalized_df, function_name, dates, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def ln_correlation_matrix_data(dates: List[str], time_step: str,
                               window: str) -> None:
    """uses local normalization to compute the correlation matrix of the
       normalized returns.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_correlation_matrix_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, dates, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/local_normalization/ln_normalized_returns_data_{dates[0]}'
            + f'_{dates[1]}_step_{time_step}_win_{window}.pickle', 'rb'))

        corr_matrix_df: pd.DataFrame = data.corr()

        # Saving data
        local_normalization_tools \
            .save_data(corr_matrix_df, function_name, dates, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

    except TypeError as error:
        print('To compute the correlation is needed at least to stocks')
        print(error)
        print()

# ----------------------------------------------------------------------------


def ln_aggregated_dist_returns_pair_data(data: pd.DataFrame, cols: Tuple[str],
                                         time_step: str, window: str) -> None:
    """Uses local normalization to compute the aggregated distribution of
       returns for a pair of stocks.

    :param data: pandas dataframe to be used.
    :param cols: pair of stocks to be analized (i. e. ('AAPL', 'MSFT')).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    try:

        two_col = data[[cols[0], cols[1]]]
        cov_two_col = two_col.cov()
        eVa, eVe = np.linalg.eig(cov_two_col)

        # R: rotation, S: scaling
        # eVe:  eigenvector, eVa: eigenvalues
        R, S = eVe, np.diag(np.sqrt(eVa))
        # T: transformation matrix
        # T = R . S
        T = R.dot(S).T

        trans_two_col = two_col.dot(np.linalg.inv(T))
        trans_two_col.columns = two_col.columns

        xxx = trans_two_col[col1].append(trans_two_col[col2], ignore_index=True)

        yyy = yyy.append(xxx, ignore_index=True)

        from matplotlib import pyplot as plt

        x_gauss: np.ndarray = np.arange(-6, 6, 0.001)
        gaussian: np.ndarray = local_normalization_tools \
            .gaussian_distribution(0, 1, x_gauss)

        plot_log = yyy.plot(kind='density', figsize=(16, 9),
                                          logy=True, legend=False)
        plt.semilogy(x_gauss, gaussian, lw=5)
        plt.xlim(-5, 5)
        plt.ylim(10 ** -5, 10)
        figure_log: plt.Figure = plot_log.get_figure()
        plt.show()

        corr_matrix_df: pd.DataFrame = data.corr()

        Saving data
        local_normalization_tools \
            .save_data(corr_matrix_df, function_name, dates, time_step, window)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

    except TypeError as error:
        print('To compute the correlation is needed at least to stocks')
        print(error)
        print()

# ----------------------------------------------------------------------------


def ln_aggregated_dist_returns_pair_data(dates: List[str], time_step: str,
                                         window: str) -> None:
    """Uses local normalization to compute the aggregated distribution of
       returns.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_aggregated_dist_returns_pair_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, dates, time_step, window)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        yyy = pd.DataFrame()
        for col1 in data.columns:
            for col2 in data.columns:

                if col1 == col2:
                    pass
                else:
                    two_col = data[[col1, col2]]
                    cov_two_col = two_col.cov()
                    eVa, eVe = np.linalg.eig(cov_two_col)

                    # R: rotation, S: scaling
                    # eVe:  eigenvector, eVa: eigenvalues
                    R, S = eVe, np.diag(np.sqrt(eVa))
                    # T: transformation matrix
                    # T = R . S
                    T = R.dot(S).T

                    trans_two_col = two_col.dot(np.linalg.inv(T))
                    trans_two_col.columns = two_col.columns

                    xxx = trans_two_col[col1].append(trans_two_col[col2], ignore_index=True)

                    yyy = yyy.append(xxx, ignore_index=True)

        from matplotlib import pyplot as plt

        x_gauss: np.ndarray = np.arange(-6, 6, 0.001)
        gaussian: np.ndarray = local_normalization_tools \
            .gaussian_distribution(0, 1, x_gauss)

        plot_log = yyy.plot(kind='density', figsize=(16, 9),
                                          logy=True, legend=False)
        plt.semilogy(x_gauss, gaussian, lw=5)
        plt.xlim(-5, 5)
        plt.ylim(10 ** -5, 10)
        figure_log: plt.Figure = plot_log.get_figure()
        plt.show()

        corr_matrix_df: pd.DataFrame = data.corr()

        Saving data
        local_normalization_tools \
            .save_data(corr_matrix_df, function_name, dates, time_step, window)

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

    dates = ['1992-01', '2012-12']
    time_step = '1d'
    window = '25'

    ln_aggregated_dist_returns_pair_data(dates, time_step, window)

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
