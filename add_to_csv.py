### File used to create new entries in order to gather training and test data for Natural Language Model.
import csv # import csv module - dataset is stored as csv file.

to_add = [] # list for tasks to be added.
brek = False
while not brek: # use brek as an 'anchor' in a while loop
	title = input("Title of Todo: ") # ask for title of record
	cat = input("Type of Todo: ") # ask for category of record
	if cat not in ["W", "H", "S"]: # check category is not valid, wherein, 'W' is work, 'H' is home and 'S' is shopping
		continue # restart this loop
	else: # if category is valid...
		to_add.append([title, cat]) # add this task to the list of tasks that will be added to the csv, put them in the form of a list.
	ex = input("Exit? ") # ask if i want to stop adding data
	brek = True if ex == "y" else print("...") # exit if want to stop.

with open("todos.csv", "a") as f: # open the dataset in append mode
	writer = csv.writer(f, delimiter=',')
	writer.writerows(to_add) # write new tasks to dataset.


