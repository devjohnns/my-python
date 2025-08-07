

# your functon only takes 3 parameters 

def greet(*args):

    for arg in args:
        print("Name is",arg)

greet("John","Jane","Jack","Jill")
#greet(456,True,False,None,[1,2,3])

def sum(*args):
    ans=0
    for n in args:
       # print(f"{ans}={ans}+{n}")
        print(ans,"=",ans,"+",n)
        ans=ans+n

        print("Ans is ",ans)
    return ans
sum(100,200,300,400,500,600)