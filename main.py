import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Financial Semester Calculator")
root.geometry("410x170")

#Initialize and Start Window
sem = tk.StringVar()
prgSponFunds = tk.StringVar()
personalFunds = tk.StringVar()
iworkStudentEmployment = tk.StringVar()
costOfAttendance = tk.StringVar()

#Int Check
def intCheck(value,varName):
    try:
        return int(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{varName} must be a number.")
        return None

#Actual Code
def calculate():
    try:
        #Getters
        programSponsorFundsNum = intCheck(prgSponFunds.get(),"Progran Sponsor Funds")
        personalFundsNum = intCheck(personalFunds.get(), "Personal Funds")
        numSemesters = intCheck(sem.get(),"Number Of Semesters")
        costAttendance = intCheck(costOfAttendance.get(), "Cost of Attendance")

        #Setters to 0 to initialize
        prgSponFunds.set(0)
        personalFunds.set(0)
        iworkStudentEmployment.set(0)
        sem.set(0)
        costOfAttendance.set(0)
        
        #Personal funds go by year, not by semesters
        #Checks if number is between the semester, adjusts to yearly family contribution
        if 0 <= numSemesters <= 3:
            iworkAnnualCalc = 1
        elif 4 <= numSemesters <= 6:
            iworkAnnualCalc = 2
        elif 7 <= numSemesters <= 9:
            iworkAnnualCalc = 3
        elif 10 <= numSemesters <= 12:
            iworkAnnualCalc = 4
        else:
            resultText = ("Invalid amount entered")
        
        #add better calc
        result1 = ((programSponsorFundsNum*4)/12) * numSemesters
        result2 = (personalFundsNum*iworkAnnualCalc)
        initialCal = ((costAttendance*4/12) * numSemesters) - result1
        result3 = initialCal - result2
        
        resultText = (
            f"Program Sponsor Funds: ${result1:,.0f}\n"
            f"Personal Funds: ${result2:,.0f}\n"
            f"IWORK Student Employment: ${result3:,.0f}"
        )
        resultLabel.config(text=resultText,justify='left')
        
        
    except ValueError:
        #Display error msg
        resultLabel.config(text="Needs to be number")
        print("Error code")
        return None

#Label Program Sponsor Funds

#Cost of Attendence (annual)
coa_label = tk.Label(root,
text='Cost of Attendance (annually)',
font=('calibre',10,'bold')
)

coa_entry = tk.Entry(root,
textvariable= costOfAttendance,
font=('calibre',10,'normal'))

#Number of Semesters left
semester_label = tk.Label(root,
text='Numbers of Sesmeters Left',
font=('calibre',10,'bold'))

semester_entry = tk.Entry(root,
textvariable= sem,
font=('calibre',10,'normal'))

#This is basically IWORK AMT based off 4 years
programSponsorFunds_label = tk.Label(root,
text='Program Sponsor Funds (annually)',
font=('calibre',10,'bold'))

prgSponFunds_entry = tk.Entry(root,
textvariable = prgSponFunds, 
font=('calibre',10,'normal'))

#Personal funds
personalFunds_label = tk.Label(root,
text='Personal Funds (annually)',
font=('calibre',10,'bold'))

personalFunds_entry = tk.Entry(root,
textvariable = personalFunds,
font=('calibre',10,'normal'))

#IWORK Student Employment
studentEmployment_label = tk.Label(root,
text='IWORK Student Employment',
font=('calibre',10,'bold'))

#Submit buttonz
submitButton = tk.Button(root,
text='Submit',
font=('calibre',10,'bold'),
command=calculate)

#Result Text
resultLabel = tk.Label(root, 
text="", 
font=('calibre',10,'bold'))

#Placing labels inside the window for display
semester_label.grid(row=0,column=0)
semester_entry.grid(row=0,column=1)
coa_label.grid(row=1,column=0)
coa_entry.grid(row=1,column=1)
programSponsorFunds_label.grid(row=2,column=0)
prgSponFunds_entry.grid(row=2,column=1)
personalFunds_label.grid(row=3,column=0)
personalFunds_entry.grid(row=3,column=1)
submitButton.grid(row=4,column=1)
resultLabel.grid(row=8,column=0)

#Loop Window for display
root.mainloop()