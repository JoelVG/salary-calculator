# Salary calculator
## Python >= 3.7.* required

## Solution
    Metodology: TDD.
    Explanaition: 
    The `main.py` file contains all the functions that I use for this solution.

    - `process_data(file_name:str="data.txt)`: Process the data from **data.txt** or the file that was passed in the format that
    the problem show. e.g. RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
    returns a generator formated as a dictionary and if we do: `list(process_data())[0]` we are going to get this dictionary:
    ```
    {
        "name": "RENE", 
        "days_worked": ["MO", "TU", "TH", "SA", "SU"],
        "hours_worked": ["10:00-12:00", "10:00-12:00", "01:00-03:00", "14:00-18:00", "20:00-21:00"]
    }
    ```
    that contains the "name" of the currend worker, "days_worked" that he or she worked and the "hours_worked"
    for the correspond days.

    - `get_total_payment(worker: dict) -> float`: Function that return the total payment for an
    specific worker.

    - `is_in_time_interval(time_interval: tuple[str], time: datetime) -> bool`: Function that returns a True
    if the **time** is in the interval of **time_interval** of False if not.

    - `get_rate(init_time: datetime, end_time: datetime, payment: dict)`: Function that returns the
    payment rate for an specific interval of time (init_time and end_time).
    In this method We have two diferent cases:
    - CASE 1: If the interval of time (init_time and end_time) is in only one of the interval
    that the problem give us. Return the payment rate for this interval of time.
    - CASE 2: If the interval of time (init_time and end_time) is more than one of the interval
    that the problem give us. The function calculates for the two period of times and returns a tuple
    that contains a flag and the total of the pay rate for each interval of time. e.g.
    data = LOREM=MO10:00-19:00,SA17:00-23:00
    For monday:
    - from 10:00 to 18:00: 8h x 15usd/h = 140USD
    - from 18:01 to 19:00: 1h x 20usd/h = 20USD
    For saturday:
    - from 17:00 to 18:00: 1h x 20usd/h = 20USD
    - from 18:01 to 23:00: 5h x 25usd/h = 125USD 

    TOTAL: 305USD


    The `constnts.py` file contains all the contants that I use for the solution of this problem.

    The `tests.py` file contains all the tests that I use to test all my functions and use the data
    from **fixtures.txt** file.

## Run
    To run the solution execute:
    `python main.py --data=path/data.txt`


    - If the path is not provided the script run by default with **data.txt** from the current directory.

## Test
    To run the tests execute:
    `python tests.py`

    - The script load the *fixtures.txt* that contains the different use cases for the problem.
