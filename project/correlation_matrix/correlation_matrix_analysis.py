'''Portfolio optimization correlation matrix analysis module.

The functions in the module compute the returns, the normalized returns and the
correlation matrix of financial time series.

This script requires the following modules:
    * itertools
    * multiprocessing
    * pickle
    * typing
    * numpy
    * pandas
    * correlation_matrix_tools

The module contains the following functions:
    * returns_data - computes the returns of the time series.
    * normalized_returns_data - normalizes the returns of the time series.
    * correlation_matrix_data - computes the correlation matrix of the
     normalized returns.
    * aggregated_dist_returns_pair_data - computes the aggregated distribution
      of returns for a pair of stocks.
    * aggregated_dist_returns_market_data - computes the aggregated
      distribution of returns for a market.
    * main - the main function of the script.

..moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''
# -----------------------------------------------------------------------------
# Modules

from itertools import product as iprod
from itertools import combinations as icomb
import multiprocessing as mp
import pickle
from typing import Any, Iterator, List, Tuple

import numpy as np  # type: ignore
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


def normalized_returns_data(dates: List[str], time_step: str) -> None:
    """Normalizes the returns of the time series.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, dates, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        normalized_df: pd.DataFrame = (data - data.mean()) / data.std()

        # Saving data
        correlation_matrix_tools \
            .save_data(normalized_df, function_name, dates, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def correlation_matrix_data(dates: List[str], time_step: str) -> None:
    """Computes the correlation matrix of the normalized returns.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = correlation_matrix_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, dates, time_step)

    try:

        # Load data
        data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{dates[0]}'
            + f'_{dates[1]}_step_{time_step}.pickle', 'rb'))

        corr_matrix_df: pd.DataFrame = data.corr()

        # Saving data
        correlation_matrix_tools \
            .save_data(corr_matrix_df, function_name, dates, time_step)

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

    except TypeError as error:
        print('To compute the correlation is needed at least two stocks')
        print(error)
        print()

# ----------------------------------------------------------------------------


def aggregated_dist_returns_pair_data(dates: List[str], time_step: str,
                                      cols: List[str]) -> pd.Series:
    """Computes the aggregated distribution of returns for a pair of stocks.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param cols: pair of stocks to be analized (i. e. ('AAPL', 'MSFT')).
    :return: pd.Series -- The function returns a pandas dataframe.
    """

    try:

        # Load data
        two_col: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))[[cols[0], cols[1]]]

        cov_two_col: pd.DataFrame = two_col.cov()
        # eig_vec:  eigenvector, eig_val: eigenvalues
        eig_val, eig_vec = np.linalg.eig(cov_two_col)

        # rot: rotation, scal: scaling
        rot, scal = eig_vec, np.diag(np.sqrt(eig_val))
        # trans: transformation matrix
        # trans = rot . scal
        trans = rot.dot(scal).T

        trans_two_col = two_col.dot(np.linalg.inv(trans))
        trans_two_col.columns = two_col.columns

        one_col = trans_two_col[cols[0]].append(trans_two_col[cols[1]],
                                                ignore_index=True)

        del two_col

        return one_col

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()
        return None

# ----------------------------------------------------------------------------


def aggregated_dist_returns_market_data(dates: List[str],
                                        time_step: str) -> None:
    """Computes the aggregated distribution of returns for a market.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = aggregated_dist_returns_market_data.__name__
    correlation_matrix_tools \
        .function_header_print_data(function_name, dates, time_step)

    try:

        # Load data
        stocks_name: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))

        agg_ret_mkt_list: List[pd.Series] = []

        stocks_perm: Iterator[Tuple[Any, ...]] = icomb(stocks_name, 2)
        args_prod: Iterator[Any] = iprod([dates], [time_step], stocks_perm)

        with mp.Pool(processes=mp.cpu_count()) as pool:
            agg_ret_mkt_list.extend(pool.starmap(
                aggregated_dist_returns_pair_data, args_prod))

        agg_ret_mkt_series = pd.concat(agg_ret_mkt_list, ignore_index=True)

        # Saving data
        correlation_matrix_tools \
            .save_data(agg_ret_mkt_series, function_name, dates, time_step)

        del agg_ret_mkt_list
        del agg_ret_mkt_series

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
