print("Name: Moriah De Pedro")
print("=== LA #8 ====\n")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

Adi = Book("ILYSince1892", "Binibining Mia")

print("First Book Title and Author: ", Adi.title, Adi.author)

Adi.author = "Bianca Sparacino"
del Adi.author

Bal = Book("The Prince Who Stole My Glass Slippers", "Ventrecanard")
print("Second Book Title and Author: ", Bal.title, Bal.author)