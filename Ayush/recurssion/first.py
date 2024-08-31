#print("Hellow world")
#n = int(input(" Enter your number: "))
def show(a):
    if a == 0 :
        return
    else:
        print(a)
        return a*show(a - 1)
show(5)

