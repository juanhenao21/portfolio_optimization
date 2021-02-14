'''HIST data main module.

The functions in the module compute the responses of the Historic Rate data
from HIST Capital in a year.

This script requires the following modules:
    * itertools
    * multiprocessing
    * typing
    * hist_data_analysis_responses_physical
    * hist_data_plot_responses_physical
    * hist_data_tools_responses_physical

The module contains the following functions:
    * hist_data_plot_generator - generates all the analysis and plots from the
      HIST data.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

from typing import List

import hist_data_analysis_matrices_physical
import hist_data_plot_matrices_physical
import hist_data_tools_matrices_physical

# -----------------------------------------------------------------------------


def hist_data_plot_generator(fx_pairs: List[str], years: List[str],
                             intervals: List[str]) -> None:
    """Generates all the analysis and plots from the HIST data.

    :param fx_pairs: list of the string abbreviation of the forex pairs to be
     analyzed (i.e. ['eur_usd', 'gbp_usd']).
    :param years: list of the string of the year to be analyzed
     (i.e. ['2016', '2017']).
    :param intervals: list of string of the interval to be analyzed
     (i.e. ['week', 'month', 'quarter', 'year'])
    :return: None -- The function saves the data in a file and does not return
     a value.
    """

    # Specific functions
    year: str
    for year in years:
        # hist_data_analysis_matrices_physical. \
        #     hist_fx_returns_year_physical_data(fx_pairs, year)

        interval: str
        for interval in intervals:
            # hist_data_analysis_matrices_physical. \
            #     hist_fx_correlations_physical_data(year, interval)

            hist_data_plot_matrices_physical. \
                hist_fx_correlations_physical_plot(year, interval)

            # hist_data_plot_matrices_physical. \
            #     hist_fx_returns_distributions_physical_plot(year, interval)

# -----------------------------------------------------------------------------


def main() -> None:
    """The main function of the script.

    The main function extract, analyze and plot the data.

    :return: None.
    """

    hist_data_tools_matrices_physical.hist_initial_message()

    # Forex pairs and weeks to analyze
    # Response function analysis
    # The other years will be downloaded with the spread data
    years: List[str] = ['2019']
    fx_pairs: List[str] = ['eur_usd', 'gbp_usd', 'usd_jpy', 'aud_usd',
                           'usd_chf', 'usd_cad', 'nzd_usd']
    intervals: List[str] = ['week', 'month', 'quarter', 'year']

    # Basic folders
    hist_data_tools_matrices_physical.hist_start_folders(years)

    # Run analysis
    # Analysis and plot
    hist_data_plot_generator(fx_pairs, years, intervals)

    print('Ay vamos!!!')

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
