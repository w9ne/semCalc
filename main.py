import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Financial Semester Calculator")
root.geometry("400x170")

#Initialize and Start Window
sem = tk.IntVar()
prgSponFunds = tk.IntVar()
personalFunds = tk.IntVar()
iworkStudentEmployment = tk.IntVar()

#Actual Code
def calculate():
    try:
        programSponsorFundsNum = int(prgSponFunds.get())
        personalFundsNum = int(personalFunds.get())
        numSemesters = int(sem.get())

        prgSponFunds.set(0)
        personalFunds.set(0)
        iworkStudentEmployment.set(0)
        sem.set(0)
        
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
        initialCal = ((150864/12) * numSemesters) - result1
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

#Label Program Sponsor Funds

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
programSponsorFunds_label.grid(row=1,column=0)
prgSponFunds_entry.grid(row=1,column=1)
personalFunds_label.grid(row=2,column=0)
personalFunds_entry.grid(row=2,column=1)
submitButton.grid(row=3,column=1)
resultLabel.grid(row=8,column=0)

#Loop Window for display
root.mainloop()