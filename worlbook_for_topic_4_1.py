from datetime import datetime, timedelta


def check_arrival_time(current_time, lesson_start="08:30"):
    current_time = datetime.strptime(current_time, "%H:%M")
    lesson_start = datetime.strptime(lesson_start, "%H:%M")
    delta = lesson_start - current_time
    delta_in_minuts = int(delta.total_seconds() / 60)
    if 0 <= delta_in_minuts <= 15:
        return 'Ваш ребенок пришел в школу вовремя.'
    elif delta_in_minuts > 15:
        return 'Ваш ребенок пришел слишком рано!'
    elif delta_in_minuts < 0:
        return f'Ваш ребенок опоздал на {delta_in_minuts * -1} мин.'


print(check_arrival_time("08:15"))
print(check_arrival_time("06:30"))
print(check_arrival_time("08:45"))
