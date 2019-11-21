import tkinter
import random

lunch = ['Tuna Melt', 'Peas and Pancetta', 'CondiRiso', 'GabiBabis Special Soup']
dinner = ['GabiBabis Special Chicken and Potatoes', 'Gateau', 'Polpettone']

choice_lunch = lunch[random.randint(1, len(lunch))]
choice_dinner = dinner[random.randint(1,len(dinner))]

# Generate the GUI window
window = tkinter.Tk()

# Rename the window
window.title("Random Meal Decider")

# Create a function for choosing dinner
def call_dinner():
    tkinter.Label(window, text = choice_dinner).pack()

tkinter.Button(window, text = "Random Dinner", command = call_dinner).pack()

window.mainloop()
