def howManyMonths(start, rate, spending, target):
    
    
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

print(howManyMonths(15000, 0.03, 100, 20000))





# Project Title

One Paragraph of project description goes here.

## Getting Started

These instructions will [do something] on your local machine for [development/experimentation/demo].

### Prerequisites

[Project] requires [software and version] to run, with [additional packages, libaries, or mods]. The commands below will [upgrade OS and install the prerequisites, or do something else]

```
sudo apt update
sudo apt upgrade
sudo apt install package1 package2
```

## Running
Once installed you can run the program with the following command

```
python cna_demo.py
```

Add any additional ways to run the program below

```
python cna_demo.py test.txt

```

##Thanks
Provide thank yous and attributions here.  If someone helped you, you looked at anothers repostiory, or another article, provide it here.
