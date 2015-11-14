[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```python
In [86]: summaries(sample)
Mean:  74278.7075312
Median:  51226.9330656
Skewness:  4.94992024443
Pearson Median Skewness:  0.736125801914
% Below Mean: 66.0%
Out[86]: (74278.707531187203, 51226.933065623722)

In [87]: summaries(sample7)
Mean:  124267.397222
Median:  51226.9330656
Skewness:  11.6036902675
Pearson Median Skewness:  0.391564509277
% Below Mean: 85.7%
Out[87]: (124267.39722164697, 51226.933065623722)
```
>> There does seem to ba a right skew that is visible when taking into account the different metrics that have been defined.
>>> The mean is greater than the median
>>> The moment skewness and Pearson Median Skewness measure are both positive (indicating right skew)
>> When the upper bound is changed, the skewness measure changes drastically while the pearson median skewness actually decreases. The mean changes drastically as well; therefore the mean and the skewness metrics are seemingly quite sensitive to the assumed upper bound. 
