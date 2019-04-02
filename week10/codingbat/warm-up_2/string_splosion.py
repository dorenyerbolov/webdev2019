def string_splosion(str):
    res = ""

    for x in range(len(str)):
        res += str[:x + 1]

    return res
