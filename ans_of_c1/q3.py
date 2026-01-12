# Write a program that converts a number (0-99) into its English word representation.
# For example: 23 → "twenty three", 5 → "five"

num = int(input("Enter a number (0-99): "))

ones = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]

teens = [
    "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
]

if 0 <= num < 10:
    print(ones[num])

elif 10 <= num < 20:
    print(teens[num - 10])

elif 20 <= num < 100:
    if num % 10 == 0:
        print(tens[num // 10])
    else:
        print(tens[num // 10] + " " + ones[num % 10])

else:
    print("Number out of range")
