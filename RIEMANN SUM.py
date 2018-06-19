#This is a program that calculates the left, right and middle reimann sums
#of a polynomial function over intervals as indicated by the user
from tkinter import *
from math import *
from turtle import *

def Rearrange(funct):    #this function partially rearranges a given function in such a way
                         #that it can be evaluated by python
    function=funct
    functT=""    #this is to hold the previous value of i in the previous iteration
    functF=""    #this is to become the "rearranged" function
    for i in function:
        if i=="x" and function.index(i)==0: #if the first character in the function is an "x",
            functF=functF+"("+i+")"         #put a bracket around it. This is so that python
                                            #will not exponentiate a negative x before applying
                                            #the negative sign and add this to functF
            
        elif i=="x" and functT!="+" and functT!="-": #If "x" has a coefficient ie it does not                                       
            functF=functF+"*("+i+")"                 #appear after a plus or minus, then put
                                                #brackets around the "x" and a multiplication
                                                #sign between the coefficient and the "x" with
                                                #brackets and add them to functF
        else:
            functF=functF+i                     #else, add i to functF               
        functT=i                              #set the value of functT to i for next iteration
    functioN="("+functF
    functionF=""
    for i in functioN:           #This loop puts each term of the polynomial in a bracket
        
        if i=="+" or i=="-":
            functionF=functionF+")"+i+"("
        else:
            functionF=functionF+i
        
            
    functionF=functionF+")"    
            
    return functionF



def calcFunctionalValue(funct,value):    #This calculates the functional value of a function,
                                         #"funct" at x=value
    function=Rearrange(funct)            #uses rearrange function to rearrange function
    replaced=function.replace("x",str(value))#replaces x's in the function with actual "value"
    replaced2=replaced.replace("^","**")
    answer=eval(replaced2)               #evaluates function to get an "answer"
    return answer



def drawGraph(function): #This function draws graphs for a given polynomial function called
                         #"function
    y1=Turtle()          #beginning creating turtles for drawing axes and setting their speed
    y1.speed(0)
    y2=Turtle()
    y2.speed(0)
    x1=Turtle()
    x1.speed(0)
    x2=Turtle()
    x2.speed(0)     #ending creating turtles for drawing axes and setting their speed

    y1.left(90)    #beginning drawing of axes
    y1.forward(30)
    for i in range(10):
        y1.left(90)
        y1.forward(3)
        y1.backward(6)
        y1.forward(3)
        y1.right(90)
        y1.forward(30)

    y2.right(90)
    y2.forward(30)
    for i in range(10):
        y2.left(90)
        y2.forward(3)
        y2.backward(6)
        y2.forward(3)
        y2.right(90)
        y2.forward(30)

    x2.right(180)
    x2.forward(30)
    for i in range(10):
        x2.left(90)
        x2.forward(3)
        x2.backward(6)
        x2.forward(3)
        x2.right(90)
        x2.forward(30)

    x1.forward(30)
    for i in range(10):
        x1.left(90)
        x1.forward(3)
        x1.backward(6)
        x1.forward(3)
        x1.right(90)
        x1.forward(30)   #ending drawing of axes

    global wT        
    wT=Turtle()        #creating turtle for labelling axes and drawing rest of graph 
    wT.speed(0)
    wT.hideturtle()
    x=-10
    wT.up()
    wT.setpos(-330,-17)
    wT.write("-y")     #beginning labelling of axes
    wT.forward(30)
    for i in range(21):
        wT.down()
        wT.write(str(x))
        wT.up()
        wT.forward(30)
        x=x+1

    wT.down()
    wT.write("+y")
    wT.up()
    y=-10

    wT.setpos(-15,-330)
    wT.left(90)
    wT.write("-y")
    wT.forward(30)
    for i in range(21):
        wT.down()
        wT.write(str(y))
        wT.up()
        wT.forward(30)
        y=y+1
    wT.write("+y")      #ending labelling of axes

    initialX=-10
    scaledX=initialX*30
    initialY=calcFunctionalValue(function,initialX)
    scaledY=initialY*30
    wT.setpos(scaledX,scaledY)
    wT.down()
    initialX=initialX+1
    while initialX<10.05:  #this loop draws the graph of of the function using the
                           #calcFunctionalValue function from x=-10 to x=10
        scaledX=initialX*30
        initialY=calcFunctionalValue(function,initialX)
        scaledY=initialY*30
        wT.goto(scaledX,scaledY)
        initialX=initialX+0.05
        
    
def drawLRS(funcT,low,up,num):    #this function uses the drawGraph function to draw the graph
                                  #of "funcT". Then it uses the calcFunctionalValue function
                                  #in drawing rectangles for the left Riemann Sum
    drawGraph(funcT)
    a=low
    b=up
    n=num
    dx=(b-a)/n
    wT.up()
    wT.goto(a*30,0)
    wT.down()
    while a<b:
        initX=a*30
        Y=calcFunctionalValue(funcT,a)
        initY=Y*30
        wT.goto(initX,initY)
        wT.goto(initX+(dx*30),initY)
        wT.goto(initX+(dx*30),0)
        a=a+dx



def drawMRS(funcT,low,up,num):   #This function draws the graph of "funcT"  and draws
                                 #rectangles for the middle riemann sum
    drawGraph(funcT)
    a=low
    b=up
    n=num
    dx=(b-a)/n
    wT.up()
    wT.goto(a*30,0)
    wT.down()
    while a<b:
        initX=a*30
        Y=calcFunctionalValue(funcT,a+(dx/2))
        initY=Y*30
        wT.goto(initX,initY)
        wT.goto(initX+(dx*30),initY)
        wT.goto(initX+(dx*30),0)
        a=a+dx




def drawRRS(funcT,low,up,num):  #Draws graph of "funcT" from x=-10 to x=10 and draws rectangles
                                #for right riemann sums
    drawGraph(funcT)
    a=low
    b=up
    n=num
    dx=(b-a)/n
    wT.up()
    wT.goto(a*30,0)
    wT.down()
    while a<=b:
        initX=a*30
        Y=calcFunctionalValue(funcT,a+dx)
        initY=Y*30
        wT.goto(initX,initY)
        wT.goto(initX+(dx*30),initY)
        wT.goto(initX+(dx*30),0)
        a=a+dx



    


    
def lrSum(Funct,lowerLimit,upperLimit,numOfRect):#This function calculates the left riemann
                                                #sum given a function, a lower and upper
                                                #limit and a number of rectangles
        a=float(lowerLimit)
        b=float(upperLimit)
        n=int(numOfRect)
        dx=(b-a)/n
        functSum=0
        functVal=a
        for i in range(n):
            functSum=functSum+calcFunctionalValue(Funct,functVal)
            functVal=functVal+dx
        RiemannSum=functSum*dx
        return RiemannSum
            

def rrSum(Funct,lowerLimit,upperLimit,numOfRect):#This function calculates the right riemann
                                                 #sum given the same input as for "lrSum"
        a=float(lowerLimit)
        b=float(upperLimit)
        n=int(numOfRect)
        dx=(b-a)/n
        functSum=0
        functVal=a+dx
        for i in range(n):
            functSum=functSum+calcFunctionalValue(Funct,functVal)
            functVal=functVal+dx
        RiemannSum=functSum*dx
        return RiemannSum


def mrSum(Funct,lowerLimit,upperLimit,numOfRect): #This function calculates the middle riemann
                                                  #given the same input as "lrSum"
        a=float(lowerLimit)
        b=float(upperLimit)
        n=int(numOfRect)
        dx=(b-a)/n
        functSum=0
        functVal=a+(dx/2)
        for i in range(n):
            functSum=functSum+calcFunctionalValue(Funct,functVal)
            functVal=functVal+dx
        RiemannSum=functSum*dx
        return RiemannSum

    

#Middle Riemann Sum
def createmrSWindow():  #This function creates a GUI program that allows the user to enter
                        #a function, a lower and upper limit and a number of rectangles
                        #and uses these inputs along with the "drawMRS" and "mrSum" functions
                        #to calculate and display the middle riemann sum along with a
                        #graphical representation of the function and rectangles for the middle
                        #riemann sum
    mainWindow.destroy()
    mrsWindow=Tk()
    mrsWindow.resizable(width=False,height=False)
    topicLabel=Label(mrsWindow,text="Right Riemann Sum", font = ("Papyrus",30,"bold"))
    topicLabel.grid(columnspan=2, sticky = "NE"+"SW")
    functLabel=Label(mrsWindow,text="f(x)=", font = ("Papyrus",20))
    functLabel.grid(row=1,column=0, sticky = "NE"+"SW")
    functEntry=Entry(mrsWindow)
    functEntry.grid(row=1,column=1, sticky = "NE"+"SW")
    uLLabel=Label(mrsWindow,text="Upper Limit=", font = ("Papyrus",20))
    uLLabel.grid(row=2,column=0, sticky = "NE"+"SW")
    uLEntry=Entry(mrsWindow)
    uLEntry.grid(row=2,column=1, sticky = "NE"+"SW")
    lLLabel=Label(mrsWindow,text="Lower Limit=", font = ("Papyrus",20))
    lLLabel.grid(row=3,column=0, sticky = "NE"+"SW")
    lLEntry=Entry(mrsWindow)
    lLEntry.grid(row=3,column=1, sticky = "NE"+"SW")
    intLabel=Label(mrsWindow,text="Number of rectangles=", font = ("Papyrus",20))
    intLabel.grid(row=4,column=0, sticky = "NE"+"SW")
    intEntry=Entry(mrsWindow)
    intEntry.grid(row=4,column=1, sticky = "NE"+"SW")
    answer=StringVar()
    ansLabel1=Label(mrsWindow,text="Answer", font = ("Papyrus",20))
    ansLabel1.grid(row=5,column=0, sticky = "NE"+"SW")
    ansLabel2=Label(mrsWindow,textvariable=answer)
    ansLabel2.grid(row=5,column=1, sticky = "NE"+"SW")
    def calcmrSum():
        f=functEntry.get()
        g=lLEntry.get()
        h=uLEntry.get()
        i=intEntry.get()
        asum=mrSum(f,g,h,i)
        answer.set(asum)
        drawMRS(f,float(g),float(h),int(i))
    submitBut=Button(mrsWindow,text="Submit",command=calcmrSum, font = ("Papyrus",20))
    submitBut.grid(row=6,column=1, sticky = "NE"+"SW")
    def back():
        mrsWindow.destroy()
        rMain()
    cancelButton=Button(mrsWindow,text="Back",command=back, font = ("Papyrus",20))
    cancelButton.grid(row=6,column=0, sticky = "NE"+"SW")
    mainloop()



#Right riemann sum

def createrrSWindow():  #This function creates a GUI program that allows the user to enter
                        #a function, a lower and upper limit and a number of rectangles
                        #and uses these inputs along with the "drawRRS" and "rrSum" functions
                        #to calculate and display the right riemann sum along with a
                        #graphical representation of the function and rectangles for the right
                        #riemann sum 
    mainWindow.destroy()
    rrsWindow=Tk()
    rrsWindow.resizable(width=False,height=False)
    topicLabel=Label(rrsWindow,text="Right Riemann Sum", font = ("Papyrus",30,"bold"))
    topicLabel.grid(columnspan=2, sticky = "NE"+"SW")
    functLabel=Label(rrsWindow,text="f(x)=", font = ("Papyrus",20))
    functLabel.grid(row=1,column=0, sticky = "NE"+"SW")
    functEntry=Entry(rrsWindow)
    functEntry.grid(row=1,column=1, sticky = "NE"+"SW")
    uLLabel=Label(rrsWindow,text="Upper Limit=", font = ("Papyrus",20))
    uLLabel.grid(row=2,column=0, sticky = "NE"+"SW")
    uLEntry=Entry(rrsWindow)
    uLEntry.grid(row=2,column=1, sticky = "NE"+"SW")
    lLLabel=Label(rrsWindow,text="Lower Limit=", font = ("Papyrus",20))
    lLLabel.grid(row=3,column=0, sticky = "NE"+"SW")
    lLEntry=Entry(rrsWindow)
    lLEntry.grid(row=3,column=1, sticky = "NE"+"SW")
    intLabel=Label(rrsWindow,text="Number of rectangles=", font = ("Papyrus",20))
    intLabel.grid(row=4,column=0, sticky = "NE"+"SW")
    intEntry=Entry(rrsWindow)
    intEntry.grid(row=4,column=1, sticky = "NE"+"SW")
    answer=StringVar()
    ansLabel1=Label(rrsWindow,text="Answer", font = ("Papyrus",20))
    ansLabel1.grid(row=5,column=0, sticky = "NE"+"SW")
    ansLabel2=Label(rrsWindow,textvariable=answer)
    ansLabel2.grid(row=5,column=1, sticky = "NE"+"SW")
    def calcrrSum():
        f=functEntry.get()
        g=lLEntry.get()
        h=uLEntry.get()
        i=intEntry.get()
        asum=rrSum(f,g,h,i)
        answer.set(asum)
        drawRRS(f,float(g),float(h),int(i))
    submitBut=Button(rrsWindow,text="Submit",command=calcrrSum, font = ("Papyrus",20))
    submitBut.grid(row=6,column=1, sticky = "NE"+"SW")
    def back():
        rrsWindow.destroy()
        rMain()
    cancelButton=Button(rrsWindow,text="back",command=back, font = ("Papyrus",20))
    cancelButton.grid(row=6,column=0, sticky = "NE"+"SW")
    mainloop()



def createLRSWindow():   #This function creates a GUI program that allows the user to enter
                        #a function, a lower and upper limit and a number of rectangles
                        #and uses these inputs along with the "drawLRS" and "lrSum" functions
                        #to calculate and display the left riemann sum along with a
                        #graphical representation of the function and rectangles for the left
                        #riemann sum
    mainWindow.destroy()
    lrsWindow=Tk()
    lrsWindow.resizable(width=False,height=False)
    topicLabel=Label(lrsWindow,text="Left Riemann Sum", font = ("Papyrus",30,"bold"))
    topicLabel.grid(columnspan=2, sticky = "NE"+"SW")
    functLabel=Label(lrsWindow,text="f(x)=", font = ("Papyrus",20))
    functLabel.grid(row=1,column=0, sticky = "NE"+"SW")
    functEntry=Entry(lrsWindow)
    functEntry.grid(row=1,column=1, sticky = "NE"+"SW")
    uLLabel=Label(lrsWindow,text="Upper Limit=", font = ("Papyrus",20))
    uLLabel.grid(row=2,column=0, sticky = "NE"+"SW")
    uLEntry=Entry(lrsWindow)
    uLEntry.grid(row=2,column=1, sticky = "NE"+"SW")
    lLLabel=Label(lrsWindow,text="Lower Limit=", font = ("Papyrus",20))
    lLLabel.grid(row=3,column=0, sticky = "NE"+"SW")
    lLEntry=Entry(lrsWindow)
    lLEntry.grid(row=3,column=1, sticky = "NE"+"SW")
    intLabel=Label(lrsWindow,text="Number of rectangles=", font = ("Papyrus",20))
    intLabel.grid(row=4,column=0, sticky = "NE"+"SW")
    intEntry=Entry(lrsWindow)
    intEntry.grid(row=4,column=1, sticky = "NE"+"SW")
    answer=StringVar()
    ansLabel1=Label(lrsWindow,text="Answer", font = ("Papyrus",20))
    ansLabel1.grid(row=5,column=0, sticky = "NE"+"SW")
    ansLabel2=Label(lrsWindow,textvariable=answer)
    ansLabel2.grid(row=5,column=1, sticky = "NE"+"SW")
    def calclrSum():
        f=functEntry.get()
        g=lLEntry.get()
        h=uLEntry.get()
        i=intEntry.get()
        asum=lrSum(f,g,h,i)
        answer.set(asum)
        drawLRS(f,float(g),float(h),int(i))
    submitBut=Button(lrsWindow,text="Submit",command=calclrSum, font = ("Papyrus",20))
    submitBut.grid(row=6,column=1, sticky = "NE"+"SW")
    def back():
        lrsWindow.destroy()
        rMain()
    cancelButton=Button(lrsWindow,text="Back",command=back, font = ("Papyrus",20))
    cancelButton.grid(row=6,column=0, sticky = "NE"+"SW")
    mainloop()



def rMain():     #This function creates the GUI interface you see when you start the program
                 #It has four buttons. Three of them allow you to choose which riemann sum
                 #you want to calculate. The last allows you to terminate the program
    global mainWindow
    mainWindow=Tk()
    mainWindow.resizable(width=False,height=False)
    titleLab = Label(mainWindow, text = "Riemann Sums", font = ("Papyrus",30,"bold"))
    titleLab.grid(row=0, column = 0, sticky = "NE"+"SW")
    lrSumButton=Button(mainWindow,text="Left Riemann Sum",command=createLRSWindow, font = ("Papyrus",20))
    lrSumButton.grid(row=1,column=0, sticky = "NE"+"SW")
    rrSumButton=Button(mainWindow,text="Right Riemann Sum",command=createrrSWindow,font = ("Papyrus",20))
    rrSumButton.grid(row=2,column=0, sticky = "NE"+"SW")
    mrSumButton=Button(mainWindow,text="Middle Riemann Sum",command=createmrSWindow,font = ("Papyrus",20))
    mrSumButton.grid(row=3,column=0, sticky = "NE"+"SW")
    def cancel():
        mainWindow.destroy()
    cancelButton=Button(mainWindow,text="Terminate Program",command=cancel, font = ("Papyrus",20))
    cancelButton.grid(row=4,column=0,columnspan=1, sticky = "NE"+"SW")
    mainloop()

    
    
rMain()   #calling the rMain function
    




