'''Portfolio optimization correlation matrix main module.

The functions in the module compute the returns and correlation matrix of
financial time series.

This script requires the following modules:
    * typing
    * correlation_matrix_analysis
    * correlation_matrix_plot
    * correlation_matrix_tools

The module contains the following functions:
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from typing import List
import multiprocessing as mp
from itertools import product as iprod

import correlation_matrix_analysis
import correlation_matrix_plot
import correlation_matrix_tools

# -----------------------------------------------------------------------------


def data_plot_generator(years: List[str], time_step: List[str]) -> None:
    """Generates all the analysis and plots from the data.
    :param years: list of the string of the year to be analyzed
     (i.e. ['2016', '2017']).
    :param time_steps: list of the string of the time step of the data
     (i.e. ['1m', '2m', '5m']).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Parallel computing
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # Specific functions
        pool.starmap(correlation_matrix_analysis
                     .returns_data, iprod(years, time_step))
        pool.starmap(correlation_matrix_analysis
                     .returns_data, iprod(years, time_step))
        pool.starmap(correlation_matrix_analysis
                     .normalized_returns_data, iprod(years, time_step))
        pool.starmap(correlation_matrix_analysis
                     .correlation_matrix_data, iprod(years, time_step))

        # Plot
        pool.starmap(correlation_matrix_plot
                     .returns_plot, iprod(years, time_step))
        pool.starmap(correlation_matrix_plot
                     .normalized_returns_plot, iprod(years, time_step))
        pool.starmap(correlation_matrix_plot
                     .normalized_returns_distribution_plot,
                     iprod(years, time_step))
        pool.starmap(correlation_matrix_plot
                     .correlation_matrix_plot, iprod(years, time_step))

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    correlation_matrix_tools.initial_message()

    # Initial year and time step
    years: List[str] = ['1980']
    time_steps: List[str] = ['1d']

    # Basic folders
    correlation_matrix_tools.start_folders()

    # Run analysis
    # Analysis and plot
    data_plot_generator(years, time_steps)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
