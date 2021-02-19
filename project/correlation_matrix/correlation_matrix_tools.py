'''Portfolio optimization correlation matrix tools module.

The functions in the module do small repetitive tasks, that are used along the
whole implementation. These tools improve the way the tasks are standardized
in the modules that use them.

This script requires the following modules:
    * os
    * pickle
    * typing
    * matplotlib
    * numpy

The module contains the following functions:
    * save_data - saves computed data.
    * save_plot - saves figures.
    * function_header_print_data - prints info about the function running.
    * function_header_print_plot - prints info about the plot.
    * start_folders - creates folders to save data and plots.
    * initial_message - prints the initial message with basic information.
    * gaussian_distribution - compute gaussian distribution values.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
import pickle
from typing import Any, List

from matplotlib import pyplot as plt  # type: ignore
import numpy as np  # type: ignore

# -----------------------------------------------------------------------------


def save_data(data: Any, function_name: str, year: str,
              time_step: str) -> None:
    """Saves computed data in pickle files.

    Saves the data generated in the functions of the
    correlation_matrix_analysis module in pickle files.

    :param data: data to be saved. The data can be of different types.
    :param function_name: name of the function that generates the plot.
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Saving data

    pickle.dump(data, open(
        f'../data/correlation_matrix/{function_name}_{year}_step_{time_step}'
                + f'.pickle', 'wb'))

    print('Data Saved')
    print()

# -----------------------------------------------------------------------------


def save_plot(figure: plt.Figure, function_name: str, year: str,
              time_step: str) -> None:
    """Saves plot in png files.

    Saves the plot generated in the functions of the
    correlation_matrix_analysis module in png files.

    :param figure: figure object that is going to be save.
    :param function_name: name of the function that generates the plot.
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    # Saving plot data

    figure.savefig(f'../plot/correlation_matrix/{function_name}_{year}_step'
                   + f'_{time_step}.png')

    print('Plot Saved')
    print()

# -----------------------------------------------------------------------------


def function_header_print_data(function_name: str, year: str,
                               time_step: str) -> None:
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('Portfolio Optimization')
    print(function_name)

    print(f'Computing the results of the data from the year {year} to the '
          + f'present in time steps of {time_step}')
    print()

# -----------------------------------------------------------------------------


def function_header_print_plot(function_name: str, year: str,
                               time_step: str) -> None:
    """Prints a header of a function that generates a plot when it is running.

    :param function_name: name of the function that generates the data.
    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('Portfolio Optimization')
    print(function_name)

    print(f'Computing the plots of the data from the year {year} to the '
          + f'present in time steps of {time_step}')
    print()

# -----------------------------------------------------------------------------


def start_folders(year: str, time_step: str) -> None:
    """Creates the initial folders to save the data and plots.

    :param year: initial year of the analysis (i.e. '1980').
    :param time_step: time step of the data (i.e. '1m', '2m', '5m', ...).
    :return: None -- The function creates folders and does not return a value.
    """

    try:
        os.mkdir(f'../data/correlation_matrix')
        os.mkdir(f'../plot/correlation_matrix')
        print('Folder to save data created')
        print()

    except FileExistsError as error:
        print('Folder exists. The folder was not created')
        print(error)
        print()

# -----------------------------------------------------------------------------


def initial_message() -> None:
    """Prints the initial message with basic information.

    :return: None -- The function prints a message and does not return a value.
    """

    print()
    print('##################')
    print('Correlation Matrix')
    print('##################')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('* https://juanhenao21.github.io/')
    print('* https://github.com/juanhenao21/portfolio_optimization')
    # print('* https://forex-response_spread-year.readthedocs.io/en/latest/')
    print()

# -----------------------------------------------------------------------------


def gaussian_distribution(mean, variance, x):
    return (1 / (2 * np.pi * variance) ** 0.5) \
        * np.exp(-((x - mean) ** 2) / (2 * variance))

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
