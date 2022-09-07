# AICup22-Analytics

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Example](#example)

## About <a name = "about"></a>

This is a simple python script that aims to manage a mass iteration of AICup2022 server, 
and to analyze the result and dump it into a `result.log` file at the current working directory.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

Only what is required by the server itself is needed to run this script

### Installing

Just clone the repo, and then copy `analyzor.py` to where your kernel directory is, and then simply run it

## Usage <a name = "usage"></a>

This project simply runs receives the path of the server and clients, and then runs it for specific amount of time. for example you say run it 1000 times, and it does it. how convenient
It aslo renames the log files starting from 0 to the number you specified.
after the process is over, you can easily grab the important data about your iteration from `result.log`.
spoiler alert: it contains the reason why a team has won

## Example <a name = "example"></a>

If run the script blindedly you'll see the Python interpreter panics like this:
```
└─$ python3 analyzor.py 
Panic!:  Invalid number of arguments 
arg 1 : server path
arg 2 : server iteration count
arg 3 : first client path (optional)
arg 4 : second client path (optional) 
```

So you'll need to at least tell the script where the server is and how many times you want to run it:
```
└─$ python3 analyzor.py ./src/server.py 10
Am I allowed to delete the log folder at "./logs" ['y', 'n'] : y
server run count : 0 ,         ('Team 2', 'Random')        run_time:0.18
server run count : 1 ,  ('Team 2', 'More coins in wallet') run_time:0.18
server run count : 2 ,  ('Team 2', 'More coins in wallet') run_time:0.18
server run count : 3 ,  ('Team 1', 'More coins in wallet') run_time:0.18
server run count : 4 ,  ('Team 2', 'More coins in wallet') run_time:0.18
server run count : 5 ,  ('Team 2', 'More coins in wallet') run_time:0.18
server run count : 6 ,         ('Team 1', 'Random')        run_time:0.18
server run count : 7 ,  ('Team 2', 'More coins in wallet') run_time:0.18
server run count : 8 ,         ('Team 1', 'Random')        run_time:0.18
server run count : 9 ,  ('Team 1', 'More coins in wallet') run_time:0.18

Server run iteration is over, check the log file at : "./result.log"
```

And there's a breif report of the whole process in the `result.log` that might be of your interests:
```
.
.
.

total games count : 10
Team 2 win count : 6
Team 1 win count : 4
 total run time : 1.796    
```

That's pretty much it, make sure to use it wisely :)




