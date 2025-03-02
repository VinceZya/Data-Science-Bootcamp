def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("1. Fibonacci series (10 terms):")
print(fibonacci(10))
print("-" * 40)


sample_list = [10, 20, 30, 40, 50, 60, 70, 80]

odd_index_numbers = sample_list[1::2]
print("2. Numbers at odd indices of the list:")
print(odd_index_numbers)
print("-" * 40)


text = """
I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!
"""
words = [word for word in text.split(" ")]
unique_words = set(words)
print("3. Number of different words in the text:")
print(len(unique_words))
print("-" * 40)


def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

test_word = "Hello world"
print("4. Count of vowels in '{}':".format(test_word))
print(count_vowels(test_word))
print("-" * 40)


animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print("5. Animals in all caps:")
for animal in animals:
    print(animal.upper())
print("-" * 40)


print("6. Odd or Even from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
print("-" * 40)


def sum_of_integers(a, b):
    return a + b

try:
    a = int(input("7. Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    print("The sum of the integers is:", sum_of_integers(a, b))
except ValueError:
    print("Invalid input. Please enter valid integers.")
