# Initialize Collections exactly as described
books = [
    ("Book Title 1", "Author A", "2025", "Programming"),
    ("Book Title 2", "Author B", "2026", "AI")
]
library_categories = {"Programming", "AI", "Cloud"}
student_wishlist = {"AI", "Cloud", "Data Science"}

print("="*50)
print("LIBRARY BOOK  ")
print("="*50)

#Start Menu with While Loop

while True:
    # Display Menu
    print("1. View Books | 2. Add Book | 3. View Categories") #using | function to separate the options in menu
    print("4. Add Wishlist | 5. Gap Analysis | 6. Exit")
    choice = input("Prompt: Input choice (1-6): ")           #firstly we took input from user to select the option from menu

    if choice == "1":     #using if statement to check the user input and perform the action accordingly
        # Iterate through books list
        for book in books:             #using for loop to iterate through the books list and print the details of each book
            title = book[0]            #for title we are taking the first element of the tuple
            author = book[1]           #for author we are taking the second element of the tuple
            year = book[2]             #for year we are taking the third element of the tuple
            category = book[3]         #for category we are taking the fourth element of the tuple
            print(title, author, year, category)  #print the details of each book
        print("Total count:", len(books))         #print the total count of books in the library with printing the length of the books list

    #Add Book Option
     
    elif choice == "2":  
        # Prompt for inputs
        title = input("Prompt title: ")       #taking input from user for title of the book
        author = input("Prompt author: ")     #taking input from user for author of the book
        year = input("Prompt year: ")         #taking input from user for year of the book
        category = input("Prompt category: ") #taking input from user for category of the book

        # Check if all fields are provided 
        if title != "" and author != "" and year != "" and category != "": #checking if all the fields are provided by the user or not
            new_book = (title, author, year, category)     #creating a new tuple with the provided inputs with the help of tuple data structure
            books.append(new_book)                         #adding the new book to the books list with the help of append method of list data structure
            library_categories.add(category)               #adding the new category to the library_categories set with the help of add method of set data structure
            print("[SUCCESS] Book added")                  #printing the success message after adding the book to the library
        else:                                              #using else statement to check if any of the fields are empty or not
            print("[ERROR] All fields mandatory!")         #print error if any field is empty.
    
    #View Option
    
    elif choice == "3":                #3 to view 
        # Display sorted unique categories
        for cat in sorted(library_categories):  #using for loop inside elif with sorted function
            print(cat)
        print("Total genres count:", len(library_categories))

    #
    
    elif choice == "4":
        req_cat = input("Prompt: requested category: ")
        
        # Check if input is non-empty
        if req_cat != "":
            student_wishlist.add(req_cat)
            print("[SUCCESS] Added to wishlist")
        else:
            print("[ERROR] Category cannot be empty")

    elif choice == "5":
        # Execute Set Operations step-by-step
        in_stock = library_categories.intersection(student_wishlist)
        to_order = student_wishlist.difference(library_categories)
        full_coverage = library_categories.union(student_wishlist)

        # Display Category Gap Analysis
        print("\n===========GAP ANALYSIS==============\n")
        print("1. Already In Stock:", in_stock)
        print("2. Purchase Order Needed:", to_order)
        print("3. Full Combined Coverage:", full_coverage)

    elif choice == "6":
        print("Thank you, goodbye!")
        break

    else:
        print("[INVALID] Enter number 1-6")


#in 20th line 
#we can do
#  if choice=="1":
#  for ind,book in enumerate



#update is for dictionary