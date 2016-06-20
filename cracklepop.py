def cracklepop(start, end):
    for i in range(start, end+1):
        if (i % 15) == 0:
            print('CracklePop');
        elif (i % 3) == 0:
            print('Crackle');
        elif (i % 5) == 0:
            print('Pop');
        else:
            print(i);
    return;

cracklepop(1, 100);
