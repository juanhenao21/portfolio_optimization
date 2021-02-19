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

import correlation_matrix_analysis
import correlation_matrix_plot
import correlation_matrix_tools

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    correlation_matrix_tools.initial_message()

    # Initial year and time step
    year = '1980'
    time_step = '1d'

    # Basic folders
    correlation_matrix_tools.start_folders(year, time_step)

    # Run analysis
    # Analysis and plot
    correlation_matrix_analysis.returns_data(year, time_step)
    correlation_matrix_analysis.normalized_returns_data(year, time_step)
    correlation_matrix_analysis.correlation_matrix_data(year, time_step)

    correlation_matrix_plot.returns_plot(year, time_step)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
