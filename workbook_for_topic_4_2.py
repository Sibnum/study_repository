from datetime import datetime, timedelta


def get_arrival_time(departure_time, hour, minute):
    if hour < 0 or hour >= 24:
        return 'Ошибка в данных'
    if minute < 0 or minute >= 60:
        return 'Ошибка в данных'
    departure_time = datetime.strptime(departure_time, "%H:%M %d:%m:%Y")
    delta = timedelta(hours=hour, minutes=minute)
    result = departure_time + delta
    arrival_time = result.strftime("%H:%M %d:%m:%Y")
    return f'{arrival_time}'


print(get_arrival_time("10:30 15:12:2023", 2, 45))
print(get_arrival_time("23:45 31:12:2023", 3, 30))
print(get_arrival_time("10:30 15:12:2023", -1, 45))
print(get_arrival_time("10:30 15:12:2023", 2, 60))
