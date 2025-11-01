import tkinter as tk

#Actual Code
def calculate():
    
    programSponsorFunds = programSponsorFunds.get()

    print(programSponsorFunds)

    programSponsorFunds.set("")


# Initialize and Start Window
prgSponFunds = tk.IntVar()
personalFunds = tk.IntVar()
iworkStudentEmployment = tk.IntVar()

root = tk.Tk()
root.title("Financial Semester Calculator")
root.geometry("600x400")

# Label Program Sponsor Funds
# This is basically IWORK AMT based off 4 years
programSponsorFunds = tk.Label(root,text='Program Sponor Amount Number', 
font= (calibre, 10, bold))
#Widget Entry
prgSponFunds_entry = tk.Entry(root,textvariable = prgSponFunds, 
font=('calibre',10,'normal'))

root.mainloop()