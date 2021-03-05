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
    * volatility_plot - plots the volatility of five stocks.
    * normalized_returns_plot - plots the normalized returns of five stocks.
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


def returns_plot(years: List[str], time_step: str) -> None:
    """Plots the returns of five stocks.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = returns_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, years, time_step)

    try:

        # Load data
        returns_data: pd.DataFrame = pickle.load(open(
                        f'../data/correlation_matrix/returns_data_{years[0]}'
                        + f'_{years[1]}_step_{time_step}.pickle', 'rb')) \
                        .iloc[:, :5]

        plot: np.ndarray = returns_data.plot(subplots=True, sharex=True,
                                             figsize=(16, 16), grid=True,
                                             sort_columns=True)

        _ = [ax.set_ylabel('Returns', fontsize=20) for ax in plot]
        _ = [plot.legend(loc=1, fontsize=20) for plot in plt.gcf().axes]
        plt.title(f'Returns from {years[0]} to {years[1]} - {time_step}',
                  fontsize=30)
        plt.xlabel(f'Date - {time_step}', fontsize=20)
        plt.tight_layout(pad=0.5)
        figure: plt.Figure = plot[0].get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, years, time_step)

        plt.close()
        del returns_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def volatility_plot(years: List[str], time_step: str, window: str) -> None:
    """Plots the volatility of five stocks.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :param window: window time to compute the volatility (i.e. '60', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = volatility_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, years, time_step)

    try:

        # Load data
        volatility_data: pd.DataFrame = pickle.load(open(
                        f'../data/correlation_matrix/volatility_data_win'
                        + f'_{window}_{years[0]}_{years[1]}_step_{time_step}'
                        + f'.pickle', 'rb')).iloc[:, :5]

        plot: np.ndarray = volatility_data.plot(subplots=True, sharex=True,
                                                figsize=(16, 16), grid=True,
                                                sort_columns=True)

        _ = [ax.set_ylabel('Volatility', fontsize=20) for ax in plot]
        _ = [plot.legend(loc=1, fontsize=20) for plot in plt.gcf().axes]
        plt.title(f'Volatility from {years[0]} to {years[1]} - {time_step}'
                  + f' - time window {window}', fontsize=30)
        plt.xlabel(f'Date - {time_step} - time window {window}', fontsize=20)
        plt.tight_layout(pad=0.5)
        figure: plt.Figure = plot[0].get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, years, time_step)

        plt.close()
        del volatility_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# -----------------------------------------------------------------------------


def normalized_returns_plot(years: List[str], time_step: str) -> None:
    """Plots the normalized returns of five stocks.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, years, time_step)

    try:

        # Load data
        norm_returns_data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{years[0]}'
            + f'_{years[1]}_step_{time_step}.pickle', 'rb')).iloc[:, :5]

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
            .save_plot(figure, function_name, years, time_step)

        plt.close()
        del norm_returns_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()


# -----------------------------------------------------------------------------


def normalized_returns_distribution_plot(years: List[str],
                                         time_step: str) -> None:
    """Plots the normalized returns distribution of five stocks.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = normalized_returns_distribution_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name + 'lin', years, time_step)

    try:

        # Load data
        norm_returns_data: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/normalized_returns_data_{years[0]}'
            + f'_{years[1]}_step_{time_step}.pickle', 'rb')).iloc[:, :5]

        x_gauss: np.ndarray = np.arange(-6, 6, 0.001)
        gaussian: np.ndarray = correlation_matrix_tools \
            .gaussian_distribution(0, 1, x_gauss)

        # Linear plot
        plot = norm_returns_data.plot(kind='density', figsize=(16, 9))

        plt.plot(x_gauss, gaussian, lw=5, label='Gaussian')
        plt.title(f'Normalized returns distribution from {years[0]} to'
                  + f' {years[1]} - {time_step}', fontsize=30)
        plt.legend(loc=1, fontsize=20)
        plt.xlabel('Returns', fontsize=25)
        plt.ylabel('Counts', fontsize=25)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlim(-4, 4)
        plt.grid(True)
        plt.tight_layout()
        figure: plt.Figure = plot.get_figure()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name + '_lin', years, time_step)

        plt.close()
        del figure

        # Log plot
        figure = plt.figure(figsize=(16, 9))
        plt.hist(norm_returns_data, 100, (-5, 5), density=True, log=True,
                 histtype='step', label=norm_returns_data.columns)
        plt.plot(x_gauss, gaussian, lw=5, label='Gaussian')
        plt.title(f'Normalized returns distribution from {years[0]} to'
                  + f' {years[1]} - {time_step}', fontsize=30)

        plt.legend(loc='lower center', fontsize=20)
        plt.xlabel('Returns', fontsize=25)
        plt.ylabel('Counts', fontsize=25)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlim(-5, 5)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name + '_log', years, time_step)

        plt.close()
        del norm_returns_data
        del figure
        gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# ----------------------------------------------------------------------------


def correlation_matrix_plot(years: List[str], time_step: str) -> None:
    """Plots the correlation matrix of the normalized returns.

    :param years: List of the interval of years to be analyzed
     (i.e. ['1980', '2020']).
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = correlation_matrix_plot.__name__
    correlation_matrix_tools \
        .function_header_print_plot(function_name, years, time_step)

    try:

        figure: plt.figure = plt.figure(figsize=(16, 9))

        # Load data
        correlations: pd.DataFrame = pickle.load(open(
            f'../data/correlation_matrix/correlation_matrix_data_{years[0]}'
            + f'_{years[1]}_step_{time_step}.pickle', 'rb'))

        sns.heatmap(correlations, vmin=-1, vmax=1)

        plt.title(f'Correlation matrix from {years[0]} to {years[1]} -'
                  + f' {time_step}', fontsize=30)
        plt.yticks(rotation=45)
        plt.xticks(rotation=45)

        figure.tight_layout()

        # Plotting
        correlation_matrix_tools \
            .save_plot(figure, function_name, years, time_step)

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
