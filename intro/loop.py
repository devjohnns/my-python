
# for ,while , do_while

to_loop=True
i=0

while to_loop:
    if i>10:
        to_loop=False
    print("i is",i)
    i+=1

#for(let i=0;i<10;i++)

for i in range(0,10):
    print("for loop is", i)

for i in range(0, 1000, 2):
    print("for loop is", i)

protection=["Orange","Banana","Mango"]

for i in protection:
    print(i)