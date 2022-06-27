WEEKDAYS: dict = {
    "MO": 1,
    "TU": 2,
    "WE": 3,
    "TH": 4,
    "FR": 5,
    "SA": 6,
    "SU": 7,
}

PAY_RATE_WEEK: dict = {
    25: ("00:01", "09:00"),
    15: ("09:01", "18:00"),
    20: ("18:01", "23:59"),
}

PAY_RATE_WEEKEND: dict = {
    30: ("00:01", "09:00"),
    20: ("09:01", "18:00"),
    25: ("18:01", "23:59"),
}

PAYMENT: dict = {
    "week":{ 
        "hourly_payment": PAY_RATE_WEEK,
    },
    "weekend":{ 
        "hourly_payment": PAY_RATE_WEEKEND,
    },
}