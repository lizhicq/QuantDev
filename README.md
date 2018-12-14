Building Quantitative Strategy for Personal Trading
==================
  
Simplified Quantopian System, locally download data, building strategy, bask testing, paper trading


### Data Source

Data is imported from yahoo finance, I wrapped sp500 stocks from 2000-01-01 to 2018-08-08. You're free to add more stocks using the template. I personally add TSLA, YHOO, BABA.

I used mysql to manage the stocks daily data and provide table to create/insert/update query for reference.
It is easy to migrate the data with mysql. 

Later, when I introduce the text analysis model, I may use mongo db to manager the text data I wrapped from the web.



### Example,
Here is an example, I use sklearn template to make this sample. Using the close price - open price as input, find their kernals and try to cluster those stocks with similiar change pattern.  

![alt text](https://lh3.googleusercontent.com/-6E-nUmRvrBI/W331bA8byHI/AAAAAAAA_dM/2JORMapWoyg76qIOqTJ3Ed9lW8wiJKoKwCL0BGAs/w530-d-h405-n-rw/download.png)

 
 
### Install
This project requires **Python 2.7** and the following Python libraries installed:

- [Bintrees](https://pypi.python.org/pypi/bintrees/2.0.2)
- [Matplotlib](http://matplotlib.org/)
- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [Seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/)
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)
- [scikit-learn](https://pypi.org/project/scikit-learn/) 
 


 
### Main References
1. Gareth James • Daniela Witten • Trevor Hastie • Robert Tibshirani, An Introduction to
Statistical Learning, 4th Edition.
2. CHAN, N. T.; SHELTON, C. *An electronic market-maker*. 2001.

### License
The contents of this repository are covered under the [Apache 2.0 License](LICENSE.md).   
