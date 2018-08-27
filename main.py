#!/usr/bin/python3.5

from tkinter import *

temp = "Welcome"

root = Tk()
root.geometry("640x800")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command = text.yview)

# opening the book

books = {
	1:'./Bible/Genesis.txt',
	2:'./Bible/Exodus.txt',
	3:'./Bible/Leviticus.txt',
	4:'./Bible/Numbers.txt',
	5:'./Bible/Deuteronomy.txt',
	6:'./Bible/Joshua.txt',
	7:'./Bible/Judges.txt',
	8:'./Bible/Ruth.txt',
	9:'./Bible/1Samuel.txt',
	10:'./Bible/2Samuel.txt',
	11:'./Bible/1Kings.txt',
	12:'./Bible/2Kings.txt',
	13:'./Bible/1Chronicles.txt',
	14:'./Bible/2Chronicles.txt',
	15:'./Bible/Ezra.txt',
	16:'./Bible/Nehemiah.txt',
	17:'./Bible/Esther.txt',
	18:'./Bible/Job.txt',
	19:'./Bible/Psalms.txt',
	20:'./Bible/Proverbs.txt',
	21:'./Bible/Ecclesiastes.txt',
	22:'./Bible/Song.txt',
	23:'./Bible/Isaiah.txt',
	24:'./Bible/Jeremiah.txt',
	25:'./Bible/Lamentations.txt',
	26:'./Bible/Ezekiel.txt',
	27:'./Bible/Daniel.txt',
	28:'./Bible/Hosea.txt',
	29:'./Bible/Joel.txt',
	30:'./Bible/Amos.txt',
	31:'./Bible/Obadiah.txt',
	32:'./Bible/Jonah.txt',
	33:'./Bible/Micah.txt',
	34:'./Bible/Nahum.txt',
	35:'./Bible/Habakkuk.txt',
	36:'./Bible/Zephaniah.txt',
	37:'./Bible/Haggai.txt',
	38:'./Bible/Zechariah.txt',
	39:'./Bible/Malachai.txt',
	40:'./Bible/Matthew.txt',
	41:'./Bible/Mark.txt',
	42:'./Bible/Luke.txt',
	43:'./Bible/John.txt',
	44:'./Bible/Acts.txt',
	45:'./Bible/Romans.txt',
	46:'./Bible/1Corinthians.txt',
	47:'./Bible/2Corinthians.txt',
	48:'./Bible/Galatians.txt',
	49:'./Bible/Ephesians.txt',
	50:'./Bible/Philippians.txt',
	51:'./Bible/Colossians.txt',
	52:'./Bible/1Thessalonians.txt',
	53:'./Bible/2Thessalonians.txt',
	54:'./Bible/1Timothy.txt',
	55:'./Bible/2Timothy.txt',
	56:'./Bible/Titus.txt',
	57:'./Bible/Philemon.txt',
	58:'./Bible/Hebrews.txt',
	59:'./Bible/James.txt',
	60:'./Bible/1Peter.txt',
	61:'./Bible/2Peter.txt',
	62:'./Bible/1John.txt',
	63:'./Bible/2John.txt',
	64:'./Bible/3John.txt',
	65:'./Bible/Jude.txt',
	66:'./Bible/Revelation.txt'

}

def change_book(num):
	#print("We Are Awesome")
	global books
	title = books.get(num)
	file = open(title, 'rt')
	temp_text = file.read()
	global text
	text.config(state=NORMAL)
	text.delete('1.0',END)
	text.insert(END, temp_text)
	text.pack(fill=BOTH, expand=TRUE)
	text.config(state=DISABLED)

	


########### Creating the screen ################


##### The Menu #####
menu = Menu(root)
books_menu = Menu(menu)
menu.add_cascade(label="Books", menu=books_menu)
books_menu.add_command(label="Genesis", command=lambda: change_book(1))
books_menu.add_command(label="Exodus", command=lambda: change_book(2))
books_menu.add_command(label="Leviticus", command=lambda: change_book(3))
books_menu.add_command(label="Numbers", command=lambda: change_book(4))
books_menu.add_command(label="Deuteronomy", command=lambda: change_book(5))
books_menu.add_command(label="Joshua", command=lambda: change_book(6))
books_menu.add_command(label="Judges", command=lambda: change_book(7))
books_menu.add_command(label="Ruth", command=lambda: change_book(8))
books_menu.add_command(label="1 Samuel", command=lambda: change_book(9))
books_menu.add_command(label="2 Samuel", command=lambda: change_book(10))
books_menu.add_command(label="1 Kings", command=lambda: change_book(11))
books_menu.add_command(label="2 Kings", command=lambda: change_book(12))
books_menu.add_command(label="1 Chronicles", command=lambda: change_book(13))
books_menu.add_command(label="2 Chronicles", command=lambda: change_book(14))
books_menu.add_command(label="Ezra", command=lambda: change_book(15))
books_menu.add_command(label="Nehemiah", command=lambda: change_book(16))
books_menu.add_command(label="Esther", command=lambda: change_book(17))
books_menu.add_command(label="Job", command=lambda: change_book(18))
books_menu.add_command(label="Psalms", command=lambda: change_book(19))
books_menu.add_command(label="Proverbs", command=lambda: change_book(20))
books_menu.add_command(label="Ecclesiastes", command=lambda: change_book(21))
books_menu.add_command(label="Song of Solomon", command=lambda: change_book(22))
books_menu.add_command(label="Isaiah", command=lambda: change_book(23))
books_menu.add_command(label="Jeremiah", command=lambda: change_book(24))
books_menu.add_command(label="Lamentations", command=lambda: change_book(25))
books_menu.add_command(label="Ezekiel", command=lambda: change_book(26))
books_menu.add_command(label="Daniel", command=lambda: change_book(27))
books_menu.add_command(label="Hosea", command=lambda: change_book(28))
books_menu.add_command(label="Joel", command=lambda: change_book(29))
books_menu.add_command(label="Amos", command=lambda: change_book(30))
books_menu.add_command(label="Obadiah", command=lambda: change_book(31))
books_menu.add_command(label="Jonah", command=lambda: change_book(32))
books_menu.add_command(label="Micah", command=lambda: change_book(33))
books_menu.add_command(label="Nahum", command=lambda: change_book(34))
books_menu.add_command(label="Habakkuk", command=lambda: change_book(35))
books_menu.add_command(label="Zephaniah", command=lambda: change_book(36))
books_menu.add_command(label="Haggai", command=lambda: change_book(37))
books_menu.add_command(label="Zechariah", command=lambda: change_book(38))
books_menu.add_command(label="Malachai", command=lambda: change_book(39))

books_menu.add_separator()

books_menu.add_command(label="Matthew", command=lambda: change_book(40))
books_menu.add_command(label="Mark", command=lambda: change_book(41))
books_menu.add_command(label="Luke", command=lambda: change_book(42))
books_menu.add_command(label="John", command=lambda: change_book(43))
books_menu.add_command(label="Acts", command=lambda: change_book(44))
books_menu.add_command(label="Romans", command=lambda: change_book(45))
books_menu.add_command(label="1 Corinthians", command=lambda: change_book(46))
books_menu.add_command(label="2 Corinthians", command=lambda: change_book(47))
books_menu.add_command(label="Galatians", command=lambda: change_book(48))
books_menu.add_command(label="Ephesians", command=lambda: change_book(49))
books_menu.add_command(label="Philippians", command=lambda: change_book(50))
books_menu.add_command(label="Colossians", command=lambda: change_book(51))
books_menu.add_command(label="1 Thessalonians", command=lambda: change_book(52))
books_menu.add_command(label="2 Thessalonians", command=lambda: change_book(53))
books_menu.add_command(label="1 Timothy", command=lambda: change_book(54))
books_menu.add_command(label="2 Timothy", command=lambda: change_book(55))
books_menu.add_command(label="Titus", command=lambda: change_book(56))
books_menu.add_command(label="Philemon", command=lambda: change_book(57))
books_menu.add_command(label="Hebrews", command=lambda: change_book(58))
books_menu.add_command(label="James", command=lambda: change_book(59))
books_menu.add_command(label="1 Peter", command=lambda: change_book(60))
books_menu.add_command(label="2 Peter", command=lambda: change_book(61))
books_menu.add_command(label="1 John", command=lambda: change_book(62))
books_menu.add_command(label="2 John", command=lambda: change_book(63))
books_menu.add_command(label="3 John", command=lambda: change_book(64))
books_menu.add_command(label="Jude", command=lambda: change_book(65))
books_menu.add_command(label="Revelation", command=lambda: change_book(66))





######### Footer ##########




#text.pack(fill=BOTH)
root.config(menu=menu)
root.mainloop()