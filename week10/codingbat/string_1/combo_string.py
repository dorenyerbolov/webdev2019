def combo_string(a, b):
    short = a
    long = b

    if len(a) > len(b):
        short = b
        long = a

    return short + long + short
