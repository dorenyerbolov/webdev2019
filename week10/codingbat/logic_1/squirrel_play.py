def squirrel_play(temp, is_summer):
    upper = 100 if is_summer else 90
    return 60 <= temp and temp <= upper
