import os
import re
import tkinter as tk
from tkinter import ttk


def load_tasks():
    lable3.delete(0, tk.END)
    try:
        with open('Student_name', "r") as file:
            for task in file:
                lable3.insert(tk.END, task.strip())
    except FileNotFoundError:
        open('Student_name', "w").close()


def addMarks():
    


    Student_name  = Enter3.get().strip().lower()
    subject_s = combom.get()
    Marks = Enter5.get().strip()
    class_nma = Enter6.get()
    rollnow = Spin3.get()
    father = Enter2.get().lower()
    totalmarks = Total_mark.get()
    # stn = f'{Student_name} {father}'
    
    file = open(f'class{class_nma}\{Student_name}', 'r')
    a = file.read()
    b = a.split()
    rollno = b[13]
    

    
    if rollnow == rollno:
        with open(f'class{class_nma}\{Student_name}', "a") as file:
            file.write(f'\n{subject_s}                                 {Marks}                                                {totalmarks}')
        load_tasks()  # now Python knows this function exists
        # Entery6.delete(0, tk.END)
    else:
        root = tk.Tk()
        root.geometry('20x100')
        root.title('Error!')
        lable1 = ttk.Label(root, text = 'Something is wrong', background='red', anchor='center')
        lable1.pack(expand=True, fill='both')
        root.mainloop()
    # file.close()





def showresult():
    student_name = Student_name.get().strip().lower()
    student_class = Student_class.get().strip().lower()

    # clear previous results
    lable40.delete(0, tk.END)

    file_path = os.path.join(f'class{student_class}', student_name)

    try:
        with open(file_path, "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:  # skip empty lines
                    lable40.insert(tk.END, clean_line)
    except FileNotFoundError:
        # create an empty file if it doesn't exist
        os.makedirs(f'class{student_class}', exist_ok=True)
        # open(file_path, "w").close()




def obtainedmarks(): 
    classs = Student_class.get()
    student = Student_name.get()
    file = open(f'class{classs}\{student}', 'r')
    
    data = file.read().split()
    file.close()

    total = 0
    index = 23   # starting index

    while index < len(data):
        try:
            total += int(data[index])
        except:
            pass
        index += 3
    lable34var.set(total)
    print(total)
    
def teachera():
    counte = Teacher_total.get()
    file = open('teacher.txt', 'w')
    lable6var.set(f'{counte}')
    file.write(f'{counte}')
    
    
    file.close()
    
def he():
    file = open('teacher.txt', 'r')
    a = file.read()
    lable6var.set(a) 
    file.close()   
    
def totalmarks(): 
    classs = Student_class.get()
    student = Student_name.get()
    file = open(f'class{classs}\{student}', 'r')
    
    data = file.read().split()
    file.close()

    totala = 0
    index = 24   # starting index

    while index < len(data):
        try:
            totala += int(data[index])
        except:
            pass
        index += 3
    lable37var.set(totala)
    print(totala)

def percentage():
    
    classs = Student_class.get()
    student = Student_name.get()

    # Load student file
    with open(f'class{classs}\\{student}', 'r') as file:
        data = file.read().split()

    # Calculate obtained marks using index 23
    obtained = 0
    idx = 23
    while idx < len(data):
        try:
            obtained += int(data[idx])
        except:
            pass
        idx += 3

    lable34var.set(obtained)
    print("Obtained:", obtained)

    # Calculate total marks using index 24
    total_marks = 0
    idx = 24
    while idx < len(data):
        try:
            total_marks += int(data[idx])
        except:
            pass
        idx += 3

    lable37var.set(total_marks)
    print("Total Marks:", total_marks)

    # Guard against division by zero
    if total_marks == 0:
        percent = 0
    else:
        percent = (obtained / total_marks) * 100

    print("Percentage:", percent)
    # lablePercentVar.set(percent)   # If you have a label for percentage

    lable101var.set(percent)
    


def resultbar():
    showresult()
    obtainedmarks()
    totalmarks()
    percentage()





def add():
    roll_no = spne.get()
    gende = gender.get()
    task = Enter1.get().strip().lower()
    father = Enter2.get().lower()
    class_name = clas_no.get()
    tasks = f'{task} {father}'
    if task:
        with open('Student_name', "a") as file:
            file.write(f"{roll_no}_ {task}  {father}\n")
        load_tasks()  # now Python knows this function exists
        Enter1.delete(0, tk.END)
        file = open(f'class{class_name}\{tasks}', 'w')
        file.write(f'Name = {task}\nFather name = {father}\nGender = {gende}\nRoll No.  = {roll_no}\nClass = {class_name}\n\nSubjects:                         Obtained Marks:                                Total marks:' )
        file.close()



def deletetext():
    Enter1.delete(0, tk.END)

def deletetext2():
    Enter2.delete(0, tk.END)

def update_count():
    try:
        with open('Student_name', 'r') as file:
            count = sum(1 for _ in file)
        lable4.config(text=f"{count}")
    except FileNotFoundError:
        lable4.config(text="File not found!")



def removetasks():
    word_to_remove = Enter1.get().strip()
    
    with open("Student_name", "r") as file:
        lines = file.readlines()
    
    with open("Student_name", "w") as file:
        for line in lines:
            # if the line doesn't contain the word, keep it
            if not re.search(rf"\b{re.escape(word_to_remove)}\b", line):
                file.write(line)
    os.remove(word_to_remove)
    load_tasks()



def main():
   
    add()
    deletetext()
    update_count()
    deletetext2()
def main2():
    removetasks()
    update_count()
    deletetext()
    deletetext2()

def totlestudent():
    pass



window = tk.Tk()
window.title('Student Mangment System')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

main_notebook = ttk.Notebook(window)




Home_fram = ttk.Frame(master=main_notebook)
Marks_fram = ttk.Frame(master=main_notebook)
result_fram = ttk.Frame(main_notebook)
Setting_fram = ttk.Frame(main_notebook)
newstudent_fram = ttk.Frame(main_notebook)



main_notebook.add(Home_fram,text = 'Home')
main_notebook.add(Marks_fram , text = 'Marks')
main_notebook.add(result_fram , text = 'Result')
main_notebook.add(newstudent_fram, text = 'Add Student')
main_notebook.add(Setting_fram, text = 'Setting')

main_notebook.pack(expand = True , fill = 'both')


#colour fo the background
# colour = ttk.Label(Home_fram,background='hotpink')
# colour.place(x = 0 ,y = 150, width = 150 , height = 200)


#----------------------------------------------------Home page-----------------------------------------------------------------------------------------
lable1 = ttk.Label(Home_fram, text='Welcome To Academy', font='Timesroaman 40 bold ', background='skyblue',anchor='center')
lable1.place(x = 0 , y = 0, width=1700 , height= 150)

lable2 = ttk.Label(Home_fram,text='Student Mangemeant System:' , font='Timesroman 15 bold')
lable2.place(x = 0 , y = 150)


lablefa = ttk.Label(Home_fram, text = 'Student:' , font = 'Timesroman 11')
lablefa.place(x = 400, y = 280)
lable4 = ttk.Label(Home_fram, text='0' , font='Timesroman 20 bold', background='lightpink',anchor='center')
lable4.place(x = 400, y = 300, width= 100 , height= 100 )
update_count()
lablefa1 = ttk.Label(Home_fram, text = 'Classes:' , font = 'Timesroman 11')
lablefa1.place(x = 700, y = 280)
lable5 = ttk.Label(Home_fram, text='12' , font='Timesroman 20 bold', background='lightpink',anchor='center')
lable5.place(x = 700, y = 300, width= 100 , height= 100 )


lablefa2 = ttk.Label(Home_fram, text = 'Teacher:' , font = 'Timesroman 11')
lablefa2.place(x = 1000, y = 280)
lable6var = tk.StringVar()
lable6 = ttk.Label(Home_fram, text='0' , font='Timesroman 20 bold', background='lightpink',anchor='center', textvariable = lable6var)
lable6.place(x = 1000, y = 300, width= 100 , height= 100 )
he()

# ------------------------------------------------------Marks fram---------------------------------------------------------------------------------
lable12 = ttk.Label(Marks_fram, text='Enter a marks of the student', font='Timesroaman 40 bold ', background='skyblue',anchor='center')
lable12.place(x = 0 , y = 0, width=1700 , height= 150)

lable13  = ttk.Label(Marks_fram , text='About:' , font='Timesroman 10 bold')
lable13.place(x=  0 , y = 160)
lable14 = ttk.Label(Marks_fram, text='1) You can add Marks of the studen by enter a name and roll no.')
lable14.place(x = 0 , y = 180)
lable15 = ttk.Label(Marks_fram, text='2) Enter a name and roll no carefully.')
lable15.place(x = 0 , y = 200)
lable17 = ttk.Label(Marks_fram, text = 'Enter a student name:')
lable17.place(x = 50 , y = 380)
Enter3 = ttk.Entry(Marks_fram, font = 'Timesroman 14')
Enter3.place(x = 50, y = 400 , width = 200 , height = 40)

lable17 = ttk.Label(Marks_fram, text = 'Enter a Roll no:')
lable17.place(x = 350 , y = 380)
Spin3 = ttk.Spinbox(Marks_fram , from_= 0 , to=200000000000 , increment=1, font = 'Tomesroman 14')
Spin3.place(x = 350 , y = 400, width = 200 , height = 40)

subject = ['Physics    ' , 'Computer  ' , 'urdu(9-12) ', 'Eng(9-12) ','Math        ' , 'T.Q          ' , 'Chemistry  ', 'Islamiyat' , 'English_A' , 'Urdu_A    ' , "English_B" , "Urdu_B    " ]
lable18 = ttk.Label(Marks_fram, text = 'Enter a Sunject:')
lable18.place(x = 650 , y = 380)
combom = ttk.Combobox(Marks_fram, font = 'Timesroman  14')
combom['value'] = subject
combom.place(x = 650 , y = 400 , width = 200 , height = 40)

lable19 = ttk.Label(Marks_fram, text = "Enter a marks:")
lable19.place(x = 950 , y = 380)
Enter5 = ttk.Entry(Marks_fram,font = 'Timesroman 14')
Enter5.place(x = 950 , y  = 400 ,width = 200 , height = 40)

lable20 = ttk.Label(Marks_fram, text = 'Enter a class:')
lable20.place(x= 1250 ,y = 380)
Enter6 = ttk.Entry(Marks_fram,font = 'Timesroman 14')
Enter6.place(x = 1250 , y  = 400 ,width = 200 , height = 40)

button112 = tk.Button(Marks_fram , text = 'ADD', bg = 'skyblue', command=addMarks)
button112.place(x  = 450, y = 500 , width = 100 , height = 40)


button112 = tk.Button(Marks_fram , text = 'UPDATE', bg = 'skyblue')
button112.place(x  = 800, y = 500 , width = 100 , height = 40)

lable_total_marks = ttk.Label(Marks_fram, text = 'Total Mark:', font = 'Timesroman 10 bold')
lable_total_marks.place(x = 1300, y = 160)
Total_mark = ttk.Entry(Marks_fram)
Total_mark.place(x = 1400, y  = 160,width = 200, height = 30)

#------------------------------------------------- Setting fram--------------------------------------------------------------------------------------------
lable12 = ttk.Label(Setting_fram, text='Set the Deflaut values', font='Timesroaman 40 bold ', background='skyblue',anchor='center')
lable12.place(x = 0 , y = 0, width=1700 , height= 150)

lable22 = ttk.Label(Setting_fram, text = "Enter a total marks of the following Subject:" , font = 'Timesroman 11 bold')
lable22.place(x = 0 , y = 150)



lable23 = ttk.Label(Setting_fram, text = 'Teachers:' , font = 'Timesroman 9 bold')
lable23.place(x = 0 , y = 200)
Teacher_total = ttk.Entry(Setting_fram)
Teacher_total.place(x = 100 , y = 200)

buttonteach = tk.Button(Setting_fram , text = 'Enter', command = teachera)
buttonteach.place(x = 300,  y = 200)

lable24 = ttk.Label(Setting_fram, text = 'Computer:' , font = 'Timesroman 9 bold')
lable24.place(x = 0 , y = 230)
Entery24 = ttk.Entry(Setting_fram)
Entery24.place(x = 100 , y = 230)



lable25 = ttk.Label(Setting_fram, text = 'Urdu(9-12):' , font = 'Timesroman 9 bold')
lable25.place(x = 0 , y = 260)
Urdu9_total_Marks = ttk.Entry(Setting_fram)
Urdu9_total_Marks.place(x = 100 , y = 260)


lable26 = ttk.Label(Setting_fram, text = 'English(9-12):' , font = 'Timesroman 9 bold')
lable26.place(x = 0 , y = 290)
English9_total_Marks = ttk.Entry(Setting_fram)
English9_total_Marks.place(x = 100 , y = 290)



lable27 = ttk.Label(Setting_fram, text = 'Math:' , font = 'Timesroman 9 bold')
lable27.place(x = 0 , y = 320)
Math_total_Marks = ttk.Entry(Setting_fram)
Math_total_Marks.place(x = 100 , y = 320)


lable28 = ttk.Label(Setting_fram, text = 'T.Q:' , font = 'Timesroman 9 bold')
lable28.place(x = 0 , y = 350)
TQ_total_Marks = ttk.Entry(Setting_fram)
TQ_total_Marks.place(x = 100 , y = 350)


lable29 = ttk.Label(Setting_fram, text = 'Chemistry:' , font = 'Timesroman 9 bold')
lable29.place(x = 0 , y = 380)
Chemistry_total_Marks = ttk.Entry(Setting_fram)
Chemistry_total_Marks.place(x = 100 , y = 380)



lable30 = ttk.Label(Setting_fram, text = 'Islamiyat:' , font = 'Timesroman 9 bold')
lable30.place(x = 0 , y = 410)
Islamiyat_total_Marks = ttk.Entry(Setting_fram)
Islamiyat_total_Marks.place(x = 100 , y = 410)



lable31 = ttk.Label(Setting_fram, text = 'English A:' , font = 'Timesroman 9 bold')
lable31.place(x = 0 , y = 440)
EnglishA_total_Marks = ttk.Entry(Setting_fram)
EnglishA_total_Marks.place(x = 100 , y = 440)



lable32 = ttk.Label(Setting_fram, text = 'English B:' , font = 'Timesroman 9 bold')
lable32.place(x = 0 , y = 470)
EnglishB_total_Marks = ttk.Entry(Setting_fram)
EnglishB_total_Marks.place(x = 100 , y = 470)

lable33 = ttk.Label(Setting_fram, text = 'Urdu B:' , font = 'Timesroman 9 bold')
lable33.place(x = 0 , y = 500)
UrduB_total_Marks = ttk.Entry(Setting_fram)
UrduB_total_Marks.place(x = 100 , y = 500)


lable33 = ttk.Label(Setting_fram, text = 'Urdu A:' , font = 'Timesroman 9 bold')
lable33.place(x = 0 , y = 530)
UrduA_total_Marks = ttk.Entry(Setting_fram)
UrduA_total_Marks.place(x = 100 , y = 530)




# ----------------------------------------------------------Add student fram---------------------------------------------------------------------------
lable1 = ttk.Label(newstudent_fram, text='Add a Student', font='Timesroaman 40 bold ', background='skyblue',anchor='center')
lable1.place(x = 0 , y = 0, width=1700 , height= 150)

lable7 = ttk.Label(newstudent_fram,text='Enter a Student name:')
lable7.place(x =0 , y = 160)
Enter1 = ttk.Entry(newstudent_fram )
Enter1.place(x = 0 , y =180, width=200 ,height=25 )
lable8 = ttk.Label(newstudent_fram, text='Enter a father name:')
lable8.place(x =0 , y = 220 )
Enter2 = ttk.Entry(newstudent_fram)
Enter2.place(x = 0 , y = 240, width=200 ,height=25)

lable3 = tk.Listbox(master=newstudent_fram,width=1000 , height=20 , font='Timesroman 10')
lable3.place(x = 0 , y = 400)
load_tasks()

button = tk.Button(newstudent_fram, text='ADD', bg='skyblue' , command=main)
button.place(x = 10, y = 300 , width=50 , height=25 )

button = tk.Button(newstudent_fram, text='DEL', bg='skyblue' , command=main2)
button.place(x = 90, y = 300 , width=50 , height=25 )
# buttoncard = tk.Button(newstudent_fram, text = 'Card', bg = 'skyblue', command = card)
# buttoncard.place(x = 170, y = 300, width = 50, height = 25)
gender = tk.StringVar()
radio1  = ttk.Radiobutton(newstudent_fram,text='male', variable=gender, value='male')
radio1.place(x = 550 , y = 180)

radio2  = ttk.Radiobutton(newstudent_fram,text='female', variable=gender, value='female')
radio2.place(x =550, y = 240)

lable9  = ttk.Label(newstudent_fram, text='Enter a Roll NO.')
lable9.place(x =300 , y = 220 )

with open('Student_name', 'r') as file:
        count = sum(1 for _ in file)
        counte = count + 1
spanvar = tk.IntVar(value=counte)
spne = ttk.Spinbox(newstudent_fram, from_=0 , to= 20000000 , increment=1, textvariable=spanvar)
spne.place(x = 300 , y = 240, width=190 ,height=25)

lable10 = ttk.Label(newstudent_fram, text='Enter a class:')
lable10.place(x = 300 , y = 160)
clas_no = ttk.Spinbox(newstudent_fram, from_=0 , to= 12 , increment=1)
clas_no.place(x = 300 , y = 180, width=190 ,height=25)

# ------------------------------------------------------Result---------------------------------------------------------------------------------------
lable1 = ttk.Label(result_fram, text='Result of the Students', font='Timesroaman 40 bold ', background='skyblue',anchor='center')
lable1.place(x = 0 , y = 0, width=1700 , height= 150)


lable31 = ttk.Label(result_fram , text = 'Enter a student name:')
lable31.place(x = 0, y = 170)
Student_name  = ttk.Entry(result_fram, font = 'Timesroman 15 ')
Student_name.place(x = 0 ,y = 190, width = 200, height= 40)

lable31 = ttk.Label(result_fram , text = 'Enter a student roll no:')
lable31.place(x = 0, y = 250)
Student_rollno  = ttk.Entry(result_fram, font = 'Timesroman 15 ')
Student_rollno.place(x = 0 ,y = 270, width = 200, height= 40)

buttontosee =  tk.Button(result_fram, bg = 'skyblue', text = 'Result', command=resultbar)
buttontosee.place(x = 50 , y = 340, width = 80 , height = 30)

lable35 = ttk.Label(result_fram , text = 'Obtain marks:')
lable35.place(x = 900, y  = 180)
lable34var = tk.IntVar()
lable34 = ttk.Label(result_fram, text='obtain marks', font='Timesroman 18 bold', background='lightpink', textvariable=lable34var, anchor='center')
lable34.place(x = 900, y = 200 , width  = 100 , height = 100)

lable36 = ttk.Label(result_fram , text = 'Total marks:')
lable36.place(x = 1100, y  = 180)
lable37var = tk.IntVar()
lable37 = ttk.Label(result_fram, text='total marks', font='Timesroman 18 bold', background='lightpink', textvariable=lable37var, anchor='center')
lable37.place(x = 1100 ,y = 200 , width  = 100 , height = 100)



lable100 = ttk.Label(result_fram , text = 'Percentage %:')
lable100.place(x = 1300, y  = 180)
lable101var = tk.IntVar()
lable102 = ttk.Label(result_fram, text='total marks', font='Timesroman 18 bold', background='lightpink', textvariable=lable101var, anchor='center')
lable102.place(x = 1300 ,y = 200 , width  = 100 , height = 100)










lable41 = ttk.Label(result_fram , text = 'Enter a student class:')
lable41.place(x = 300, y = 170)
Student_class  = ttk.Entry(result_fram, font = 'Timesroman 15 ')
Student_class.place(x = 300 ,y = 190, width = 200, height= 40)





lable40 = tk.Listbox(master=result_fram,width=1000 , height=30 , font='Timesroman 10')
lable40.place(x = 0 , y = 400)
showresult()














window.mainloop()