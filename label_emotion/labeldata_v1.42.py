import tkFileDialog as filedialog
import winsound
import os
import random
from Tkinter import *

num=[]
global i,n,check,filename,ValidData,Used
i=1
n=0
check=-1
filename=""
ValidData=[]
Used=[]


def int2str4(ind):
    if ind in range(0,10):
        name="000"+str(ind)
    elif ind in range(10,100):
        name="00"+str(ind)
    elif ind in range(100,1000):
        name="0"+str(ind)
    else:
        name=str(ind)
    return name

   
def int2str2(ind):
    if ind in range(0,10):
        name="0"+str(ind)
    else:
        name=str(ind)
    return name
    

#def getvalidtxtnum(root_road):
#    for dirPath, dirNames, fileNames in os.walk(root_road):
#        
#        for f in fileNames:
#            directory = os.path.join(dirPath,f).split('\\')
#            subdirectory = directory[-1].split('.')
#            
#            if (subdirectory[0].find("Valid")==9)&(subdirectory[1] == 'txt'):



def callback():
    global n,i,check,ValidData,Used,filename
    entry.delete(0,END)
    i=1
    Used=[]
    
    filepath=filedialog.askdirectory()
    if filepath:
        entry.insert(0,filepath)
        check=-2
        directory=filepath.split("/")  
        filename=directory[-1]  #LabelPerson00Data00V00
        print("******\n--->filename: "+filename)
        validtxtname=filename[filename.find("Data"):]+"Valid.txt"  #Data00V00Valid.txt
        vo=open(filepath.replace("/","\\")+"\\"+validtxtname,'r')  # get valid data in the txt 
        ValidData=vo.read().split("\n") 
        vo.close()
        print("*******\n--->ValidDataNEW is ")
        print(ValidData)
        while "" in ValidData:
            ValidData.remove("")
        if  os.path.exists(os.getcwd()+"\\final_ans"):
            pass
        else:
            os.makedirs(os.getcwd()+"\\final_ans")  # create folder       
        tmp_folder="tmp_"+filename+"Seg"+int2str2(n)  #tmp_LabelPerson00Data00V00Seg00
        while(os.path.exists(os.getcwd()+"\\"+tmp_folder)):
            n=n+1
            tmp_folder="tmp_"+filename+"Seg"+int2str2(n)  #tmp_LabelPerson00Data00V00Seg00           
        else:
            os.makedirs(os.getcwd()+"\\"+tmp_folder)  # create folder tmp_LabelPerson00Data00V00
#            fo=open(os.getcwd()+"\\"+tmp_folder+"\\"+filename+"Seg"+int2str2(n)+".txt",'w') 
            #LabelPerson00Data00V00Seg00.txt
#            fo.close()
            num[:]=[]    
#    return filename,ValidData
            
def playnextsound():
    global i,check,filename,ValidData,Used,n
    wavfilename=filename[filename.find("Data"):]+"Split"  #Data00V00Split
    labeltxtname=filename+"Seg"+int2str2(n) #LabelPerson00Data00V00Seg00
    if len(ValidData)==0:
        i=-4
    else:
        i=int(random.choice(ValidData))
        Used.append(int2str4(i));ValidData.remove(int2str4(i))
    print("***********\n---->i= "+int2str4(i))
        
    if(check==-3):
        if str(var.get())==" ":
            level.set("no path")
        elif os.path.exists(str(var.get())+"/"+wavfilename+int2str4(i)+".wav"):
            inputname=str(var.get())+"/"+wavfilename+int2str4(i)+".wav"
            winsound.PlaySound(inputname, winsound.SND_FILENAME)
            check=i
        else:   #the last step        
            level.set("congratulations!you have finished!")
            check=0;s=1;
            if(os.path.isdir(os.getcwd()+"\\final_ans")):{}  
            else:
                os.makedirs(os.getcwd()+"\\final_ans")
            if os.path.exists(os.getcwd()+"final_ans\\"+filename+"Seg"+int2str2(n)+".txt"):
                while(os.path.exists(os.getcwd()+"final_ans\\"+filename+"Seg"+int2str2(n)+str(s)+".txt")):
                    s=s+1
                else:
                    os.renames("tmp_"+labeltxtname+"\\"+"tmp"+int2str4(len(Used))+"\\"+labeltxtname+".txt","final_ans\\"+labeltxtname+"_"+str(s)+".txt")
            else:
                os.renames("tmp_"+labeltxtname+"\\"+"tmp"+int2str4(len(Used))+"\\"+labeltxtname+".txt","final_ans\\"+labeltxtname+".txt")
                    
    elif check==0:
        level.set("congratulations!you have finished!")
    else:
        ans="please label before going next"
        level.set(ans)
        
def playagain():    
    global check,i,ValidData,filename,Used
    if check==-2:
        i=int(random.choice(ValidData))
        Used.append(int2str4(i));ValidData.remove(int2str4(i))
        check=i
    else:
        check=check
    wavfilename=filename[filename.find("Data"):]+"Split"  #Data00V00Split
    inputname=str(var.get())+"\\"+wavfilename+int2str4(i)+".wav"
    winsound.PlaySound(inputname, winsound.SND_FILENAME)
    
def choosenum1():
    global check,n
    identifier="("+filename[17:19]+","+filename[20:]
    labeltxtname=filename+"Seg"+int2str2(n) #LabelPerson00Data00V00Seg00
#    print("---> labeltxtname= "+labeltxtname+"\n")
    if (check==i):
        num.append(identifier+","+int2str4(i)+","+str("1")+")")
        ans="1:Feels bad"
        print(ans)
        level.set(ans) 
        s=1
        while(os.path.exists(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))):
            s=s+1            
        else:
            os.makedirs(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))
        fo=open(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s)+"\\"+labeltxtname+".txt",'w')
        fo.writelines(num)
        fo.close()
        del s
        check=-3
        playnextsound()
    elif check==-1:
        level.set("Please open a folder")
    elif check==-2:
        level.set("Please press play")
#    elif check==-3:
#        level.set("Please press next button")
    elif check==0:
        level.set("congratulations!you have finished!")
    else:
        print("error for check") 
        print(check)

def choosenum2():  
    global check,n    
    identifier="("+filename[17:19]+","+filename[20:]
    labeltxtname=filename+"Seg"+int2str2(n) #LabelPerson00Data00V00Seg00
    if (check==i):
        num.append(identifier+","+int2str4(i)+","+str("2")+")")
        ans="2:Feels neutral"
        print(ans)
        level.set(ans) 
        s=1
        while(os.path.exists(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))):
            s=s+1            
        else:
            os.makedirs(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))
        fo=open(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s)+"\\"+labeltxtname+".txt",'w')
        fo.writelines(num)
        fo.close()
        del s
        check=-3
        playnextsound()
    elif check==-1:
        level.set("Please open a folder")
    elif check==-2:
        level.set("Please press play")
#    elif check==-3:
#        level.set("Please press next button")
    elif check==0:
        level.set("congratulations!you have finished!")
    else:
        print("error for check")
        print(check)

def choosenum3():     
    global check,n
    identifier="("+filename[17:19]+","+filename[20:]
    labeltxtname=filename+"Seg"+int2str2(n) #LabelPerson00Data00V00Seg00
    if (check==i):
        num.append(identifier+","+int2str4(i)+","+str("3")+")")
        ans="3:Feels positive"
        print(ans)
        level.set(ans) 
        s=1
        while(os.path.exists(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))):
            s=s+1            
        else:
            os.makedirs(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))
        fo=open(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s)+"\\"+labeltxtname+".txt",'w')
        fo.writelines(num)
        fo.close()
        del s
        check=-3
        playnextsound()
    elif check==-1:
        level.set("Please open a folder")
    elif check==-2:
        level.set("Please press play")    
#    elif check==-3:
#        level.set("Please press next button")
    elif check==0:
        level.set("congratulations!you have finished!")
    else:
        print("error for check")
        print(check)

#def choosenum4():   
#    global check
#    if (check==i)&(check!=-1):
#        num.append("("+str(i)+","+str("4")+")")      
#        ans=str(i)+str(": you choose 4")   
#        print(ans)
#        level.set(ans)
#        fo=open("recorddata"+str(n)+".txt",'r+')
#        fo.writelines(num)
#        fo.close()
#        check=check+1
#        playnextsound()
#    elif check==-1:
#        level.set("Please open a folder")
#    elif check==-2:
#        level.set("Please press play")
#    elif check>i:
#        level.set("Please press next button")
#    elif check==0:
#        level.set("congratulations!you have finished!")
#    else:
#        print("error for check")

#def choosenum5():     
#    global check
#    num.append(str("5")+'\n')      
#    ans=str(i)+str(": you choose 5")    
#    print(ans)
#    level.set(ans)
#    fo=open("recorddata"+str(n)+".txt",'r+')
#    fo.writelines(num)
#    fo.close()
#    check=check+1
#
def choosenum9():     
    global check,n
    identifier="("+filename[17:19]+","+filename[20:]
    labeltxtname=filename+"Seg"+int2str2(n) #LabelPerson00Data00V00Seg00
    if (check==i):
        num.append(identifier+","+int2str4(i)+","+str("9")+")")
        ans="9:Invalid Data"
        print(ans)
        level.set(ans) 
        s=1
        while(os.path.exists(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))):
            s=s+1            
        else:
            os.makedirs(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s))
        fo=open(os.getcwd()+"\\tmp_"+labeltxtname+"\\tmp"+int2str4(s)+"\\"+labeltxtname+".txt",'w')
        fo.writelines(num)
        fo.close()
        del s
        check=-3
        playnextsound()
    elif check==-1:
        level.set("Please open a folder")
    elif check==-2:
        level.set("Please press play")    
#    elif check==-3:
#        level.set("Please press next button")
    elif check==0:
        level.set("congratulations!you have finished!")
    else:
        print("error for check")
        print(check)
    
def close_window():
    root.destroy() 

#def decide_path():
#    var = StringVar(root)


root=Tk()
var = StringVar()
level=StringVar()
#var.set()

f=Frame(root,height=20,width=50)
f.pack_propagate(0)
f.pack()


w = Label(root,font="times 15 bold" ,text="BIIC_LAB Happy label")
w.pack(pady=2,side=TOP)


entry = Entry(root,width=55,textvariable=var)
entry.pack(side=TOP)
#v= Label(root,text=" number : level")
#v.pack(pady=10,anchor="sw",side=TOP)
e=Entry(root,width=35,textvariable=level)
e.pack(pady=4,side=TOP)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=callback)
filemenu.add_command(label="Close", command=close_window)
menubar.add_cascade(label="File", menu=filemenu)



b1=Button(root,text="1",width="5",fg="blue",command=choosenum1)
b1.pack(padx=6,side=LEFT)
b2=Button(root,text="2",width="5",fg="blue",command=choosenum2)
b2.pack(padx=6,side=LEFT)
b3=Button(root,text="3",width="5",fg="blue",command=choosenum3)
b3.pack(padx=6,side=LEFT)
#b4=Button(root,text="4",width="5",fg="blue")
#b4.pack(padx=6,side=LEFT)
#b5=Button(root,text="5",width="5",fg="blue")
#b5.pack(padx=6,side=LEFT)
bap=Button(root,text="play",width="10",fg="red",command=playagain)
bap.pack(pady=4,side=RIGHT)
b9=Button(root,text="9",width="5",fg="green",command=choosenum9)
b9.pack(padx=6,side=RIGHT)

#bnp=Button(root,text="next",width="10",fg="red",command=playnextsound)
#bnp.pack(pady=4,side=BOTTOM)

root.config(menu=menubar)
root.mainloop()