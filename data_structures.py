# Program to create a list of integers and compute their sum

numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
total = sum(numbers)
print("The sum of the integers is:", total)

# Program to create a tuple of favorite books and print each book name on a separate line.

favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
for book in favorite_books:
    print(book)

# Program to store information about a person in a dictionary and print the dictionary
    
person_info = {}
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")
print("Person's information:")
print(person_info)


# Program to create two set of integers from user input and find their intersection

set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
set2 = set(input("Enter integers for set 2 separated by spaces: ").split())
set1 = {int(num) for num in set1}
set2 = {int(num) for num in set2}
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)

# Program to create list that store words

word_list = ["apple", "banana", "orange", "kiwi", "grape", "pineapple"]
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Original list of words:", word_list)
print("Words with odd number of characters:", odd_length_words)


