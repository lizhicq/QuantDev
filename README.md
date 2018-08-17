# Building Quantitative Strategy for Personal Trading
==================
Simplified Quantopian System, locally download data, building strategy, bask testing, paper trading


### Install
This project requires **Python 2.7** and the following Python libraries installed:

- [Bintrees](https://pypi.python.org/pypi/bintrees/2.0.2)
- [Matplotlib](http://matplotlib.org/)
- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [Seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/)
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)


### Run
In a terminal or command window, navigate to the top-level project directory `rl_trading/` (that contains this README) and run the following command:

```shell
$ python -m market_sim.agent [-h] [-t] [-d] [-s] [-m] <OPTION>
```

Where *OPTION* is the kind of agent to be run. The flag *[-t]* is the number of trials to perform using the same file, *[-d]* is the date of the file to use in the simulation, *[-m]* is the month of the *date* flag and *[-s]* is the number of sessions on each trial. Use the flag *[-h]* to get information about what kind of agent is currently available, as well as other flags to use. The simulation will generate log files to be analyzed later on. Be aware that any of those simulations options might take several minutes to complete.


### Data
Data is extraded from yahoo finance, refer to QuantDB to checkout the datasource and local DB construction.


### Main References
1. Gareth James • Daniela Witten • Trevor Hastie • Robert Tibshirani, An Introduction to
Statistical Learning, 4th Edition.
2. CHAN, N. T.; SHELTON, C. *An electronic market-maker*. 2001.

### License
The contents of this repository are covered under the [Apache 2.0 License](LICENSE.md).