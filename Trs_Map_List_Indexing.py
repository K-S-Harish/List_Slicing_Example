line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
columns = position[0].lower() #we are fetching the 1st charecter of given i/p
rows = int(position[1]) # geting the 2nd item from i/p and converting it to INT form

abc = ["a","b","c"]

selected_column = abc.index(columns)
selected_row = rows - 1

map[selected_row][selected_column] = "X"

# In a NESTED List any changes made to the nested list will also reflect on the sub_list 
# contained in it.
print(f"{line1}\n{line2}\n{line3}")