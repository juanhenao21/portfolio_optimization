'''Portfolio optimization correlation matrix plot module.

The functions in the module plot the data obtained in the
correlation_matrix_analysis module.

This script requires the following modules:
    * gc
    * pickle
    * typing
    * matplotlib
    * numpy
    * pandas
    * seaborn
    * correlation_matrix_tools

The module contains the following functions:
    * returns_plot - plots the returns of five stocks.
    * normalized_returns_plot - plots the normalized returns of five stocks.
    * normalized_returns_distribution_plot - plots the normalized returns
      distribution of five stocks.
    * matrix_correlation_plot - plots the correlation matrix.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import gc
import pickle
from typing import List

from matplotlib import pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore

import correlation_matrix_tools

# -----------------------------------------------------------------------------


def returns_plot(dates: List[str], time_step: str) -> None:
    """Plots the returns of five stocks.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = returns_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, dates, time_step)

    try:

        # Load data
        returns_data: pd.DataFrame = pickle.load(open(
                        f'../data/correlation_matrix/returns_data_{dates[0]}'
                        + f'_{dates[1]}_step_{time_step}.pickle', 'rb')) \
                        .iloc[:, :5]

        plot: np.ndarray = returns_data.plot(subplots=True, sharex=True,
                                             figsize=(16, 16), grid=True,
                                             sort_columns=True)

        _ = [ax.set_ylabel('Returns', fontsize=20) for ax in plot]
        _ = [plot.legend(loc=1, fontsize=20) for plot in plt.gcf().axes]
        plt.title(f'Returns from {dates[0]} to {dates[1]} - {time_step}',
                  fontsize=30)
        plt.xlabel(f'Date - {time_step}', fontsize=20)
        plt.tight_layout(pad=0.5)
        figure: plt.Figure = plot[0].get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, dates, time_step)

        plt.close()
        del returns_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def normalized_returns_plot(dates: List[str], time_step: str) -> None:
    """Plots the normalized returns of five stocks.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, dates, time_step)

    try:

        # Load data
        norm_returns_data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{dates[0]}'
            + f'_{dates[1]}_step_{time_step}.pickle', 'rb')).iloc[:, :5]

        plot: np.ndarray = norm_returns_data.plot(subplots=True, sharex=True,
                                                  figsize=(16, 16), grid=True,
                                                  sort_columns=True)

        _ = [ax.set_ylabel('Norm. Returns', fontsize=20) for ax in plot]
        _ = [plot.legend(loc=1, fontsize=20) for plot in plt.gcf().axes]
        plt.xlabel(f'Date - {time_step}', fontsize=20)
        plt.tight_layout(pad=0.5)
        figure: plt.Figure = plot[0].get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, dates, time_step)

        plt.close()
        del norm_returns_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def normalized_returns_distribution_plot(dates: List[str],
                                         time_step: str) -> None:
    """Plots the normalized returns distribution of five stocks.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_distribution_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, dates, time_step)

    try:

        # Load data
        norm_returns_data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{dates[0]}'
            + f'_{dates[1]}_step_{time_step}.pickle', 'rb')).iloc[:, :5]

        x_gauss: np.ndarray = np.arange(-6, 6, 0.001)
        gaussian: np.ndarray = correlation_matrix_tools \
            .gaussian_distribution(0, 1, x_gauss)

        # Linear plot
        plot_lin = norm_returns_data.plot(kind='density', figsize=(16, 9))

        plt.plot(x_gauss, gaussian, lw=5, label='Gaussian')
        plt.title(f'Normalized returns distribution from {dates[0]} to'
                  + f' {dates[1]} - {time_step}', fontsize=30)
        plt.legend(loc=1, fontsize=20)
        plt.xlabel('Returns', fontsize=25)
        plt.ylabel('Counts', fontsize=25)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlim(-5, 5)
        plt.grid(True)
        plt.tight_layout()
        figure_lin: plt.Figure = plot_lin.get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure_lin, function_name + '_lin', dates, time_step)

        plt.close()
        del figure_lin
        del plot_lin

        # Log plot
        plot_log = norm_returns_data.plot(kind='density', figsize=(16, 9),
                                          logy=True)

        plt.semilogy(x_gauss, gaussian, lw=5, label='Gaussian')
        plt.title(f'Normalized returns distribution from {dates[0]} to'
                  + f' {dates[1]} - {time_step}', fontsize=30)
        plt.legend(loc=1, fontsize=20)
        plt.xlabel('Returns', fontsize=25)
        plt.ylabel('Counts', fontsize=25)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlim(-5, 5)
        plt.ylim(10 ** -6, 10)
        plt.grid(True)
        plt.tight_layout()
        figure_log: plt.Figure = plot_log.get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure_log, function_name + '_log', dates, time_step)

        plt.close()
        del norm_returns_data
        del figure_log
        del plot_log
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# ----------------------------------------------------------------------------


def correlation_matrix_plot(dates: List[str], time_step: str) -> None:
    """Plots the correlation matrix of the normalized returns.

    :param dates: List of the interval of dates to be analyzed
     (i.e. ['1980-01', '2020-12']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = correlation_matrix_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, dates, time_step)

    try:

        figure: plt.figure = plt.figure(figsize=(16, 9))

        # Load data
        correlations: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/correlation_matrix_data_{dates[0]}'
            + f'_{dates[1]}_step_{time_step}.pickle', 'rb'))

        sns.heatmap(correlations, cmap='Blues')#, vmin=-1, vmax=1)

        plt.title(f'Correlation matrix from {dates[0]} to {dates[1]} -'
                  + f' {time_step}', fontsize=30)
        plt.yticks(rotation=45)
        plt.xticks(rotation=45)

        figure.tight_layout()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, dates, time_step)

        plt.close()
        del correlations
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
