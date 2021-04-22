#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('Mad-libs')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'helvetica 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'freehand 15 bold').place(x=80, y=80)


################Stories##############


def madlib1():
    r1=Tk()
    r1.geometry('1080x1080')
    r1.title('The Photographer')

    animals_=StringVar()
    profession_=StringVar()
    cloth_=StringVar()
    verb_=StringVar()
    food_=StringVar()
    thing_=StringVar()
    name_=StringVar()
    place_=StringVar()

    def submit():
        animals=animals_.get()
        profession=profession_.get()
        cloth=cloth_.get()
        verb=verb_.get()
        food=food_.get()
        things=thing_.get()
        name=name_.get()
        place=place_.get()
        print(name)
        out=Label(r1,text= 'Say' + food + ', the photographer said as the camera flashed! \n' + name + ' and I had gone to ' + place +' to get our photos taken today.\nThe first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '.\nWhen we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + 'exactly what I had in mind',font=('calibre',10, 'italic'))
        out.grid(row=9,column=1)
        name_.set("")
    anim_label = Label(r1, text = 'Animal Name', font=('calibre',10, 'bold'))
    anim_entry = Entry(r1,textvariable =animals_, font=('calibre',10,'normal'))

    prof_label = Label(r1, text = 'Profession', font=('calibre',10, 'bold'))
    prof_entry = Entry(r1,textvariable =profession_, font=('calibre',10,'normal'))

    cloth_label = Label(r1, text = 'Cloth name', font=('calibre',10, 'bold'))
    cloth_entry = Entry(r1,textvariable =cloth_, font=('calibre',10,'normal'))

    verb_label = Label(r1, text = 'Verb in ing form', font=('calibre',10, 'bold'))
    verb_entry = Entry(r1,textvariable =verb_, font=('calibre',10,'normal'))

    food_label = Label(r1, text = 'Food Name', font=('calibre',10, 'bold'))
    food_entry = Entry(r1,textvariable =food_, font=('calibre',10,'normal'))

    thing_label = Label(r1, text = 'Thing Name', font=('calibre',10, 'bold'))
    thing_entry = Entry(r1,textvariable =thing_, font=('calibre',10,'normal'))

    name_label = Label(r1, text = 'Any  Name', font=('calibre',10, 'bold'))
    name_entry = Entry(r1,textvariable =name_, font=('calibre',10,'normal'))

    place_label = Label(r1, text = 'Place Name', font=('calibre',10, 'bold'))
    place_entry = Entry(r1,textvariable =place_, font=('calibre',10,'normal'))

    sub_btn=Button(r1,text = 'Submit', command = submit)

    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=2)

    place_label.grid(row=1,column=0)
    place_entry.grid(row=1,column=2)

    thing_label.grid(row=2,column=0)
    thing_entry.grid(row=2,column=2)

    anim_label.grid(row=3,column=0)
    anim_entry.grid(row=3,column=2)

    prof_label.grid(row=4,column=0)
    prof_entry.grid(row=4,column=2)

    cloth_label.grid(row=5,column=0)
    cloth_entry.grid(row=5,column=2)

    food_label.grid(row=6,column=0)
    food_entry.grid(row=6,column=2)

    verb_label.grid(row=7,column=0)
    verb_entry.grid(row=7,column=2)

    sub_btn.grid(row=8,column=2)
    #r1.mainloop()

def madlib2():

    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')



def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')


    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')



######buttons
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()
