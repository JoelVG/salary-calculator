from unittest import TestCase, main
from datetime import datetime
from main import process_data, is_in_time_interval, get_payment, get_total_payment
from constants import PAYMENT


class UtilsTestCase(TestCase):

    def setUp(self) -> None:
        self.rene_data = {
            "name": "RENE", 
            "days_worked": ["MO", "TU", "TH", "SA", "SU"],
            "hours_worked": ["10:00-12:00", "10:00-12:00", "01:00-03:00", "14:00-18:00", "20:00-21:00"]
        }

    def test_process_data(self):
        data = list(process_data("fixtures.txt"))
        self.assertIn(self.rene_data, data)
        
    def test_time_interval(self):
        time_init = "07:30"
        time_mid = datetime.strptime("09:30", "%H:%M")
        time_end = "10:30"
        result = is_in_time_interval(time_interval=(time_init, time_end), time=time_mid)
        self.assertTrue(result)
        
    def test_get_payment_on_week(self):
        payment = PAYMENT["week"]
        time_init = datetime.strptime("09:30", "%H:%M")
        time_end = datetime.strptime("10:30", "%H:%M")
        hours = (time_end - time_init).total_seconds()/3600
        hourly_payment = get_payment(init_time=time_init, end_time=time_end, pay=payment, hours=hours)
        # 15 because is the hourly payment in the interval from 09:01 to 18:00 on weekdays
        self.assertEqual(hourly_payment, 15)
        
    def test_get_total_payment(self):
        payment = get_total_payment(self.rene_data)
        data = list(process_data("fixtures.txt"))
        workers_payment = [215.0, 85.0, 327.5, 160.0]
        for worker_data, pay in zip(data, workers_payment):
            payment = get_total_payment(worker_data)
            self.assertEqual(payment, pay)

if __name__ == "__main__":
    main()
