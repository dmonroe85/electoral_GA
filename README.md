# Electoral College Genetic Analysis

This project investigates what it takes to skew the electoral college and product least-fair outcomes regarding the popular vote.  It uses genetic minimization to try and find voter apportionment that wins an electoral college election using the smallest possible population.

## Setup

This was tested using Python3 and Virtualenv (install via your favorite package manager).

Then
* `virtualenv -p python3 v`
* `source v/bin/activate`
* `pip install -r requirements.txt`
* `python main.py`

## Results

*Using the population of registered voters*

33799562 / 153170043 ~= 22.07% of the population with 269 EC votes, 6.77 seconds
WINNERS:
['Alabama', 0.4999991131107159, 9, 2490000]
['Alaska', 0.4999998470382583, 3, 337000]
['Arizona', 0.4999996987174466, 11, 3262000]
['Arkansas', 0.4999993107108524, 6, 1262000]
['California', 0.4999993483239171, 55, 15690000]
['Colorado', 0.49999989971844516, 9, 2645000]
['Connecticut', 0.49999886768184365, 7, 1726000]
['D.C.', 0.49999870887202735, 3, 504043]
['Delaware', 0.49999973978778767, 3, 472000]
['Hawaii', 0.49999977717527394, 4, 523000]
['Idaho', 0.49999857995318947, 4, 743000]
['Indiana', 0.49999982368133333, 11, 3131000]
['Iowa', 0.4999998080231344, 6, 1658000]
['Kansas', 0.49999980129351995, 6, 1449000]
['Kentucky', 0.4999995389337973, 8, 2389000]
['Louisiana', 0.49999796443587596, 8, 2263000]
['Maine', 0.49999941963329786, 4, 828000]
['Mississippi', 0.49999893022689, 6, 1599000]
['Montana', 0.499999118747861, 3, 579000]
['Nebraska', 0.4999998744023219, 5, 883000]
['Nevada', 0.49999874806533395, 6, 1277000]
['New Hampshire', 0.49999933582526157, 4, 726000]
['New Mexico', 0.4999993627154032, 5, 916000]
['New York', 0.49999952466991066, 29, 8553000]
['North Dakota', 0.49999938522183696, 3, 397000]
['Oklahoma', 0.49999956655412947, 7, 1777000]
['Rhode Island', 0.49999965546146485, 4, 532000]
['South Carolina', 0.4999985006529137, 9, 2430000]
['South Dakota', 0.4999985749765484, 3, 429000]
['Tennessee', 0.49999998068108115, 11, 3183000]
['Utah', 0.49999997903136223, 6, 1443000]
['Vermont', 0.4999999004436239, 3, 343000]
['West Virginia', 0.49999966523544537, 5, 892000]
['Wyoming', 0.4999995700543969, 3, 268000]
LOSERS:
['Florida', 1.0, 29, 9435000]
['Georgia', 1.0, 16, 4840000]
['Illinois', 1.0, 20, 6068000]
['Maryland', 1.0, 10, 3095000]
['Massachusetts', 1.0, 11, 3345000]
['Michigan', 1.0, 16, 5453000]
['Minnesota', 1.0, 10, 3000000]
['Missouri', 1.0, 10, 3299000]
['New Jersey', 1.0, 14, 4297000]
['North Carolina', 1.0, 15, 5160000]
['Ohio', 1.0, 18, 6062000]
['Oregon', 1.0, 7, 2274000]
['Pennsylvania', 1.0, 20, 6469000]
['Texas', 1.0, 38, 11634000]
['Virginia', 1.0, 13, 4159000]
['Washington', 1.0, 12, 3852000]
['Wisconsin', 1.0, 10, 3129000]
