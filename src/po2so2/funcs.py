import numpy as np

def so2_to_po2(so2):

    # 0.133322 is the conversion to kPa from torr/mmHg
    return 0.133322387415 * np.exp((0.385 * np.log(np.reciprocal((1/so2)-1))) + 3.32 + (np.power(so2, 6)/-6) + (-1/(72 * so2)))

def po2_to_so2(po2):

    # convert po2 from kPa to mmHg
    # because metric/SI
    # published function works in mmHg
    po2 = po2 / 0.133322387415

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
