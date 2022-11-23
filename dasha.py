def function(x, y, z):
    for i in range(5):
        for j in range(5):
            if j % 2 == 0:
                if j == 1 or j == 3:
                    print(x)
                else:
                    print(z)
            else:
                if (j+1) % 3 != 0:
                    print(y)
                else:
                    print(x)

function(0, 1, 2)
