import matplotlib.pyplot as plt

#enter points (x,y)

X_e = []
Y_e = []

print("Enter Points count :\n>> ")
N = int(input())

for k in range(N):
    print("#", k ," cordonates : ")
    xi = float(input())
    yi = float(input())
    X_e.append(xi)
    Y_e.append(yi)


RANGE = 500
precison = 20
startCor = -10

def lagrenge(x, indice):
    tot = 1.0
    templist = [h for j, h in enumerate(X_e) if j != indice]
    for xe in templist:
        tot *= (x - xe)/(X_e[indice] - xe)
    return tot
#print(lagrenge(1.0, 0))
def P(x):
    i = 0
    tot = 0.0
    for y in Y_e :
        tot = tot + y * lagrenge(x, i)
        i += 1
    return tot

print(P(3))
Ylist = []
X = []

for i in range(RANGE):
    X.append((i / precison) + startCor)
    Ylist.append(P(X[i]))

plt.plot(X , Ylist , 'bo')
plt.show()



