import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
import tkinter
from tkinter import *

gui = tkinter.Tk()
gui.geometry("510x350")
gui.title("Word Sense Disambiguation")

seq_label_1 = Label(gui, text = "  Sentence 1:  ").grid(row = 0, column = 0)
s1 = Entry(gui, width = 70)
s1.grid(row = 0, column = 1)
def_1 = Text(gui, height = 7, width = 60)
def_1.grid(row = 4, column = 0, columnspan = 3)

seq_label_2 = Label(gui, text = "  Sentence 2:  ").grid(row = 1, column = 0)
s2 = Entry(gui, width = 70)
s2.grid(row = 1, column = 1)
def_2 = Text(gui, height = 7, width = 60)
def_2.grid(row = 5, column = 0, columnspan = 3)

key_label = Label(gui, text = "  Keyword:  ").grid(row = 2, column = 0)
keyword = Entry(gui, width = 70)
keyword.grid(row = 2, column = 1)

def word_context_definition(seq, key_word):
    
    # Tokenization of the sequence
    temp = word_tokenize(seq)
      
    # Retrieving the definition of the tokens
    temp = lesk(temp, key_word)         #using inbuilt lesk module
    return temp.definition()            #returns a string with definition

def submit():
    
    kw = keyword.get()                  
    sen1 = s1.get()
    sen2 = s2.get()

    def1 = word_context_definition(sen1, kw)       #call function to find definition based on the context of the sentences
    def2 = word_context_definition(sen2, kw)
    
    def_1.delete("1.0", END)
    def_2.delete("1.0", END)
    
    def_1.insert("1.0", "Definition of " + kw + " in sentence 1   :\n" + def1)
    def_2.insert("1.0", "Definition of " + kw + " in sentence 2:\n" + def2)


submit = Button(gui, text = "SUBMIT", width = 20, command = submit).grid(row = 3, column = 0, columnspan = 3)

gui.mainloop()






