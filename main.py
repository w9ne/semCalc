import tkinter as tk

prgSponFunds = tk.IntVar()
personalFunds = tk.IntVar()
iworkStudentEmployment = tk.IntVar()


# Initialize and Start Window
root = tk.Tk()
root.title("Financial Semester Calculator")
root.geometry("600x400")

# Label Program Sponsor Funds
# This is basically IWORK AMT based off 4 years

programSponsorFunds = tk.Label(root,text='Program Sponor Amount Number', 
font= (calibre, 10, bold))


root.mainloop()