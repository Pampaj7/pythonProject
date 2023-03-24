def cassiere_alg(r, c):  # c sarà una lista
    print('Devo fornire', r, 'euro di resto')
    print('Ho a disposiione monete di taglio: ', str(c))
    c.sort()
    s = []
    while r > 0:
        x = c[-1]  # opposto del vettore ovvero taglia massima
        del c[-1]  # facendo così elimino ad ogni ciclo, non devo!
        if r >= x:
            r = r - x
            s.append(x)
        if r == 0:
            print("la soluzione è: " + str(s))
        if c == []:  # se le taglie fossere precise stamperebbe questo
            print("Non è possibile trovare la soluzione")
            break


cassiere_alg(73, [100, 50, 20, 10, 5, 2, 1])
