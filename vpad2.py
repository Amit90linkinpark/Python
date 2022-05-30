import os
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog,messagebox
main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title("Amit text editor")
main_application.wm_iconbitmap('icon.ico')
############################### main menu  ################################

main_menu=tk.Menu()
###File####
###image#####
new_image=tk.PhotoImage(file="icons2/new.png")
open_image=tk.PhotoImage(file="icons2/open.png")
save_image=tk.PhotoImage(file="icons2/save.png")
save_as_image=tk.PhotoImage(file="icons2/save_as.png")
exit_image=tk.PhotoImage(file="icons2/exit.png")


File=tk.Menu(main_menu, tearoff=False)

###edit####
#####image######
copy_image=tk.PhotoImage(file="icons2/copy.png")
paste_image=tk.PhotoImage(file="icons2/paste.png")
cut_image=tk.PhotoImage(file="icons2/cut.png")
clear_all_image=tk.PhotoImage(file="icons2/clear_all.png")
find_image=tk.PhotoImage(file="icons2/find.png")


Edit=tk.Menu(main_menu, tearoff=False)

########view#######
######image######
tool_bar_image=tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_image=tk.PhotoImage(file="icons2/status_bar.png")

View=tk.Menu(main_menu, tearoff=False)

#######Color_them#####
#####image#######
dark_color_image=tk.PhotoImage(file="icons2/dark.png")
light_default_color_image=tk.PhotoImage(file="icons2/light_default.png")
light_plus_color_image=tk.PhotoImage(file="icons2/light_plus.png")
monokai_color_image=tk.PhotoImage(file="icons2/monokai.png")
night_blue_color_image=tk.PhotoImage(file="icons2/night_blue.png")
red_color_image=tk.PhotoImage(file="icons2/red.png")

Color_theme=tk.Menu(main_menu, tearoff=False)
######Color_theme Commond########
 
theme_choice = tk.StringVar()
color_image = (light_default_color_image,dark_color_image, light_plus_color_image, monokai_color_image, night_blue_color_image, red_color_image)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}



# cascade
main_menu.add_cascade(label="File",menu=File)
main_menu.add_cascade(label="Edit",menu=Edit)
main_menu.add_cascade(label="View",menu=View)
main_menu.add_cascade(label="Color_theme",menu=Color_theme)
#------------------------------- main menu end -----------------------------



############################### Toolbar  ################################

tool_bar=tk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)
#######font box#######
font_tool=tk.font.families()
font_famili=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_famili,state="readonly")
font_box['values']=font_tool
font_box.current(font_tool.index("Arial"))
font_box.grid(row=0,column=0, padx=5)

########Size Box#######
size_tool=tuple(range(8,81))
size_famili=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=14,textvariable=size_famili,state="readonly")
size_box['values']=size_tool
size_box.current(4)
size_box.grid(row=0,column=1,padx=5)
#######Button#######
#####BOLD Button####
bold_image=tk.PhotoImage(file="icons2/bold.png")
bold_button=ttk.Button(tool_bar,image=bold_image)
bold_button.grid(row=0,column=3,padx=5)
#######italic Button#####
italic_image=tk.PhotoImage(file="icons2/italic.png")
italic_button=ttk.Button(tool_bar,image=italic_image)
italic_button.grid(row=0,column=4,padx=5)
#######underline Button #####
underline_image=tk.PhotoImage(file="icons2/underline.png")
underline_button=ttk.Button(tool_bar,image=underline_image)
underline_button.grid(row=0,column=5,padx=5)

######font_color Button######
font_color_image=tk.PhotoImage(file="icons2/font_color.png")
font_color_button=ttk.Button(tool_bar,image=font_color_image)
font_color_button.grid(row=0,column=6,padx=5)
######align_left Button ####
align_left_image=tk.PhotoImage(file="icons2/align_left.png")
align_left_button=ttk.Button(tool_bar,image=align_left_image)
align_left_button.grid(row=0,column=7,padx=5)
#######align_center Button######
align_center_image=tk.PhotoImage(file="icons2/align_center.png")
align_center_button=ttk.Button(tool_bar,image=align_center_image)
align_center_button.grid(row=0,column=8,padx=5)
######align_right Button #####
align_right_image=tk.PhotoImage(file="icons2/align_right.png")
align_right_button=ttk.Button(tool_bar,image=align_right_image)
align_right_button.grid(row=0,column=9,padx=5)
#------------------------------- Toolbar end -----------------------------



############################### Text editor  ################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
#font family and font size function###
curren_font_family="Arial"
curren_font_size=12
def change_font(main_application):
    global curren_font_family
    curren_font_family=font_famili.get()
    text_editor.configure(font=(curren_font_family,curren_font_size))
def change_font_size(main_application):
    global curren_font_size
    curren_font_size=size_famili.get()
    text_editor.configure(font=(curren_font_family,curren_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
size_box.bind("<<ComboboxSelected>>",change_font_size)
######Bold Button Function######
def change_bold():
    text_change=tk.font.Font(font=text_editor["font"])
    if text_change.actual()['weight']=='normal':
        text_editor.configure(font=(curren_font_family,curren_font_size, 'bold'))
    if text_change.actual()['weight']=='bold':
        text_editor.configure(font=(curren_font_family,curren_font_size, 'normal'))

bold_button.configure(command=change_bold)
##########Italic Button Function####
def change_style():
    text_style_change=tk.font.Font(font=text_editor["font"])
    if text_style_change.actual()['slant']=='roman':
        text_editor.configure(font=(curren_font_family,curren_font_size,"italic"))
    if text_style_change.actual()['slant']=="italic":
        text_editor.configure(font=(curren_font_family,curren_font_size,'roman'))
italic_button.configure(command=change_style)

######## Underline Button ######
def change_underline():
    underline_style=tk.font.Font(font=text_editor['font'])
    if underline_style.actual()["underline"]==0:
        text_editor.configure(font=(curren_font_family,curren_font_size,'underline'))
    if underline_style.actual()["underline"]==1:
        text_editor.configure(font=(curren_font_family,curren_font_size,'normal'))

underline_button.configure(command=change_underline)
text_editor.configure(font=("Arial",12))
######### font color button function #####
def change_font_color():
    font_color_change=tk.colorchooser.askcolor()
    text_editor.configure(fg=font_color_change[1])
font_color_button.configure(command=change_font_color)   

###############align left button function ######
def left_align_text():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=left_align_text)
#############align center button function######
def center_align_text():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")  
align_center_button.configure(command=center_align_text)  

########align Right Button Function #############
def right_align_text():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_button.configure(command=right_align_text)





#------------------------------- Text editor end -----------------------------


###############################  status bar  ################################
status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
#######Status Bar Function########
text_change=False
def status_bar_change(even=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0,'end-1c').split())
        cherator=len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f"Characters{cherator}, Words{word}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", status_bar_change)



#-------------------------------  status bar end -----------------------------


############################### main menu function  ################################
####file Commond ####
#######New button Function #####
url=''
def new_file(even=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

File.add_command(label="New",image=new_image, compound=tk.LEFT, accelerator='ctrl+n', command=new_file)
######### Open Button Function #######
def open_file(even=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Amit Select File", filetypes=(("text File,'*.txt"),("All File","*.*")))
    try:
        with open(url,"r") as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))    
File.add_command(label="Open",image=open_image, compound=tk.LEFT, accelerator='ctrl+o', command=open_file)
########## save Button Function ########
def save_file(even=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,"w", encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(("text File,'*.txt"),("All File","*.*")))
            counten2=text_editor.get(1.0,tk.END)
            url.write(counten2)
            url.close()
    except:
        return

File.add_command(label="Save",image=save_image, compound=tk.LEFT, accelerator='ctrl+s',command=save_file)
##########Save as button function##########
def save_as_file(even=None):
    global url
    try:
        countent=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(("text File,'*.txt"),("All File","*.*")))
        url.write(countent)
        url.close()
    except:
        return
File.add_command(label="Save_as",image=save_as_image, compound=tk.LEFT, accelerator='ctrl+alt+n', command=save_as_file)
########### Exit Button Function #######
def exit_file(even=None):
    global url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save this file")
            if mbox is True:
                if url:
                    countent=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding=='utf-8') as nw:
                        nw.write(countent)
                        main_application.destroy()
                else:
                    countent2=text_editor.get(1.0,tk.END)
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(("text File,'*.txt"),("All File","*.*")))        
                    url.write(countent2)
                    url.close()
                    main_application.destroy()
            if mbox is False:
                main_application.destroy()     
        else:
            main_application.destroy()      
    except:
        return 


File.add_command(label="Exit",image=exit_image, compound=tk.LEFT, accelerator='ctrl+q', command=exit_file)

####Edit Commond####

Edit.add_command(label="Copy", image=copy_image,compound=tk.LEFT,accelerator='ctrl+c', command=lambda:text_editor.event_generate("<Control c>"))
Edit.add_command(label="Paste", image=paste_image,compound=tk.LEFT,accelerator='ctrl+p',command=lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label="Cut", image=cut_image,compound=tk.LEFT,accelerator='ctrl+x',command=lambda:text_editor.event_generate("<Control x>"))

Edit.add_command(label="Clear_all", image=clear_all_image,compound=tk.LEFT,accelerator='ctrl+alt+c', command=lambda:text_editor.delete(1.0,tk.END))

####Find Button Function#####
def find_file(even=None):
    ######FInd Function####
    def find():
        word = find_entry_file.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    #####Replace Function 
    def replace_file():
        word=find_entry_file.get()
        replace_text=replace_entry_file.get()
        counten=text_editor.get(1.0, tk.END)
        new_content=counten.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
        
    
    
    
    find_fream=tk.Toplevel()
    find_fream.geometry('450x250+500+200')
    find_fream.title("Find")
    find_fream.resizable(0,0)
    ##### Frem #####
    find_dilog = ttk.Labelframe(find_fream,text="Find/Replace")
    find_dilog.pack(pady=20)
    ####Laber######
    find_label_file=ttk.Label(find_dilog,text="Find")
    replace_label_file=ttk.Label(find_dilog,text="Replace")
    ####Entery Box ### 
    find_entry_file=ttk.Entry(find_dilog,width=20)
    replace_entry_file=ttk.Entry(find_dilog,width=20)
    ##### Button FIND and REPLACE#####
    find_button_label=ttk.Button(find_dilog,text="Find", command=find)
    replace_button_label=ttk.Button(find_dilog,text="Replace", command=replace_file)
    ###### label grid ####
    find_label_file.grid(row=0,column=0, pady=5)
    replace_label_file.grid(row=1,column=0,pady=5)
    ######## Entry box label####
    find_entry_file.grid(row=0, column=1, pady=5)
    replace_entry_file.grid(row=1, column=1, pady=5)
    ######## FIND and REPLACE Button grid#####
    find_button_label.grid(row=2,column=0, padx=10, pady=5)
    replace_button_label.grid(row=2,column=1,padx=10, pady=5)

    find_fream.mainloop()

    

Edit.add_command(label="Find", image=find_image,compound=tk.LEFT,accelerator='ctrl+f', command=find_file)
######View Commond####
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
View.add_checkbutton(label="Tool_bar", image=tool_bar_image,onvalue=True,offvalue=0,variable=show_toolbar,compound=tk.LEFT, command=hide_toolbar)
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

View.add_checkbutton(label="Status_bar",onvalue=True,offvalue=0,variable=show_toolbar,image=status_bar_image,compound=tk.LEFT,command=hide_statusbar)

#######Color_edit_commond####
def change_color():
    change_them=theme_choice.get()
    color_tupel=color_dict.get(change_them)
    fg_color, bg_color = color_tupel[0], color_tupel[1]
    text_editor.config(background=bg_color,fg=fg_color)


count=0
for i in color_dict:
    Color_theme.add_radiobutton(label=i,image=color_image[count], variable=theme_choice, compound=tk.LEFT,command=change_color )
    count=count+1


#------------------------------- main menu function end -----------------------------#
main_application.config(menu=main_menu)
#####Bind shotcat key#######
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as_file)
main_application.bind("<Control-q>",exit_file)

main_application.bind("<Control-f>",find_file)
main_application.mainloop()