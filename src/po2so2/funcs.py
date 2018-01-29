import numpy as np

def mmhg_to_kpa(mmhg):
    return mmhg * 0.133322387415

def kpa_to_mmhg(kpa):
    return kpa / 0.133322387415

def hill_po2_to_so2(po2_arg, kpa=True):
    if kpa:
        p50 = mmhg_to_kpa(26.8)
    else:
        p50 = 26.8
    nh = 2.7 # hill coefficient
    return np.power((po2_arg/p50), nh) / (1 + np.power((po2_arg/p50), nh))

def severinghaus_po2_to_so2(po2_arg, kpa=True):
    if kpa:
        po2 = kpa_to_mmhg(po2_arg)
    else:
        po2 = po2_arg
    return 1 / ((23400 / (np.power(po2, 3) + (150 * po2))) + 1)


def severinghaus_so2_to_po2(so2, kpa=True):
    # TODO fix error on so2 = 0
    # po2 returned in kPa
    return mmhg_to_kpa(np.exp((0.385 * np.log(np.reciprocal((1/so2)-1))) + 3.32 + (np.power(so2, 6)/-6) + (-1/(72 * so2))))

def thomas_po2_to_so2(po2_arg, kpa=True):

    # convert po2 from kPa to mmHg
    # because metric/SI
    # published function units are mmHg
    if kpa:
        po2 = kpa_to_mmhg(po2_arg)
    else:
        po2 = po2_arg

    a1 = -8.5322289 * 10**3
    a2 = 2.1214010 * 10**3
    a3 = -6.7073989 * 10**1
    a4 = 9.3596087 * 10**5
    a5 = -3.1346258 * 10**4
    a6 = 2.3961674 * 10**3
    a7 = -6.7104406 * 10**1

    numerator = (a1 * po2) + (a2 * np.power(po2, 2)) + (a3 * np.power(po2, 3)) + np.power(po2, 4)

    denominator = a4 + (a5 * po2) + (a6 * np.power(po2, 2)) + (a7 * np.power(po2, 3)) + np.power(po2, 4)

    so2 = numerator / denominator

    return so2
