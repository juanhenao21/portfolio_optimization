'''HIST data tools module.

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
    * hist_save_data - saves computed data.
    * hist_save_plot - saves figures.
    * hist_function_header_print_data - prints info about the function running.
    * hist_function_header_print_plot - prints info about the plot.
    * hist_start_folders - creates folders to save data and plots.
    * hist_initial_message - prints the initial message with basic information.
    * hist_weeks - tuple with the numbers from 1 to 53 representing the weeks.
    * gaussian_distribution - compute gaussian distribution values.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import os
import pickle
from typing import Any, List, Tuple

from matplotlib import pyplot as plt  # type: ignore
import numpy as np  # type: ignore

# -----------------------------------------------------------------------------


def hist_save_data(data: Any, year: str, interval: str, period: str) -> None:
    """Saves computed data in pickle files.

    Saves the data generated in the functions of the
    hist_data_analysis_matrices_physical module in pickle files.

    :param data: data to be saved. The data can be of different types.
    :param year: string of the year to be analyzed (i.e '2016').
    :param interval: string of the interval to be analyzed (i.e. 'week',
     'month', 'quarter', 'year')
    :param period: location in the interval (i. e. '01')
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Saving data

    if (not os.path.isdir(
            f'../../hist_data/matrices_physical_{year}/hist_fx_matrices'
            + f'_physical_data/')):

        try:
            os.mkdir(
                f'../../hist_data/matrices_physical_{year}/hist_fx_matrices'
                + f'_physical_data/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    pickle.dump(data, open(
        f'../../hist_data/matrices_physical_{year}/hist_fx_matrices_physical'
                + f'_data/hist_fx_corr_physical_data_{year}_int_{interval}'
                + f'_{period}.pickle', 'wb'))

    print('Data Saved')
    print()

# -----------------------------------------------------------------------------


def hist_save_plot(function_name: str, figure: plt.Figure, year: str,
                   interval: str) -> None:
    """Saves plot in png files.

    Saves the plot generated in the functions of the
    hist_data_plot_matrices_trade module in png files.

    :param function_name: name of the function that generates the plot.
    :param figure: figure object that is going to be save.
    :param year: string of the year to be analyzed (i.e '2016').
    :param interval: string of the interval to be analyzed (i.e. 'week',
     'month', 'quarter', 'year')
    :return: None -- The function save the plot in a file and does not return
     a value.
    """

    # Saving plot data

    if (not os.path.isdir(
            f'../../hist_plot/matrices_physical_{year}/{function_name}/')):

        try:
            os.mkdir(f'../../hist_plot/matrices_physical_{year}/'
                     + f'{function_name}/')
            print('Folder to save data created')

        except FileExistsError:
            print('Folder exists. The folder was not created')

    figure.savefig(f'../../hist_plot/matrices_physical_{year}'
                   + f'/{function_name}/{function_name}'
                   + f'_{year}_{interval}.png')

    print('Plot saved')
    print()

# -----------------------------------------------------------------------------


def hist_function_header_print_data(function_name: str, year: str,
                                    kind: str) -> None:
    """Prints a header of a function that generates data when it is running.

    :param function_name: name of the function that generates the data.
    :param year: string of the year to be analyzed (i.e '2016').
    :param kind: kind of analysis (i.e 'returns').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('HIST data')
    print(function_name)

    if kind == 'returns':
        print(f'Processing the returns in the year {year}')
        print()
    else:
        print(f'Processing correlation matrices in the year {year}')
        print()

# -----------------------------------------------------------------------------


def hist_function_header_print_plot(function_name: str, year: str,
                                    kind: str) -> None:
    """Prints a header of a function that generates a plot when it is running.

    :param function_name: name of the function that generates the plot.
    :param year: string of the year to be analyzed (i.e '2016').
    :param kind: kind of analysis (i.e 'returns').
    :return: None -- The function prints a message and does not return a
     value.
    """

    print('HIST data')
    print(function_name)

    if kind == 'returns':
        print(f'Processing plot for returns in the year {year}')
        print()
    else:
        print(f'Processing plot for correlation matrices in {year}')
        print()

# -----------------------------------------------------------------------------


def hist_start_folders(years: List[str]) -> None:
    """Creates the initial folders to save the data and plots.

    :param years: List of the strings of the year to be analyzed
     (i.e ['2016', '2017']).
    :return: None -- The function creates folders and does not return a value.
    """

    year: str
    for year in years:

        try:
            os.mkdir(f'../../hist_data/matrices_physical_{year}')
            os.mkdir(f'../../hist_plot/matrices_physical_{year}')
            print('Folder to save data created')
            print()

        except FileExistsError as error:
            print('Folder exists. The folder was not created')
            print(error)

# -----------------------------------------------------------------------------


def hist_initial_message() -> None:
    """Prints the initial message with basic information.

    :return: None -- The function prints a message and does not return a value.
    """

    print()
    print('#####################################')
    print('HIST Matrices Physical Time Analysis')
    print('#####################################')
    print('AG Guhr')
    print('Faculty of Physics')
    print('University of Duisburg-Essen')
    print('Author: Juan Camilo Henao Londono')
    print('More information in:')
    print('* https://juanhenao21.github.io/')
    print('* https://github.com/juanhenao21/forex_matrices')
    # print('* https://forex-response_spread-year.readthedocs.io/en/latest/')
    print()

# -----------------------------------------------------------------------------


def hist_weeks() -> Tuple[str, ...]:
    """Generates a tuple with the numbers from 1 to 53 representing the weeks
       in a year.

    :return: tuple.
    """

    week_num = []

    val: int
    for val in range(1, 54):
        if val < 10:
            val_str: str = f'0{val}'
            week_num.append(f'{val_str}')
        else:
            week_num.append(f'{val}')

    return tuple(week_num)

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
