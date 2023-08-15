def find_item(list, item):
  #for i in range(len(list)):
    #if list[i] == item:
      #print("index is: " + str(i) + "The item is:" + str(list[i]))
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  #print("Midddle: " + str(middle))

  if list[middle-1] == item:
    #print("1-Item: "+item + "   Midddle: "+ list[middle-1])
    return True


  #Is the item in the first half of the list? 
  if list[middle-1] < item:
    #print("2-Item: "+item + "   Midddle: "+ list[middle])
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #print("3-Item: "+item + "   Midddle: "+ list[middle])
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", 
"Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False