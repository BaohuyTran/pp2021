def inputNumberStd():
    n=int(input("Number of students?"))
    return n

def inputStdInfo(n):
    namel=[]
    idl=[]
    dobl=[]
    for i in range (0,n,1):
        print("Student's info ",i+1)
        name=input("Name")
        namel+=[name]
        id=input("Id")
        idl+=[id]
        dob=input("Date of bird")
        dobl+=[dob]
    return [namel,idl,dobl]