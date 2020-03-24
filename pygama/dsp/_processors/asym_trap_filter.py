import numpy as np
from numba import guvectorize
import matplotlib.pyplot as plt

@guvectorize(["void(float32[:], int32, int32, int32, float32[:])",
              "void(float64[:], int32, int32, int32, float64[:])",
              "void(int32[:], int32, int32, int32, int32[:])",
              "void(int64[:], int32, int32, int32, int64[:])"],
             "(n),(),(),()->(n)", forceobj=True, cache=True)
def asymTrapFilter(wf_in, rise, flat, fall, wf_out): #,padAfter=False
    """ Computes an asymmetric trapezoidal filter"""

    # wf_out.fill(0)
    # wf_out = np.zeros_like(wf_in)
    kernel = np.zeros(2500)
    kernel[:1000] = 1. / 1000
    kernel[1500:] = 1. / 1000

    wf_out = np.convolve(wf_in, kernel, 'same')


    # wf_out[:] = wf_in[:]
    # wf_out[rise:] -= wf_in[:-fall]
    # wf_out[:] *= float(fall)/rise
    # wf_out[rise+flat:] -= wf_in[:-(fall+flat)]
    # wf_out[rise+flat+fall:] += wf_in[:-(rise+flat+fall)]
    # wf_out[:] /= fall
    # np.cumsum(wf_out, out=wf_out, axis=0)

    # x = np.arange(0,3000)
    # plt.scatter(x, wf_in)
    # plt.scatter(x, wf_out)
    # plt.show()
    # exit()



    # npad = int((rise+fall+flat)/2)
    # wf_out = np.pad(wf_out, (npad, 0), mode='constant')[:-npad]


    # kernel = np.zeros(rt + ft + flt)
    # kernel[:rt] = 1 / rt
    # kernel[rt + ft:] = -1 / flt
    # atrap = np.zeros_like(wfs)  # faster than a list comprehension
    # for i, wf in enumerate(wfs):
    #     atrap[i, :] = np.convolve(wf, kernel, 'same')
    # npad = int((rt+ft+flt)/2)
    # atrap = np.pad(atrap, ((0, 0), (npad, 0)), mode='constant')[:, :-npad]
    # atrap[:, -(npad):] = 0


    # wf_out[:] = wf_in[:]
    # wf_out[rise:] -= wf_in[:-fall]
    # wf_out[rise+flat:] -= wf_in[:-(fall+flat)]
    # wf_out[rise+flat+fall:] += wf_in[:-(rise+flat+fall)]
    # np.cumsum(wf_out, out=wf_out, axis=0)

    # wf_out.fill(0)
    # for i in range(len(wf_in)-1000):
    #     w1 = rise
    #     w2 = rise+flat
    #     w3 = rise+flat+fall
    #     r1 = np.sum(wf_in[i:w1+i])/(rise)
    #     r2 = np.sum(wf_in[w2+i:w3+i])/(fall)
    #     # if not padAfter:
    #     #     wf_out[i+1000] = r2 - r1
    #     # else:
    #     wf_out[i] = r2 - r1

    #Plot every line
