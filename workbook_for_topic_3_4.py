def vitya_hochet_viyti(
        degree: int, wind_speed: int, is_raining: bool,
        is_friend_calling: bool, is_girl_abuse: bool
        ) -> str:
    if is_girl_abuse:
        return 'Уже бегу'
    elif (is_friend_calling and degree >= -10 and wind_speed < 20
          and not is_raining
          ):
        return 'Зачилю с бро'
    elif degree >= 15 and wind_speed < 15 and not is_raining:
        return 'Погуляю один'
    else:
        return 'Полежу дома'


print(vitya_hochet_viyti(-50, 100, True, True, True))  # "Уже бегу"
print(vitya_hochet_viyti(0, 10, True, True, False))  # "Полежу дома"
print(vitya_hochet_viyti(-5, 15, False, True, False))  # "Зачилю с бро"
print(vitya_hochet_viyti(20, 10, False, False, False))  # "Погуляю один"
