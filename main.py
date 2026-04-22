import json

Expenses = []

def load_expenses():
   global Expenses

   try:
      with open("expenses.json", "r") as file:
         Expenses = json.load(file)
   except:
      Expenses = []


def save_expenses():
   with open("expenses.json", "w") as file:
      json.dump(Expenses, file, indent=4)


def add_expenses():
    try:
       amount = float(input("Enter amount: "))
    except:
       print("Invalid amount!")
       return
    
    category = input("Enter category: ").strip().lower()
    date = input("Enter date: ")

    expense = {
       'amount' : amount,
       'category' : category,
       'date' : date
    }

    Expenses.append(expense)
    save_expenses()
    print("Added successfully!")


def view_expenses():
    if not Expenses:
       print("No expense found")
       return

    for i, e in enumerate(Expenses):
      print(f"{i}. Amount: {e['amount']} | Category: {e['category']} | Date : {e['date']}")
       
       
def filter_expenses():
    category = input("Enter category: ").strip().lower()
       
    found = False

    for e in Expenses:
     if e['category'] == category:
        print(f"Amount: {e['amount']} | Category: {e['category']} | Date: {e['date']} |")
        found = True
     
    if not found:
     print("No category found")    


def total():
   if not Expenses:
      print("No expense found!")
      return
   
   total_exp = 0

   for e in Expenses:
      total_exp += e['amount']
      
   print("Total: ",total_exp)


def delete_expense():

   if not Expenses:
      print("No expenses found!")
      return

   for i, e in enumerate(Expenses):
      print(f"{i}Amount: {e['amount']} | Category: {e['category']} | Date: {e['date']}")
   
   try:
      choice = int(input("Enter expense no. to delete: "))
      removed = Expenses.pop(choice)
      save_expenses()
      print(f"Deleted: {removed}")
    
   except:
      print("Invalid index")


def edit_expense():
   if not Expenses:
      print("No expense found!")
      return

   for i,e in enumerate(Expenses):
      print(f"{i} Category : {e['category']} | Amount : {e['amount']} | Date : {e['date']}")
    
   try: 
    choice = int(input("Enter your choice number: "))
    expense = Expenses[choice]
   
   except:
    print("Invalid choice!")
    return

   new_category = input("Enter new category(Leave blank to keep same): ").lower().strip()
   expense['category'] = new_category

   try:
      new_amount = float(input("Enter amount(Leave blank to keep same): "))
      expense['amount'] = new_amount

   except:
      print("Invalid amount!")

   try:
    new_date = input("Enter date(Leave blank to keep same): ")
    expense['date'] = new_date

   except:
      print("Invalid date!")

   save_expenses()

load_expenses()

while True:
   
 print("\n1. Add Expenses"
      "\n2. View Expenses"
      "\n3. Filter"
      "\n4. Total"
      "\n5. Delete expense"
      "\n6. Edit expense"
      "\n7. Exit")
 try:
    choice = int(input("Enter choice: "))

 except:
    print("invalid input!")
    continue

 if choice == 1:
    add_expenses()
 elif choice == 2:
    view_expenses()
 elif choice == 3:
    filter_expenses()
 elif choice == 4:
    total()
 elif choice == 5:
    delete_expense()
 elif choice == 6:
    edit_expense()
 elif choice == 7:
    break
 else:
    print("Enter a valid choice!")

