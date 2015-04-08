def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value * ( (1 + periods) **rate_per_period )
    return fv
    # Put your code here.

print "$1000 at 2% compounded daily for 3 years yields $", future_value(500, .04, 10, 10)