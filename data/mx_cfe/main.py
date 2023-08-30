from datetime import date, datetime, time, timedelta
from calendar import monthcalendar

# Return A, B, C or D season depending on date condition   
def get_season(d: date) -> str:
    # Get april's first sunday
    april_first_sunday_day = min(monthcalendar(d.year, 4)[0][6], monthcalendar(d.year, 4)[1][6])
    april_first_sunday = date(year=d.year, month=4, day=april_first_sunday_day)
    # Get october's last sunday
    october_last_sunday_day = max(monthcalendar(d.year, 10)[-1][6], monthcalendar(d.year, 10)[-2][6])
    october_last_sunday = date(year=d.year, month=10, day=october_last_sunday_day)
    # If date between february 1st and april's first sunday, return A
    if d >= date(year=d.year, month=2, day=1) and d < april_first_sunday:
        return 'A'
    # If date between april's first sunday and july 31st, return B
    elif d >= april_first_sunday and d <= date(year=d.year, month=7, day=31):
        return 'B'
    # If date between august 1st and october's last sunday, return C
    elif d >= date(year=d.year, month=8, day=1) and d <= october_last_sunday:
        return 'C'
    # If date between october's last sunday and january 31st, return D
    else:
        return 'D'
    
# Return quota
def get_quota(dt: datetime) -> int:
    season = get_season(dt.date())
    # Season A
    if season == 'A':
        if dt.weekday() >= 0 and dt.weekday() <= 4:
            # If time between 00:00 - 06:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=6, minute=0): return 0
            # If time between 06:00 - 19:30 return 1
            elif dt.time() >= time(hour=6, minute=0) and dt.time() <= time(hour=19, minute=30): return 1
            # If time between 22:30 - 23:59 return 1
            elif dt.time() >= time(hour=22, minute=30) and dt.time() <= time(hour=23, minute=59): return 1
            # Any other time return 2
            else: return 2
        elif dt.weekday() == 5:
            # If time between 00:00 - 07:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=7, minute=0): return 0
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 6:
            # If time between 00:00 - 19:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=19, minute=0): return 0
            # If time between 23:00 - 23:59 return 0
            elif dt.time() >= time(hour=23, minute=0) and dt.time() <= time(hour=23, minute=59): return 0
            # Any other time return 1
            else: return 1
    # Season B
    elif season == 'B':
        if dt.weekday() >= 0 and dt.weekday() <= 4:
            # If time between 01:00 - 06:00 return 0
            if dt.time() >= time(hour=1, minute=0) and dt.time() <= time(hour=6, minute=0): return 0
            # If time between 20:30 - 22:30 return 2
            elif dt.time() >= time(hour=20, minute=30) and dt.time() <= time(hour=22, minute=30): return 2
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 5:
            # If time between 01:00 - 07:00 return 0
            if dt.time() >= time(hour=1, minute=0) and dt.time() <= time(hour=7, minute=0): return 0
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 6:
            # If time between 00:00 - 19:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=19, minute=0): return 0
            # Any other time return 1
            else: return 1
    # Season C
    elif season == 'C':
        if dt.weekday() >= 0 and dt.weekday() <= 4:
            # If time between 00:00 - 06:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=6, minute=0): return 0
            # If time between 19:30 - 22:30 return 2
            elif dt.time() >= time(hour=19, minute=30) and dt.time() <= time(hour=22, minute=30): return 2
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 5:
            # It time between 00:00 - 07:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=7, minute=0): return 0
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 6:
            # It time between 19:00 - 23:00 return 1
            if dt.time() >= time(hour=19, minute=0) and dt.time() <= time(hour=23, minute=0): return 1
            # Any other time return 0
            else: return 0
    # Season D
    elif season == 'D':
        if dt.weekday() >= 0 and dt.weekday() <= 4:
            # If time between 00:00 - 06:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=6, minute=0): return 0
            # If time between 18:30 - 22:30 return 2
            elif dt.time() >= time(hour=18, minute=30) and dt.time() <= time(hour=22, minute=30): return 2
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 5:
            # If time between 00:00 - 08:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=8, minute=0): return 0
            # If time between 19:30 and 21:30 return 2
            elif dt.time() >= time(hour=19, minute=30) and dt.time() <= time(hour=21, minute=30): return 2
            # Any other time return 1
            else: return 1
        elif dt.weekday() == 6:
            # If time between 00:00 - 18:00 return 0
            if dt.time() >= time(hour=0, minute=0) and dt.time() <= time(hour=18, minute=0): return 0
            # Any other time return 1
            else: return 1

def generate_data(start_datetime: datetime, end_datetime: datetime, datetime_delta: timedelta):
    dt = start_datetime
    while dt <= end_datetime:
        # Print iso format datetime and quota
        # print(dt.isoformat(), ',', get_quota(dt))
        print(f"{dt.isoformat()},{get_quota(dt)}")
        dt += datetime_delta

print("datetime,quota")
generate_data(
    datetime(year=2023, month=1, day=1, hour=0, minute=0), 
    datetime(year=2023, month=12, day=31, hour=23, minute=59), 
    timedelta(minutes=30))