# start.py
from sjtuautorun.mygo import RunPlan
from sjtuautorun.scripts.main import start_script
from settime import *
from calculate_dates import *

dates = getdates()

for date in dates:
    set_simulator_time(0, date[0], date[1], date[2], 10, 30, 0)
    timer = start_script('settings.yaml')
    run_plan = RunPlan(timer)
    run_plan.start_run()