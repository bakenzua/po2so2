# Po2So2

A python package providing several seminal functions to convert between oxygen saturations and oxygen partial pressures of blood. Severinghaus<sup>[1](#reference1)</sup> and Thomas<sup>[2](#reference2)</sup> published fitted curves to experimental data in the 1970s,

## Getting Started

This is a native python package developed with python 3.6.1. It is untested against python 2. The package is not currently available via pip or other package indexes. Requires local installation.

Once installed use functions to perform conversions. Functions work against scalar values and numpy arrays.

Oxygen saturations, SO<sub>2</sub>, are defined as fractions ie between 0 and 1.

Oxygen partial pressure PO<sub>2</sub> are defined in kPa

```
$ python
Python 3.6.1
>>> import po2so2
>>> import numpy as np
>>>
>>> po2so2.so2_to_po2(0.85)
6.6434949050372891
>>> po2so2.po2_to_so2(7.5)
0.89289441193803076
>>>
>>> so2s = numpy.linspace(0.01, 0.95, 20)
>>> po2so2.so2_to_po2(so2s)
array([ 0.15676692,  1.00857273,  1.44547746,  1.77603347,  2.06100573,
        2.3233735 ,  2.57504209,  2.8235901 ,  3.0746935 ,  3.33323752,
        3.60397356,  3.89205938,  4.20369728,  4.54712619,  4.93444258,
        5.38535245,  5.93585653,  6.66171949,  7.75932443,  9.98904198])
>>>
```

### Prerequisites

Python 3 and numpy need to be installed.

```
pip install numpy
```

### Installing

First clone the repository, and enter the repository directory

```
git clone https://github.com/bakenzua/po2so2.git
cd severinghaus_o2
```

then either run the makefile

```
make dev_install
```
or install a development version via pip
```
pip install -e .
```


## References

<a name="reference1">1</a>: Severinghaus JW (1979). Simple, accurate equations for human blood O2 dissoci- ation computations. Journal of Applied Physiology; 46: 599–602. [PMID:35496](https://www.ncbi.nlm.nih.gov/pubmed/35496)

<a name="reference2">2</a>:Thomas LJ (1972). Algorithms for selected blood acid-base and blood gas calculations. Journal of Applied Physiology; 33: 154–158.
https://www.ncbi.nlm.nih.gov/pubmed/5037404

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
