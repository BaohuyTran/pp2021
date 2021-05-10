def inputNumberCour():
    n=int(input("Number of courses?"))
    return n

def inputCourInfo(n):
    idl=[]
    courl=[]
    for i in range (0,n,1):
        print("Course's info ",i+1," and course id should be interger starting from 0,1,..")
        id=input("Id")
        idl+=[id]
        cour=input("Name of cours")
        courl+=[cour]
    return [idl,courl]