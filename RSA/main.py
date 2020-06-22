from mpmath import *
import math

def Prime(n):
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True

mp.prec=800
mp.dps=500

N=mp.mpf(179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581)

A=int(ceil(mp.sqrt(N))) #arithmetic mean of p and q
x=mp.sqrt(power(A, 2)-N)
print(x)
print(A-x) #ans for part 1


N=mp.mpf(648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877)

for A in range(int(ceil(mp.sqrt(N))), int(N)):
	print(A)
	x=mp.sqrt(power(A, 2)-N)
	if (x-int(x)) == 0:
		p=A-x
		q=A+x

		if int(p*q) == int(N):
			print("Found prime: ",p) #ans for part 2
			break




