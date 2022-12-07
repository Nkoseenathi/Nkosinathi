def population(n):

    if n<=2:
        return 2
    else:
        return population(n-1)+population(n-2)


    