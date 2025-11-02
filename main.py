import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Financial Semester Calculator")
root.geometry("600x400")

#Initialize and Start Window
prgSponFunds = tk.IntVar()
personalFunds = tk.IntVar()
iworkStudentEmployment = tk.IntVar()

#Actual Code
def calculate():
    try:
        programSponsorFundsNum = int(prgSponFunds.get())
        personalFundsNum = int(personalFunds.get())
        prgSponFunds.set(0)
        personalFunds.set(0)
        
        #add better calc
        result1 = programSponsorFundsNum/12
        result2 = (personalFundsNum*4)/3
        
        resultText = (
            f"Program Sponsor Funds: ${result1:,.2f}\n"
            f"Personal Funds: ${result2:,.2f}\n"
            
        )
        
        resultLabel.config(text=resultText,justify='center')
        
        
    except ValueError:
        #Display error msg
        resultLabel.config(text="Needs to be number")

#Label Program Sponsor Funds
#This is basically IWORK AMT based off 4 years
programSponsorFunds_label = tk.Label(root,
text='Program Sponsor Amount',
font=('calibre',10,'bold'))

prgSponFunds_entry = tk.Entry(root,
textvariable = prgSponFunds, 
font=('calibre',10,'normal'))

#Personal funds
personalFunds_label = tk.Label(root,
text='Personal Funds',
font=('calibre',10,'bold'))

personalFunds_entry = tk.Entry(root,
textvariable = personalFunds,
font=('calibre',10,'normal'))


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
programSponsorFunds_label.grid(row=0,column=0)
prgSponFunds_entry.grid(row=0,column=1)
personalFunds_label.grid(row=1,column=0)
personalFunds_entry.grid(row=1,column=1)
submitButton.grid(row=3,column=2)
resultLabel.grid(row=5,column=0)

#TODO for IWORK Student employement 

#Loop Window for display
root.mainloop()