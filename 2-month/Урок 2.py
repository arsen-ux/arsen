# # ООП
# # принципы ООП:
#
#
class Book:
    strr = 400

    # методы

    def __int__(self, title, author, color, len):
        self.title = title
        self.author = author
        self.color = color
        self.len = len

    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author},\n'
                f'color: {self.color}, Strr: {self.strr}\n')

    def __len__(self):
        return len(self.strr + self.color + self.title + self.author)


# обьект\экземпляр класса
gород_воров = Book('город воров', 'Каныкей', 'зеленый')
kапитанская_дочка = Book('капитанская дочь', 'Пушкин', 'серый')

# beka = Book('ЭТОМИР', 'beka', 'black')
# print(len(beka))
#

gород_воров.info()
kапитанская_дочка.info()






