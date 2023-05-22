# A function for the time it will take your savings to reach a targeted amount

## Getting Started

These instructions will set up a function on your local machine for figuring how many month it would take to save a target savings amount.

### Prerequisites

This function requires Python 3 to run, with no additional software.  The commands below will set a Python program to do the math.

Python 3: https://www.python.org/downloads/

```

## Running


```
months = 0
balance = start

while True:
    months+=1

    balance = balance * (1 + rate) - spending

    if balance >= target:
        return months

    if balance < 0:
        return -1

    if months == 100:
        return -1
```


##Thanks
Provide thank yous and attributions here.  If someone helped you, you looked at anothers repostiory, or another article, provide it here.
