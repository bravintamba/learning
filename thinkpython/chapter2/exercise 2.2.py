#question 1ss
# gives access to pi 
import math               
 # radius
r = 5
volume = (4/3) * math.pi * r**3
print("Volume of sphere with radius", r, "is", volume)


#question 2
# cover price
price = 24.95       
 # 40% discount
discount = 0.40
# number of books
copies = 60

# tranformation
book_cost = price * (1 - discount) * copies
shipping = 3 + 0.75 * (copies - 1)   # shipping cost
total = book_cost + shipping

# output
print("Total wholesale cost for", copies, "copies is", total)

#question 3
# convert paces to seconds
easy = 8*60 + 15
tempo = 7*60 + 12

# total running time (seconds)
total = easy + 3*tempo + easy

# start time: 6:52 am in minutes
start = 6*60 + 52

# end time in minutes
end = start + total // 60

# clock time
end // 60, end % 60, total % 60
print("End time is", end // 60, ":", end % 60, "with", total % 60, "seconds")