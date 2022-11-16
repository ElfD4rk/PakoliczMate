import tkinter as tk
import lineEliminator
import myModule

window = tk.Tk()
window.title('Line eliminator')
window.geometry('600x400')
window.minsize(width=300, height=200)
lblGreet = tk.Label(window, text=myModule.greeting())
lblDone = tk.Label(window, text="line eliminating done")
btnImport = tk.Button(window, text="Exit", command=window.destroy)

lblGreet.pack()
lblDone.pack()
btnImport.pack()
window.mainloop()