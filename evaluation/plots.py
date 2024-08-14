# /**
#  * Use Case Cardiology HiGHmed Data Anonymisation
#  * Copyright (C) 2023 - Berlin Institute of Health
#  * <p>
#  * Use of this software is govered by the Business Source License included in the LICENSE.md file.
#  * Change Date: 14.08.2028, Change License: Academic Free License v3.0
#  * On the date above, in accordance with the Business Source License, use of this software will be governed by the
#  * open source license AFL v3.0 or as specified in the LICENSE.md file.
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def ecdf_values(value_list):
    x_ecdf = np.sort(value_list)
    y_ecdf = np.arange(1, len(value_list)+1) / len(value_list)
    return x_ecdf, y_ecdf


def ecdf_plot(orig, anon, synth, combined, xlabel='', save_to='ecdf_plot.png'):
    x_orig, y_orig = ecdf_values(orig)
    x_anon, y_anon = ecdf_values(anon)
    x_synth, y_synth = ecdf_values(synth)
    x_combined, y_combined = ecdf_values(combined)

    plt.clf()
    _, ax = plt.subplots()

    ax.plot(x_orig, y_orig, ls='solid', label='Original')
    ax.plot(x_anon, y_anon, ls='solid', label='Anonymized')
    ax.plot(x_synth, y_synth, ls='solid', label='Synthetic')
    ax.plot(x_combined, y_combined, ls='solid', label='Combined')

    ax.legend()

    plt.xlabel(xlabel)
    plt.ylabel(f'ECD({xlabel})')

    plt.savefig(save_to)

    return ax


def violin_plots(orig, anon, synth, combined, plot_parm, save_to='violin_plots.png'):
    plt.clf()
    ax = plt.gca()
    datalist = [orig, anon, synth, combined]
    ax.violinplot(datalist,
                  widths=0.85,
                  showmeans=False,
                  showmedians=False,
                  showextrema=False)
    ax.boxplot(datalist, widths=0.15, showcaps=False)
    ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([1, 2, 3, 4]))
    ax.set_ylabel(plot_parm)
    labels = ['Original', 'Anonymized', 'Synthetic', 'Combined']
    ax.set_xticklabels(labels)

    plt.savefig(save_to)

    return ax

