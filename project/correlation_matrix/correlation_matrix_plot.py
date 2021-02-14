'''HIST data plot module.

The functions in the module plot the data obtained in the
hist_data_analysis_responses_physical module.

This script requires the following modules:
    * gc
    * pickle
    * matplotlib
    * numpy
    * pandas
    * hist_data_tools_data_extract

The module contains the following functions:
    * hist_fx_returns_distributions_physical_plot - plots the correlation
      matrices.
    * hist_fx_correlations_physical_plot - plots the correlation matrices.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# -----------------------------------------------------------------------------
# Modules

import gc
import pickle

from matplotlib import pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore

import hist_data_tools_matrices_physical

# -----------------------------------------------------------------------------


def hist_fx_returns_distributions_physical_plot(year: str,
                                                interval: str) -> None:
    """Plots the returns distribution for different intervals of time.

    :param year: string of the year to be analyzed (i.e. '2016').
    :param interval: string of the interval to be analyzed (i.e. 'week',
     'month', 'quarter', 'year')
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = \
        hist_fx_returns_distributions_physical_plot.__name__
    hist_data_tools_matrices_physical \
        .hist_function_header_print_plot(function_name, year, 'returns')

    try:

        freq: str
        periods: int
        if interval == 'week':
            freq = 'W'
            periods = 52
        elif interval == 'month':
            freq = 'MS'
            periods = 12
        else:
            freq = 'QS'
            periods = 4

        # Load data
        fx_returns: pd.DataFrame = pickle.load(open(
                        f'../../hist_data/matrices_physical_{year}/hist_fx'
                        + f'_matrices_physical_data/hist_fx_returns_matrices'
                        + f'_physical_data_{year}.pickle', 'rb'))

        fx_returns.fillna(0, inplace=True)

        x_gauss = np.arange(-5, 5, 0.001)
        gaussian: np.ndarray = hist_data_tools_matrices_physical \
            .gaussian_distribution(0, 1, x_gauss)

        figure: plt.figure = plt.figure(figsize=(16, 9))

        if interval == 'year':
            fx_returns_norm: pd.DataFrame = (fx_returns - fx_returns.mean()) \
                                            / fx_returns.std()

            # pair: str
            # for pair in fx_returns_norm.columns:
            #     plt.hist(fx_returns_norm[pair], 100, (-4, 4), density=True)
            #     # fx_returns_norm.plot(kind='kde')
            fx_returns_norm.plot(kind='density')

            # plt.plot(x_gauss, gaussian, lw=10, label='Gaussian')
            plt.xlabel('Returns', fontsize=35)
            plt.ylabel('Counts', fontsize=35)
            plt.xticks(fontsize=25)
            plt.yticks(fontsize=25)
            plt.grid(True)
            plt.tight_layout()

            # Plotting
            hist_data_tools_matrices_physical \
                .hist_save_plot(function_name, figure, year, interval)

            plt.close()
            del fx_returns_norm
            del figure
            gc.collect()

        # else:
        #     time_int: pd.DatetimeIndex = \
        #         pd.date_range(f'{year}-01-01', periods=periods, freq=freq)

        #     t_idx: int
        #     t_idx_str: str

        #     for t_idx in range(1, periods):
        #         fx_returns_period: pd.DataFrame = \
        #             fx_returns[time_int[t_idx - 1]: time_int[t_idx]]
        #         fx_returns_norm =  \
        #             (fx_returns_period - fx_returns_period.mean()) \
        #                 / fx_returns_period.std()

        #         rename_df = {col: f'{col}_{interval}_{t_idx}' \
        #             for col in fx_returns_norm.columns}
        #         fx_returns_norm.rename(columns=rename_df, inplace=True)

        #         fx_returns_norm.plot.kde()

        #     plt.plot(x_gauss, gaussian, lw=10, label='Gaussian')
        #     plt.xlabel('Returns', fontsize=35)
        #     plt.ylabel('Counts', fontsize=35)
        #     plt.xticks(fontsize=25)
        #     plt.yticks(fontsize=25)
        #     plt.grid(True)
        #     plt.tight_layout()

        #     if t_idx < 10:
        #         t_idx_str = f'0{t_idx}'
        #     else:
        #         t_idx_str = f'{t_idx}'

        #     # Plotting
        #     hist_data_tools_matrices_physical \
        #         .hist_save_data(function_name, figure, year, interval)

        #     plt.close()
        #     del fx_returns_norm
        #     del figure
        #     gc.collect()

    except FileNotFoundError as error:
        print('No data')
        print(error)
        print()

# ----------------------------------------------------------------------------


def hist_fx_correlations_physical_plot(year: str, interval: str) -> None:
    """Plots the correlation matrix for different intervals of time.

    :param year: string of the year to be analyzed (i.e. '2016').
    :param interval: string of the interval to be analyzed (i.e. 'week',
     'month', 'quarter', 'year')
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    function_name: str = \
        hist_fx_correlations_physical_plot.__name__
    hist_data_tools_matrices_physical \
        .hist_function_header_print_plot(function_name, year, kind='correlations')

    try:

        periods: int
        n_cols: int
        n_rows: int
        if interval == 'week':
            periods = 52
            n_cols = 13
            n_rows = 4
        elif interval == 'month':
            periods = 12
            n_cols = 4
            n_rows = 3
        elif interval == 'quarter':
            periods = 4
            n_cols = 2
            n_rows = 2
        else:
            periods = 1
            n_cols = 1
            n_rows = 1

        figure: plt.figure = plt.figure(figsize=(16, 9))
        cbar_ax: plt.axes = figure.add_axes([0.91, 0.3, 0.03, 0.4])

        for per in range(1, periods + 1):

            if per < 10:
                per_str: str = f'0{per}'
            else:
                per_str = f'{per}'

            # Load data
            corr: pd.DataFrame = pickle.load(open(
                f'../../hist_data/matrices_physical_{year}/hist_fx_matrices'
                + f'_physical_data/hist_fx_corr_physical_data_{year}_int'
                + f'_{interval}_{per_str}.pickle', 'rb'))

            ax_sub = plt.subplot(n_rows, n_cols, per)

            if interval in ('week', 'month'):
                sns.heatmap(corr, ax=ax_sub, cbar=per == 1,
                            cbar_ax=None if (per-1) else cbar_ax,
                            vmin=-1, vmax=1)

            else:
                sns.heatmap(corr, annot=True, ax=ax_sub, cbar=per == 1,
                            cbar_ax=None if (per-1) else cbar_ax,
                            vmin=-1, vmax=1)

            if interval == 'week':
                ax_sub.tick_params(axis='x', bottom=False, labelbottom=False)
                ax_sub.tick_params(axis='y', left=False, labelleft=False)

            plt.yticks(rotation=45)
            plt.xticks(rotation=45)

        figure.tight_layout(rect=[0, 0, .9, 1])

        # Plotting
        hist_data_tools_matrices_physical \
            .hist_save_plot(function_name, figure, year, interval)

        plt.close()
        del corr
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

    hist_fx_returns_distributions_physical_plot('2019', 'year')

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
