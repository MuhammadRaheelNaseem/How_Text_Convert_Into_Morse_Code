# Muhammad Raheel Naseem
# Morse Code Encoder & Decoder App

from tkinter import *
import datetime

gui=Tk()
gui.title('Python')
gui.geometry('680x550')
gui.attributes('-fullscreen',True)
gui.configure(bg="black")

#__________define datetime in 'x' variable for save text file
x=datetime.datetime.now()

# __________Define Morse Codes___________
morse_code={
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..--','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..',
    # Using Numeric value 
    '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
    '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
    # Symbol as like . , / "" @ ( ) - $ -
    '.':'.-.-.-',',':'--..--','?':'..--..',':':'---...',';':'-.-.-.','-':'-....-','/':'-..-.',
    '""':'.-..-.','(':'-.-- .',')':'-.--.-','=':'-...-','@':'.--.-.','&':'.-...','+':'.-.-.',
    '!':'-.-.--','$':'...-..',"'":'.----.'
}
# Creating speacial loop for reverse morse code
morse_code_reverse={key:value for value,key in morse_code.items()}
reverse_code=morse_code_reverse

# ___________Creating functionality for perfoming tasks__________________
# 1.) Encoding function
def morse_code_checking(encode):
    global x
    storing_morseCode=''
    for i in encode.upper():
        storing_morseCode+=morse_code.get(i,'//')+' '
    output_text.insert(0.0,storing_morseCode)
    with open('save_morseCode.txt','a') as file:
        a=(x.strftime('%a %D %I:%M %p \t\t Input ==>:'))+encode+'Output:==>'+storing_morseCode+'\n'
        file.writelines(a)
# 2.) Decoding function
def decoding(decode):
    global x
    storing_morseCode=''
    for i in decode.split():
        storing_morseCode+=reverse_code.get(i,' ')+''
    output_text.insert(0.0,storing_morseCode.capitalize())
    with open('save_morseCode.txt','a') as file:
        a=(x.strftime('%a %D %I:%M %p \t\t Input ==>:'))+decode+'Output:==>'+storing_morseCode+'\n'
        file.writelines(a)

# 3.) Clear function
def clear():
    encoding_txt.delete('1.0',END)
    decoding_txt.delete('1.0',END)
    output_text.delete('1.0',END)
# ____________________Button for exit____________________________
exit_button=Button(gui,
                   text=X,
                   command=gui.destroy,
                   font=('Times 16'),
                   bg='red',fg='white',
                   activebackground='red',
                   activeforeground='white',
                   relief=FLAT)
exit_button.place(x=1325,
                  y=0,
                  width=43)
label='wellcome to morse code encoding & decoding application'.title()
heading_label=Label(gui,
                    text=label,
                    font=('Times 35 bold'),bg='black',foreground='white')
heading_label.place(x=100,
                    y=50)

# making frame for all function parts
# ____________________Frame 1 for Encoding_____________________________
encoding_frame=Frame(gui,bg='black')
encoding_frame.place(x=10,
                     y=125,
                     height=380,
                     width=500)
# Making label for showing heading
encoding_label=Label(encoding_frame,
                     text='ENCODING :',
                     font=('Arial 18 bold'),
                     bg='black',foreground='white')
encoding_label.place(x=6,y=16)
# scroll bar for scrolling
encoding_scroll=Scrollbar(encoding_frame)
encoding_scroll.place(x=480,
                      y=51,
                      height=299)
# Making text box for getting values
encoding_txt=Text(encoding_frame,
                  yscrollcommand=encoding_scroll.set,
                  bg='#82E0AA',
                  font=('Arial 18 bold'),
                  bd=15)
encoding_txt.place(x=6,
                   y=50,
                   width=475,
                   height=300)
# This line represent scrollbar
encoding_scroll.configure(command=encoding_txt.yview)

# _________________________Frame 2 for Decoding___________________________
decoding_frame=Frame(gui,
                     bg='black')
decoding_frame.place(x=860,
                     y=125,
                     height=380,
                     width=500)
# Making label for showing heading
decoding_label=Label(decoding_frame,
                     text='DECODING:',
                     font=('Arial 18 bold'),
                     bg='black',foreground='white')
decoding_label.place(x=6,
                     y=16)
# scroll bar for scrolling
decoding_scroll=Scrollbar(decoding_frame)
decoding_scroll.place(x=480,
                      y=51,
                      height=299)
# Making text box for getting values
decoding_txt=Text(decoding_frame,
                  yscrollcommand=decoding_scroll.set,
                  bg='#82E0AA',
                  font=('Arial 18 bold'),
                  bd=15)
decoding_txt.place(x=6,
                   y=50,
                   height=300,
                   width=475)
# This line represent scrollbar
decoding_scroll.configure(command=decoding_txt.yview)
# _________________________Frame 3 for Buttons_________________________
button_frame=Frame(gui,
                   bg='black')
button_frame.place(x=512,
                   y=125,
                   height=380,
                   width=343)
encoding_btn=Button(button_frame,
                    text='Convert Encoding',
                    font=('Times 25 italic'),
                    bg='#5DADE2',
                    relief=FLAT,
                    activebackground='#5DADE2',
                    command=lambda: morse_code_checking(encoding_txt.get('1.0',END)))
encoding_btn.place(x=35,
                   y=90)
decoding_btn=Button(button_frame,
                    text='Convert Decoding',
                    font=('Times 25 italic'),
                    bg='#5DADE2',
                    relief=FLAT,
                    activebackground='#5DADE2',
                    command=lambda: decoding(decoding_txt.get('1.0',END)))
decoding_btn.place(x=35,
                   y=180)
encoding_btn=Button(button_frame,
                    text='Clear All',
                    font=('Times 25 italic'),
                    relief=FLAT,
                    activebackground='#F1948A',
                    bg='#F1948A',
                    command=clear)
encoding_btn.place(x=35,
                   y=270,
                  width='275'
                  )
#btn_ent=Entry(button_frame)
#btn_ent.place(x=955,y=17,height=30)

# ________________________Frame 4 for showing Output_______________________________
output_frame=Frame(gui,
                   bg='black')
output_frame.place(x=10,
                   y=480,
                   width=1350,
                   height=270)
output_label=Label(output_frame,
                   text='Output :',
                   font=('Arial 25 underline bold'),
                   bg='black',
                  foreground='white')
output_label.place(x=10,
                   y=15)
output_scroll=Scrollbar(output_frame)
output_scroll.place(x=1310,
                    y=60,
                    height=200)
output_text=Text(output_frame,
                 yscrollcommand=output_scroll.set,
                 bg='#82E0AA',
                 font=('arial 19'),
                bd='15')
output_text.place(x=10,
                  y=60,
                  height=200,
                  width=1300)
output_scroll.configure(command=output_text.yview)
gui.mainloop()