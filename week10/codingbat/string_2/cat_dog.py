def cat_dog(str):
    cat_k = dog_k = 0

    for x in range(len(str) - 2):
        if str[x:x + 3] == "cat":
            cat_k += 1
        elif str[x:x + 3] == "dog":
            dog_k += 1

    return cat_k == dog_k