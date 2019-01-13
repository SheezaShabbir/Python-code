def adding_report(report="T"):
  total = 0
  items = ""
  while True:
    int_input = input("Input an integer to add to the total or Q to quit: ")
    if int_input.isdigit() == True:
      total = int(total) + int(int_input)
      if report.upper() == "A":
        items = items + int_input + "\n"
    elif int_input.upper().startswith("Q") == True:
      if report.upper() == "A":
        print("\n" + "Items: " +  "\n" + str(items))
        print("Total: " + str(total))
        break
      elif report.upper() == "T":
        print("\n" + "Total: " + str(total))
        break
    else:
      print("Invalid input.")
      
adding_report()
x = ["this", "is", "a" True "list"]
print(x)
