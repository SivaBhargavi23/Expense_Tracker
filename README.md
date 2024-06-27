Explanation:
The code uses a JSON file to store the expenses. When the program starts, it loads the expenses from the file using the load_expenses method. This method checks if the file exists, and if it does, it loads the expenses from the file using the json.load function. If the file does not exist, it returns an empty dictionary.
The save_expenses method is used to save the expenses to the file whenever an expense is added. It uses the json.dump function to dump the expenses to the file.
The ExpenseTracker class has an expenses dictionary to store the entered expense data. The keys are dates in the format YYYY-MM-DD, and the values are dictionaries with categories as keys and amounts as values.
The add_expense method allows users to input their daily expenses. It checks if the date and category already exist in the expenses dictionary and updates the amount accordingly.
The get_monthly_summary method calculates the total expenditure for a given month and year.
The get_category_wise_expenditure method calculates the total expenditure for a given category.
The display_expenses method displays all the entered expenses.
The main function provides a user-friendly interface for users to interact with the ExpenseTracker class. It uses a simple menu-driven approach to allow users to add expenses, get monthly summaries, get category-wise expenditure, display expenses, or exit the application.
Error handling is implemented using try-except blocks to handle unexpected inputs. For example, if the user enters an invalid date or amount, the application will prompt them to enter valid input
