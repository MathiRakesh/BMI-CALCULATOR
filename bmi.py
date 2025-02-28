from tkinter import *
from tkinter import messagebox

def reset():
    height.delete(0, 'end')
    weight.delete(0, 'end')

def bmi_cal():
    kg = int(weight.get())
    m = float(height.get())  # Height in meters directly
    bmi = kg / m ** 2
    bmi = round(bmi, 1)

    age_range = "under 18" if var.get() == 1 else "over 18"
    if age_range == "under 18":
        bmi_index_under18(bmi)
    else:
        bmi_index_over18(bmi)

def bmi_index_over18(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
    elif bmi >= 29.9:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI', 'Something went wrong!')

def bmi_index_under18(bmi):
    if bmi < 5:
        messagebox.showinfo('BMI', f'BMI = {bmi} - Severely underweight')
    elif 5 <= bmi < 10:
        messagebox.showinfo('BMI', f'BMI = {bmi} - Underweight')
    elif 10 <= bmi < 25:
        messagebox.showinfo('BMI', f'BMI = {bmi} - Normal')
    elif 25 <= bmi < 30:
        messagebox.showinfo('BMI', f'BMI = {bmi} - Overweight')
    elif bmi >= 30:
        messagebox.showinfo('BMI', f'BMI = {bmi} - Obese')
    else:
        messagebox.showerror('BMI', 'Something went wrong!')

def info():
    messagebox.showinfo('Info', 'v1, you can calculate your BMI.')

root = Tk()
root.title("BMI Calculator")

var = IntVar()

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

age = Label(frame, text="Select Your Age Range:", fg='red')
age.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=10)

under18 = Radiobutton(frame2, text="Under 18 years", variable=var, value=1)
under18.pack(side=RIGHT)
over18 = Radiobutton(frame2, text="Over 18 years", variable=var, value=0)
over18.pack(side=LEFT)

height_label = Label(frame, text="Enter your Height in meters:")  # Updated label
height_label.grid(row=3, column=1)
weight_label = Label(frame, text="Enter your Weight in KG:")
weight_label.grid(row=4, column=1)

height = Entry(frame)
height.grid(row=3, column=2, pady=5)
weight = Entry(frame)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, column=3, pady=10)

calculate_b = Button(frame3, text="Calculate", command=bmi_cal)
calculate_b.pack(side=LEFT)

reset_b = Button(frame3, text="Reset", command=reset)
reset_b.pack(side=RIGHT)

info_b = Button(frame3, text="Info", command=info)
info_b.pack(side=RIGHT)

root.mainloop()