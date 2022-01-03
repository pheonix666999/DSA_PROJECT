import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QApplication, QMainWindow, Qtkinter.Label, QLineEdit, QGraphicsDropShadowEffect
from collections import Counter
from tkinter import *
from tkinter.ttk import *
import sys
import tkinter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import webbrowser
import cgitb
cgitb.enable(format='text')
# import time
# from tkhtmlview import HTMLtkinter.Label

stop_words = set(stopwords.words('english'))
snow_stemmer = SnowballStemmer(language='english')

file_lexicon = open(r"lexicon.json", "r")  # lexicon file
lexicon = json.load(file_lexicon)

file_inverted = open(r"inverted_index.json", "r")  # inverted index file
inverted_index = json.load(file_inverted)

file_doc = open(r"doc_id.json", "r")  # URL file
doc_id = json.load(file_doc)

title_file = open(r"doc_title.json", "r")  # title file
doc_title = json.load(title_file)

t_lexicon = open(r"lexicon_of_titles.json", "r")
lexicon_titles = json.load(t_lexicon)

t_inverted = open(r"inverted_index_of_titles.json", "r")
inverted_index_titles = json.load(t_inverted)

print(len(lexicon))


# data = {}
# count = 0
# word_id_title = []
# common_titles = []
# common_content = []

# temp2 = []
# temp3 = []


# temp1 = "The Last White Helmet of Idlib"
# temp1 = nltk.word_tokenize(temp1)
# for i in range(len(temp1)):
#     temp1[i] = snow_stemmer.stem(temp1[i])
# for i in temp1:
#     if i not in stop_words:
#         temp2.append(i)
# for i in temp2:
#     if (i.isalnum()):
#         temp3.append(i)
# temp3 = list(dict.fromkeys(temp3))
# print(temp3)
# temp3_title = temp3.copy()
# temp3_content = temp3.copy()


# # Checking the data in title::::::::::::::::::::::::::::::::::::::::::::::::
# while len(temp3_title) > 0:
#     for word in temp3_title:
#         if word in lexicon_titles:
#             word_id_title.append(
#                 inverted_index_titles[str(lexicon_titles[word])])
#     common_titles = set(word_id_title[0]).intersection(*word_id_title)
#     for doc_ids in common_titles:
#         if doc_title[doc_ids] not in data:
#             data[doc_title[doc_ids]] = doc_id[doc_ids]

#     temp3_title.remove(temp3_title[len(temp3_title) - 1])
#     word_id_title.clear()
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
# # word_id_content = []

# while len(temp3_content) > 0:
#     for word in temp3_content:
#         if word in lexicon:
#             word_id_content.append(inverted_index[str(lexicon[word])])

#     common_content = set(word_id_content[0]).intersection(*word_id_content)
#     for doc_ids in common_content:
#         if doc_title[doc_ids] not in data:
#             data[doc_title[doc_ids]] = doc_id[doc_ids]

#     temp3_content.remove(temp3_content[len(temp3_content) - 1])
#     word_id_content.clear()

# for i in data:
#     print(str(count), ": ", i)
#     print(str(count), ": ", data[i])
#     print()
#     count = count + 1

# end = time.time()
# print("The time of the program is: ", end - start)


# Tkinter GUI(UI)


def callback(url):
    webbrowser.open_new(url)


main = tkinter.Tk()
# main.iconbitmap('piper.ico')
# main.tkinter.call('wm', 'iconphoto', main._w, tkinter.PhotoImage(file='piper.ico'))
main.iconphoto(False, tkinter.PhotoImage(file='piper.png'))
conodition = 0

main.title('Piper 7')

main.config(bg='black')
# Adding the main window properties.
main.geometry('1366x768')
main.state('normal')
# Adding the search bar for the quries
search_box = Text(main, height=1, width=72,
                  font=("Century Gothic", 20, 'bold'))
# Setting the tkinter.Button borders

add_content = tkinter.Button(text="Add Content", bg='black', fg='yellow', font=(
    "Century Gothic", 10, 'bold'), command=lambda: tkinter.Listbox.insert(END, "To enter new content you have to put the new file in the nela-elections-2020\\newsdata and further instructons are given in the read me file."))


tkinter.Button_border1 = tkinter.Frame(main, highlightbackground="yellow",
                                       highlightthickness=2, bd=0)
tkinter.Button_border2 = tkinter.Frame(main, highlightbackground="yellow",
                                       highlightthickness=2, bd=0)
list_box_border = tkinter.Frame(
    main, highlightbackground="yellow", highlightthickness=2, bd=0)
# Adding the properties of the search engine name.
heading = tkinter.Label(main, text="Piper 7", fg='yellow', bg='black')
heading.config(font=("Century Gothic", 70, 'bold'))
# Adding the search results
tkinter.Listbox = tkinter.Listbox(main, width=1200, bg='black', fg='yellow',
                                  font=("Century Gothic", 20, 'bold'))
# Adding the search tkinter.Buttonss


def clear():
    tkinter.Listbox.delete(0, END)
    # tkinter.Button.pack_forget()
    # tkinter.btn.destroy()
    tkinter.Button.destroy()


clear_box = tkinter.Button(main, text='CLEAR BOX',
                           bg='BLACK', fg='WHITE', command=clear)


def Searching():
    # Listbox.delete(0, tkinter.END)
    temp1 = search_box.get(1.0, "end-1c")
    data = {}
    count = 0
    word_id_title = []
    word_id_content = []
    common_titles = []
    common_content = []

    temp2 = []
    temp3 = []

    print(temp1)
    # temp1 = "The Last White Helmet of Idlib"
    temp1 = nltk.word_tokenize(temp1)
    for i in range(len(temp1)):
        temp1[i] = snow_stemmer.stem(temp1[i])
    for i in temp1:
        if i not in stop_words:
            temp2.append(i)
    for i in temp2:
        if (i.isalnum()):
            temp3.append(i)
    temp3 = list(dict.fromkeys(temp3))
    print(temp3)
    temp3_title = temp3.copy()
    temp3_content = temp3.copy()

    # Checking the data in title::::::::::::::::::::::::::::::::::::::::::::::::
    while len(temp3_title) > 0:
        for word in temp3_title:
            if word in lexicon_titles:
                word_id_title.append(
                    inverted_index_titles[str(lexicon_titles[word])])
        common_titles = set(word_id_title[0]).intersection(*word_id_title)
        for doc_ids in common_titles:
            if doc_title[doc_ids] not in data:
                data[doc_title[doc_ids]] = doc_id[doc_ids]

        temp3_title.remove(temp3_title[len(temp3_title) - 1])
        word_id_title.clear()
    word_id_title.clear()
    temp3_title = temp3.copy()
    temp3_title.remove(temp3_title[0])
    for word in temp3_title:
        if word in lexicon_titles:
            word_id_title.append(
                inverted_index_titles[str(lexicon_titles[word])])
    for doc_id_list in word_id_title:
        for docs in doc_id_list:
            if doc_title[docs] not in data:
                data[doc_title[docs]] = doc_id[docs]

    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
    # word_id_content = []

    while len(temp3_content) > 0:
        for word in temp3_content:
            if word in lexicon:
                word_id_content.append(inverted_index[str(lexicon[word])])

        common_content = set(word_id_content[0]).intersection(*word_id_content)
        for doc_ids in common_content:
            if doc_title[doc_ids] not in data:
                data[doc_title[doc_ids]] = doc_id[doc_ids]

        temp3_content.remove(temp3_content[len(temp3_content) - 1])
        word_id_content.clear()

    # for i in data:
    #     print(str(count), ": ", i)
    #     print(str(count), ": ", data[i])
    #     print()
        # count = count + 1
    for i in data:
        tkinter.Listbox.insert(END, i)
    # end = time.time()
    # print("The time of the program is: ", end - start)
    print(len(data))

    def selected_item():
        for i in tkinter.Listbox.curselection():
            print(tkinter.Listbox.get(i))
            callback(data[tkinter.Listbox.get(i)])
    # go_to_tkinter.Button = tkinter.tkinter.Frame(main, highlightbackground = "yellow", highlightthickness = 2, bd = 0)
    btn = tkinter.Button(main, text='Go to Link', command=selected_item,
                         bg='black', font=("Century Gothic", 10, 'bold'), fg='white')

    def del_em_buttons():
        btn.pack_forget()
        delete_button.pack_forget()
        number_of_articals.pack_forget()

    delete_button = tkinter.Button(main, text='Remove the button', bg='BLACK', fg='WHITE',
                                   command=del_em_buttons)
    delete_button.pack()
    number_of_articals = tkinter.Label(
        main, text="Articals = " + str(len(data)), fg='yellow', bg='black', font=("Century Gothic", 10, 'bold'))
    number_of_articals.pack(side=RIGHT)
    btn.pack()
    # condition = 1


search = tkinter.Button(tkinter.Button_border1, text="Piper Search", bg='black',
                        fg='yellow', font=("Century Gothic", 10, 'bold'), command=Searching)
# Adding the Feeling Lucky tkinter.Button


def feeling_lucky():
    tkinter.Listbox.insert(END, "Ali Ammar")
    tkinter.Listbox.insert(END, "Muhammad Ans")


lucky = tkinter.Button(tkinter.Button_border2, text="I'm feeling lucky",
                       bg='black', fg='yellow', font=("Century Gothic", 10, 'bold'), command=lambda: tkinter.Listbox.insert(END, "Ali Ammar & Muhammad Ans & Hammad Ahmad & Khizran Haider"))

# Showing the result of the quries
scrollbar = Scrollbar(main)

# for values in range(100):
# tkinter.Listbox.insert(END, "My name is Ali Ammar")
# my_text = "<a href = 'https://www.google.com/'>GOOGLE</a>"
# tkinter.Label = HTMLtkinter.Label(html = my_text)
# tkinter.Label = tkinter.Label(text = my_text)
# tkinter.Listbox.insert(END, my_text)
# tkinter.Label.bind("GOOGLE", lambda e: callback('http://www.google.com'))
# tkinter.Listbox.insert(END, tkinter.Label)
# tkinter.Label.pack(side = RIGHT)
# templist = tkinter.Listbox(bg = 'black', fg = 'yellow')
# link1 = tkinter.Label(main, text = "GOOGLE", fg = 'yellow', bg = 'black', cursor = 'hand2')
# templist.insert(END, link1)
# # link1.bind("GOOGLE", lambda e: callback('http://www.google.com'))
# templist.bind("<tkinter.Button-1>", lambda e: callback("http://www.google.com"))
# tkinter.Listbox.insert(END, templist, "<tkinter.Button-1>")
# link1 = tkinter.Label(main, text = "GOOGLE", fg = 'yellow', bg = 'black', cursor = 'hand2')
# tkinter.Listbox.insert(END, link1)
# tkinter.Listbox.bind("<tkinter.Button-1>", lambda e: callback("http://www.google.com"))
# link2 = tkinter.Label(main, text = "FACEBOOK", fg = 'yellow', bg = 'black', cursor = 'hand2')
# tkinter.Listbox.insert(END, link2)
# tkinter.Listbox.bind("<tkinter.Button-2>", lambda e: callback("https://www.facebook.com/"))
# tkinter.Label = HTMLtkinter.Label(html = "<a href = 'https://www.google.com/'>GOOGLE</a>")
# tkinter.Listbox.insert(END, tkinter.Label)

tkinter.Listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=tkinter.Listbox.yview)

# Addding the elements
heading.pack()
search_box.pack()
search.pack()
lucky.pack()
clear_box.pack()
add_content.pack()
# delete_button.pack()
tkinter.Button_border1.pack()
tkinter.Button_border2.pack()
tkinter.Listbox.pack(side=TOP, fill=BOTH)
scrollbar.pack(side=TOP, fill=BOTH)

# The main loop for the GUI(UI)
main.mainloop()


# # GUI SECTION


# class Scrolltkinter.Label(QScrollArea):
#     # constructor
#     def __init__(self, *args, **kwargs):
#         QScrollArea.__init__(self, *args, **kwargs)

#         # making widget resizable
#         self.setWidgetResizable(True)

#         # making qwidget object
#         content = QWidget(self)
#         self.setWidget(content)

#         # vertical box layout
#         lay = QVBoxLayout(content)

#         # creating tkinter.Label
#         self.tkinter.Label = Qtkinter.Label(content)
#         self.tkinter.Label.setOpenExternalLinks(True)
#         self.tkinter.Label.setText(self.tkinter.Label.text() + '\n')
#         # making tkinter.Label multi-line
#         self.tkinter.Label.setWordWrap(True)

#         # adding tkinter.Label to the layout
#         lay.addWidget(self.tkinter.Label)

#     # the setText method
#     def setText(self, text):
#         # setting text to the tkinter.Label
#         self.tkinter.Label.setText(text + "\n")

#     # getting text method
#     def text(self):
#         # getting text of the tkinter.Label
#         get_text = self.tkinter.Label.text()

#         # return the text
#         return get_text

#     # setToolTip method
#     def setToolTip(self, p_str):
#         # setting tool tip to the tkinter.Label
#         self.tkinter.Label.setToolTip(p_str)

#     # setToolTipDuration method
#     def setToolTipDuration(self, p_int):
#         # setting tool tip duration to the tkinter.Label
#         self.tkinter.Label.setToolTipDuration(p_int)


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Piper")
#         self.setGeometry(0, 25, 1100, 700)
#         self.Components()
#         self.show()
#         self.showMaximized()

#     def Components(self):
#         # The heading specifications.
#         self.heading = Qtkinter.Label("Piper 7", self)
#         self.heading.setGeometry(520, 80, 700, 200)
#         self.heading.setOpenExternalLinks(True)
#         self.heading.setStyleSheet(style)
#         # The search bar specifications.
#         self.textbox = QLineEdit(self)
#         self.textbox.setGeometry(395, 250, 575, 40)
#         self.textbox.setAlignment(QtCore.Qt.AlignCenter)
#         # The is the search tkinter.Button specifications.
#         self.search = QPushtkinter.Button("Piper Search", self)
#         self.search.setGeometry(485, 305, 200, 45)
#         self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.search.clicked.connect(self.searching)
#         # This is the feeling lucky specifications.
#         self.feeling_lucky = QPushtkinter.Button("I'm Feeling Lucky", self)
#         self.feeling_lucky.setGeometry(685, 305, 200, 45)
#         self.feeling_lucky.setCursor(
#             QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         # Setting the display area for the queries
#         # self.display_area = QListWidget(self)
#         # self.display_area = QListWidget(self)
#         # self.display_area.setGeometry(50, 500, 100, 100)
#         # setting the tkinter.Labels
#         # self.tkinter.Label = Qtkinter.Label(self)
#         # self.tkinter.Label.setOpenExternalLinks(True)
#         # self.tkinter.Label.setGeometry(100, 600, 100, 100)
#         # self.tkinter.Label.setText("<a href=\"https://www.google.com\">QtCentre</a>")
#         # self.tkinter.Label.setStyleSheet(style_queries)
#         # self.display_area.addItem(self.tkinter.Label)
#         # print(str(self.tkinter.Label.selectedText()))
#         # SETTING THE QURIES
#         self.tkinter.Label = Scrolltkinter.Label(self)
#         # tkinter.Label.setText("<a href=\"https://www.google.com\">GOOGLE</a>")
#         # tkinter.Label.setText(linktemplate.format('https://www.facebook.com', 'FACEBOOK'))
#         # i = 1000
#         # while i > 0:
#         #     tkinter.Label.setText(tkinter.Label.text() + "\n" + linktemplate.format('https://www.facebook.com', 'FACEBOOK'))
#         #     i = i - 1
#         # tkinter.Label.setText("<a href=\"https://www.google.com\">GOOGLE</a>\n<a href=\"https://www.youtube.com/\">YOUTUBE</a>")
#         linktemplate = '<a href=\"{0}\">{1}</a>'
#         self.tkinter.Label.setGeometry(0, 360, 1365, 340)
#         self.tkinter.Label.setStyleSheet(style_q)
#         self.tkinter.Label.setToolTipDuration(1000)
#         # self.temp = Qtkinter.Label(self)
#         # self.temp.setText("Oyyeah")
#         # self.temp.setText(self.temp.text() + "\n" + "FUCK YEAH")
#         # tempString = linktemplate.format('https://www.google.com/', 'This is the bests')
#         # self.temp.setText(linktemplate.format('https://www.google.com/', 'This is the best.'))
#         # self.temp.setText(self.temp.text() + "\n" + tempString)
#         # self.temp.setGeometry(0, 0, 200, 200)
#         # self.temp.setStyleSheet(style_q)
#         # tkinter.Label.setText("")
#         # tkinter.Label.setOpenExternalLinks(True)
#         # self.temp = Qtkinter.Label(self)
#         # self.temp.setText('<a href=\"https://www.google.com/\">Google</a>' + "\nOO YEAH")
#         # self.temp.setText(self.temp.text() + "\nMy name is sheila.\n")
#         # self.temp.setStyleSheet(style_q)
#         # self.temp.setGeometry(0, 0, 900, 200)

#     def searching(self):
#         count = 0
#         linktemplate = '<a href=\"{0}\">{1}</a>'
#         self.tkinter.Label.setText("")
#         data = {}
#         count = 0
#         word_id_title = []
#         common_titles = []
#         common_content = []

#         temp2 = []
#         temp3 = []
#         temp1 = self.textbox.text()
#         # temp1 = "The Last White Helmet of Idlib"
#         temp1 = nltk.word_tokenize(temp1)
#         for i in range(len(temp1)):
#             temp1[i] = snow_stemmer.stem(temp1[i])
#         for i in temp1:
#             if i not in stop_words:
#                 temp2.append(i)
#         for i in temp2:
#             if (i.isalnum()):
#                 temp3.append(i)
#         temp3 = list(dict.fromkeys(temp3))
#         print(temp3)
#         temp3_title = temp3.copy()
#         temp3_content = temp3.copy()


#         # Checking the data in title::::::::::::::::::::::::::::::::::::::::::::::::
#         while len(temp3_title) > 0:
#             for word in temp3_title:
#                 if word in lexicon_titles:
#                     word_id_title.append(
#                         inverted_index_titles[str(lexicon_titles[word])])
#             if(len(word_id_title) > 0):
#                 common_titles = set(word_id_title[0]).intersection(*word_id_title)
#             for doc_ids in common_titles:
#                 if doc_title[doc_ids] not in data:
#                     data[doc_title[doc_ids]] = doc_id[doc_ids]

#             temp3_title.remove(temp3_title[len(temp3_title) - 1])
#             word_id_title.clear()
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         # cSearching in the content::::::::::::::::::::::::::::::::::::::::::::::::::
#         word_id_content = []

#         while len(temp3_content) > 0:
#             for word in temp3_content:
#                 if word in lexicon:
#                     word_id_content.append(inverted_index[str(lexicon[word])])

#             common_content = set(word_id_content[0]).intersection(*word_id_content)
#             for doc_ids in common_content:
#                 if doc_title[doc_ids] not in data:
#                     data[doc_title[doc_ids]] = doc_id[doc_ids]

#             temp3_content.remove(temp3_content[len(temp3_content) - 1])
#             word_id_content.clear()

#         # for i in data:
#         #     # print(str(count), ": ", i)
#         #     print(str(count), ": ", data[i])
#         #     print()
#         #     count = count + 1
#         count_print = 0
#         for i in data:
#             self.tkinter.Label.setText("\n" + self.tkinter.Label.text() + linktemplate.format(data[i], str(count_print) + ":::::-" + i + "-::::::::::::\n"))
#             # whole_data.append(str(linktemplate.format(data[i], str(count_print) + ": " + i)))
#             count_print += 1

# style_q = """
#     Qtkinter.Label{
#         font-family: arial;
#         font-size: 30px;
#         background-color: black;
#         border-color: 10px solid red;
#     }
# """
# style = """
#     QMainWindow{
#         background: #333333;
#     }
#     Qtkinter.Label{
#         font-size: 120px;
#         font-family: MoonLight;
#         color: YELLOW;
#         background-color: #333333;
#     }
#     QLineEdit{
#         font-size: 20px;
#         font-family: arial;
#         color: YELLOW;
#         background-color: #333333;
#         border: 2px solid yellow;
#         border-radius: 12px;
#     }
#     QPushtkinter.Button{
#         font-size: 27px;
#         font-family: MoonLight;
#         background-color: #333333;
#         border: 2px solid yellow;
#         color: yellow;
#         border-radius: 5px;
#     }
#     QPushtkinter.Button:hover{
#         color: BLACK;
#         background-color: YELLOW;
#     }
#     QPushtkinter.Button::pressed{
#         color: cyan;
#         background-color: black;
#         border: 2px solid black;
#     }
# """
# App = QApplication(sys.argv)
# App.setStyleSheet(style)
# QtGui.QFontDatabase.addApplicationFont(
#     'Fonts\shocked-up\Shocked Up Free Trial.ttf')
# QtGui.QFontDatabase.addApplicationFont('Fonts\start-game\Start Game.otf')
# QtGui.QFontDatabase.addApplicationFont(
#     'Fonts\moonlight-5\Moonlight-Regular.ttf')
# QtGui.QFontDatabase.addApplicationFont('Fonts\corpus-gaii\CorpusGaii.ttf')
# QtGui.QFontDatabase.addApplicationFont('Fonts\Grind Halftone.otf')
# window = Window()
# sys.exit(App.exec())
