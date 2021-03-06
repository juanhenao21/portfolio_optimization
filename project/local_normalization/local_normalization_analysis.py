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

from itertools import product as iprod
from itertools import combinations as icomb
import multiprocessing as mp
import pickle
from typing import Any, Iterator, List, Tuple

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
            f'../data/local_normalization/ln_normalized_returns_data'
            + f'_{dates[0]}_{dates[1]}_step_{time_step}_win_{window}.pickle',
            'rb'))

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


def ln_aggregated_dist_returns_pair_data(dates: List[str], time_step: str,
                                         cols: List[str],
                                         window: str) -> List[float]:
    """Uses local normalization to compute the aggregated distribution of
       returns for a pair of stocks.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param cols: pair of stocks to be analized (i. e. ('AAPL', 'MSFT')).
    :param window: window time to compute the volatility (i.e. '60').
    :return: pd.Series -- The function returns a pandas dataframe.
    """

    try:

        # Load data
        two_col: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb'))[[cols[0], cols[1]]]

        agg_ret_mkt_list: List[float] = []

        two_col['DateCol'] = two_col.index
        two_col['Group'] = two_col.groupby(
            pd.Grouper(key='DateCol', freq=window + 'B'))['DateCol'] \
            .transform('first')

        for local_data in two_col.groupby(by=['Group']):

            local_data_df: pd.DataFrame = local_data[1][[cols[0], cols[1]]]
            cov_two_col: pd.DataFrame = local_data_df.cov()
            # eig_vec:  eigenvector, eig_val: eigenvalues
            eig_val, eig_vec = np.linalg.eig(cov_two_col)

            # rot: rotation, scal: scaling
            rot, scale = eig_vec, np.diag(1 / np.sqrt(eig_val))
            # trans: transformation matrix
            # trans = rot . scal
            trans = rot.dot(scale)

            try:
                trans_two_col = local_data_df.dot(trans)
                trans_two_col.columns = [cols[0], cols[1]]

                one_col = trans_two_col[cols[0]].append(trans_two_col[cols[1]],
                                                        ignore_index=True)

                agg_ret_mkt_list.extend(one_col)

                del local_data_df
                del one_col
                del trans_two_col

            except np.linalg.LinAlgError as error:
                print(error)
                print()

        del two_col

        return agg_ret_mkt_list

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# ----------------------------------------------------------------------------


def ln_aggregated_dist_returns_market_data(dates: List[str], time_step: str,
                                           window: str) -> None:
    """Computes the aggregated distribution of returns for a market.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60').
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    function_name: str = ln_aggregated_dist_returns_market_data.__name__
    local_normalization_tools \
        .function_header_print_data(function_name, dates, time_step, window)

    try:

        # Load data
        stocks_name: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/returns_data_{dates[0]}_{dates[1]}'
            + f'_step_{time_step}.pickle', 'rb')).columns[:20]

        agg_ret_mkt_list: List[float] = []

        stocks_comb: Iterator[Tuple[Any, ...]] = icomb(stocks_name, 2)
        args_prod: Iterator[Any] = iprod([dates], [time_step], stocks_comb,
                                         [window])

        with mp.Pool(processes=mp.cpu_count()) as pool:
            agg_ret_mkt_list.extend(pool.starmap(
                ln_aggregated_dist_returns_pair_data, args_prod))

        agg_ret_mkt_list_flat = [val for sublist in agg_ret_mkt_list for val in sublist]
        agg_ret_mkt_series: pd.Series = pd.Series(agg_ret_mkt_list_flat)

        # Saving data
        local_normalization_tools \
            .save_data(agg_ret_mkt_series, function_name, dates, time_step,
                       window)

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

    # ln_aggregated_dist_returns_pair_data(['1992-01', '2012-12'], '1d', ['AAPL', 'MSFT'], '25')
    ln_aggregated_dist_returns_market_data(['1992-01', '2012-12'], '1d', '25')


# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
