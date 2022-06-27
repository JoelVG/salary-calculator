from datetime import datetime, timedelta
from constants import PAYMENT, WEEKDAYS
import argparse


def process_data(file_name: str="data.txt"):
    """
    Function that clean data from `data.text` and returns a generator
    formatted as a dictionary.
    """

    with open(file_name) as file:
        lines =  file.readlines()

    for line in lines:
        data_cleaned = {}
        splited_line = line.split("=")
        # Getting the name of employee
        data_cleaned["name"] = splited_line[0]
        splited_date = splited_line[1].split(",")
        # Getting days worked
        data_cleaned["days_worked"] = [day[:2] for day in splited_date]
        # Getting hours worked
        data_cleaned["hours_worked"] = [hour[2:].strip() for hour in splited_date]
        yield data_cleaned


def get_total_payment(worker: dict) -> float:
    """Function that calculates the total amount of payment of a worker."""

    total = 0
    for hours, day in zip(worker["hours_worked"], worker["days_worked"]):
        hour_interval = hours.split("-")
        init_time = datetime.strptime(hour_interval[0], "%H:%M")
        end_time = datetime.strptime(hour_interval[1], "%H:%M")
        hours = (end_time - init_time).total_seconds()/3600 #3600s in 1h
        payment = PAYMENT["weekend"] if WEEKDAYS[day] > 5 else PAYMENT["week"]
        rate = get_payment(init_time, end_time, payment, hours)
        total += rate
                
    return total


def is_in_time_interval(time_interval: tuple[str], time: datetime) -> bool:
    """Function that checks if `time` is in a specific time interval."""
    
    init_time = datetime.strptime(time_interval[0], "%H:%M")
    end_time = datetime.strptime(time_interval[1], "%H:%M")
    return init_time <= time <= end_time


def get_payment(init_time: datetime, end_time: datetime, pay: dict, hours: float) -> float:
    "Function that gets the payment in the range of init_time and end_time."

    one_minute = timedelta(minutes=1)
    hourly_payment = pay["hourly_payment"]
    for payment, interval in hourly_payment.items():
        if is_in_time_interval(interval, init_time) and is_in_time_interval(interval, end_time):
            return payment * hours
        else:
            end_datetime = datetime.strptime(interval[1], "%H:%M")
            if end_datetime > init_time:
                time_one = (end_datetime - init_time).total_seconds()/3600
                payment_one = payment * time_one
                time_two = (end_time - end_datetime + one_minute).total_seconds()/3600
                payment_two = get_payment(end_datetime + one_minute, end_time, pay, int(time_two))
                return payment_one + payment_two


def main(path: str) -> None:
    data = list(process_data(path))
    for worker_data in data:
        payment = round(get_total_payment(worker_data), 2)
        print(f"The amount to pay {worker_data['name']} is: {payment} USD")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.set_defaults(method=main)
    parser.add_argument("-d", "--data", 
                        help="Path for the file with the workers data", 
                        type=str,
                        default="data.txt"
                        )
    path = parser.parse_args()
    main(path.data)
