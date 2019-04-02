def sleep_in(weekday, vacation):
    if (not weekday and not vacation) or (not weekday and vacation) or (weekday and vacation):
        return True
    if weekday and not vacation:
        return False
