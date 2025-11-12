def is_enought_machines(free_machines_number, target_weight, max_payload=3):
    if free_machines_number * max_payload >= target_weight:
        return True
    else:
        return False


print(is_enought_machines(3, 9, 11))

print(is_enought_machines(1, 9, 3))
