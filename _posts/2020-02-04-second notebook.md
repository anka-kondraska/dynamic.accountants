---
layout: post
title: Second Jupyter Notebook - Finishing Cleaning Data with pandas
tags: cleaning data, pandas, python
excerpt_separator: <!--more-->
---
Here is part two of cleaning financial data with `Python` `pandas` package.
<!--more-->

### <i class="fa fa-wind"></i> Let's `keep` cleaning it!

In this second part of cleaning the financial data [financial_sample.csv](/assets/files/financial_sample.csv){:target="_blank"}, I convert columns with numbers as text into decimals, as well as convert any NaNs into zeroes. In the first notebook, I focused on removing extra whitespace in column labels, Series data, as well as removing other characters such as `$` or `$-`. In our dataFrame, we want consistent uniform data that we can relay on in our analysis.

### <i class="fa fa-wind"></i> Load it up

Similarily as with the first notebook, please upload [python_pandas_cleaning_data2.ipynb](/assets/files/python_pandas_cleaning_data2.ipynb){:target="_blank"} and the csv file [financial_sample.csv](/assets/files/financial_sample.csv){:target="_blank"} to [Google's Colab](https://colab.research.google.com/notebooks/welcome.ipynb){:target="_blank"}.

Then proceed through the steps outlined in the notebook

View the code below, open it in Colab or download it from Gist.
<script src="https://gist.github.com/anka-kondraska/6df6f27f2a19a33d2b850ac2cd2e9102.js"></script>

### <i class="fa fa-wind"></i> Keyboard shortcuts are super helpful. 

To familirize yourself with keyboard shortcuts in jupyter notebook, please check out the `Help` menu. Also, all the most important package references are included as well.
![Jupyter help menu](/assets/img/jupyter_help_menu.png)