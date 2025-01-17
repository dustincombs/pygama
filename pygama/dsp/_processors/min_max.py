import numpy as np
from numba import guvectorize
from pygama.dsp.errors import DSPFatal

@guvectorize(["void(float32[:], float32[:], float32[:], float32[:], float32[:])",
              "void(float64[:], float64[:], float64[:], float64[:], float64[:])"],
             "(n)->(),(),(),()", nopython=True, cache=True)
def min_max(w_in, t_min, t_max, a_min, a_max):
    """
    Find the value and index of the minimum and maximum values
    in the waveform.  Note that the first instance of each extremum
    in the waveform will be returned.

    Parameters
    ----------
    w_in : array-like
           The input waveform
    t_min: int
           The index of the minimum value
    t_max: int
           The index of the maximum value
    a_min: float
           The minimum value
    a_max: float
           The maximum value

    Processing Chain Example
    ------------------------
    "tp_min, tp_max, wf_min, wf_max": {
        "function": "min_max",
        "module": "pygama.dsp.processors",
        "args": ["waveform", "tp_min", "tp_max", "wf_min", "wf_max"],
        "unit": ["ns", "ns", "ADC", "ADC"],
        "prereqs": ["waveform"]
    }
    """
    a_min[0] = np.nan
    a_max[0] = np.nan
    t_min[0] = np.nan
    t_max[0] = np.nan

    if np.isnan(w_in).any():
        return

    min_index = 0
    max_index = 0

    for i in range(0, len(w_in), 1):
        if w_in[i] < w_in[min_index]:
            min_index = i
        if w_in[i] > w_in[max_index]:
            max_index = i

    a_min[0] = w_in[min_index]
    a_max[0] = w_in[max_index]
    t_min[0] = float(min_index)
    t_max[0] = float(max_index)
