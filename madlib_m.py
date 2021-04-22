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
    r1.geometry('1080x720')
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
        animals=animals_entry.get()
        profession=profession_entry.get()
        cloth=cloth_entry.get()
        verb=verb_entry.get()
        food=food_entry.get()
        things=thing_entry.get()
        name=name_entry.get()
        place=place_entry.get()
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
    
    r1 = Tk()
    r1.geometry("1080x720")
    r1.title("The Butterfly")

    color_ = StringVar()
    thing_ = StringVar()
    place_ = StringVar()
    person_ = StringVar()
    adjective_ = StringVar()
    insect_ = StringVar()
    food_ = StringVar()
    verb_ = StringVar()
    adjective1_ = StringVar()

    def submit():
        color = color_entry.get()
        thing = thing_entry.get()
        place = place_entry.get()
        person = person_entry.get()
        adjective = adjective_entry.get()
        insect = insect_entry.get()
        food = food_entry.get()
        verb = verb_entry.get()
        adjective1 = adjective1_entry.get()

        out = Label(r1, text = 'Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splotches that looked like '+thing+ ' .\nI flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjective1+ ' ' +insect +' .\nWe ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.', font=('calibre',10, 'italic'))
        out.grid(row = 9, column = 1)

    adjective_label = Label(r1, text = 'Adjective', font = ('calibre',10, 'bold'))
    adjective_entry = Entry(r1, textvariable = adjective_, font = ('calibre',10,'normal'))

    color_label = Label(r1, text = 'Color Name', font = ('calibre',10, 'bold'))
    color_entry = Entry(r1, textvariable = color_, font = ('calibre',10,'normal'))

    thing_label = Label(r1, text = 'Thing Name', font = ('calibre',10, 'bold'))
    thing_entry = Entry(r1, textvariable = thing_, font = ('calibre',10,'normal'))

    place_label = Label(r1, text = 'Place Name', font = ('calibre',10, 'bold'))
    place_entry = Entry(r1, textvariable = place_, font = ('calibre',10,'normal'))

    person_label = Label(r1, text = 'Person Name', font = ('calibre',10, 'bold'))
    person_entry = Entry(r1, textvariable = person_, font = ('calibre',10,'normal'))

    adjective1_label = Label(r1, text = 'Adjective', font = ('calibre',10, 'bold'))
    adjective1_entry = Entry(r1, textvariable = adjective1_, font = ('calibre',10,'normal'))

    insect_label = Label(r1, text = 'Insect Name', font = ('calibre',10, 'bold'))
    insect_entry = Entry(r1, textvariable = insect_, font = ('calibre',10,'normal'))

    food_label = Label(r1, text = 'Food Name', font = ('calibre',10, 'bold'))
    food_entry = Entry(r1, textvariable = food_, font = ('calibre',10,'normal'))

    verb_label = Label(r1, text = 'Verb', font = ('calibre',10, 'bold'))
    verb_entry = Entry(r1, textvariable = verb_, font = ('calibre',10,'normal'))

    sub_btn = Button(r1, text = 'Submit', command = submit)

    adjective_label.grid(row = 0, column = 0)
    adjective_entry.grid(row = 0, column = 2)

    color_label.grid(row = 1, column = 0)
    color_entry.grid(row = 1, column = 2)

    thing_label.grid(row = 2, column = 0)
    thing_entry.grid(row = 2, column = 2)

    place_label.grid(row = 3, column = 0)
    place_entry.grid(row = 3, column = 2)

    person_label.grid(row = 4, column = 0)
    person_entry.grid(row = 4, column = 2)

    adjective1_label.grid(row = 5, column = 0)
    adjective1_entry.grid(row = 5, column = 2)

    insect_label.grid(row = 6, column = 0)
    insect_entry.grid(row = 6, column = 2)

    food_label.grid(row = 7, column = 0)
    food_entry.grid(row = 7, column = 2)

    verb_label.grid(row = 8, column = 0)
    verb_entry.grid(row = 8, column = 2)

    sub_btn.grid(row = 9, column = 2)


def madlib3():

    r1=Tk()
    r1.geometry('1080x720')
    r1.title('Apple and Apple')

    thing_=StringVar()
    food_=StringVar()
    adverb_=StringVar()
    verb_=StringVar()
    place_=StringVar()
    adjective_=StringVar()
    color_=StringVar()
    person_=StringVar()


    def submit():
        adverb=adverb_entry.get()
        adjective=adjective_entry.get()
        color=color_entry.get()
        verb=verb_entry.get()
        food=food_entry.get()
        thing=thing_entry.get()
        person=person_entry.get()
        place=place_entry.get()
        out=Label(r1,text='Today we picked apple from '+person+ "'s Orchard.\nI had no idea there were so many different varieties of apples.\nI ate " +color+ ' apples straight off the tree that tested like '+food+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.\nWhen our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '.\nI can hardly wait to get home and cook with the apples. We are going to make apple '+food+ ' and '+thing+' pies!.',font=('calibre',10, 'italic'))
        out.grid(row=8,column=1)

    verb_label = Label(r1, text = 'Verb in ing form', font=('calibre',10, 'bold'))
    verb_entry = Entry(r1,textvariable =verb_, font=('calibre',10,'normal'))

    food_label = Label(r1, text = 'Food Name', font=('calibre',10, 'bold'))
    food_entry = Entry(r1,textvariable =food_, font=('calibre',10,'normal'))

    adverb_label = Label(r1, text = 'Adverb', font=('calibre',10, 'bold'))
    adverb_entry = Entry(r1,textvariable =adverb_, font=('calibre',10,'normal'))

    thing_label = Label(r1, text = 'Thing', font=('calibre',10, 'bold'))
    thing_entry = Entry(r1,textvariable =thing_, font=('calibre',10,'normal'))

    place_label = Label(r1, text = 'Place', font=('calibre',10, 'bold'))
    place_entry = Entry(r1,textvariable =place_, font=('calibre',10,'normal'))

    adjective_label = Label(r1, text = 'Adjective', font=('calibre',10, 'bold'))
    adjective_entry = Entry(r1,textvariable =adjective_, font=('calibre',10,'normal'))

    color_label = Label(r1, text = 'Color', font=('calibre',10, 'bold'))
    color_entry = Entry(r1,textvariable =color_, font=('calibre',10,'normal'))

    person_label = Label(r1, text = 'Person', font=('calibre',10, 'bold'))
    person_entry = Entry(r1,textvariable =person_, font=('calibre',10,'normal'))

    sub_btn=Button(r1,text = 'Submit', command = submit)

    adverb_label.grid(row=0,column=0)
    adverb_entry.grid(row=0,column=2)

    place_label.grid(row=1,column=0)
    place_entry.grid(row=1,column=2)

    thing_label.grid(row=2,column=0)
    thing_entry.grid(row=2,column=2)

    adjective_label.grid(row=3,column=0)
    adjective_entry.grid(row=3,column=2)

    color_label.grid(row=4,column=0)
    color_entry.grid(row=4,column=2)

    person_label.grid(row=5,column=0)
    person_entry.grid(row=5,column=2)

    food_label.grid(row=6,column=0)
    food_entry.grid(row=6,column=2)

    verb_label.grid(row=7,column=0)
    verb_entry.grid(row=7,column=2)

    sub_btn.grid(row=8,column=2)





######buttons
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()
