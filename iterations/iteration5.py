import tkinter as tk
from tkinter import ttk, messagebox, END
import json                                                                              
from PIL import Image, ImageTk
import customtkinter as ctk
import threading  
import google.generativeai as genai
import socket
import translators.server

class baseapp: # This class houses the main program 
    def __init__(self, root): # This method runs other methods and open text file 
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.root.title("Greyscale Technology App")
        self.width_text = int(self.screen_width * 0.98)
        self.height_text = int(self.screen_height * 0.90)
        self.root.geometry(f"{self.width_text}x{self.height_text}+0+0")
        try:
            with open("account.txt", 'r') as self.file:
                pass
        except FileNotFoundError:
            with open("account.txt", 'w') as self.file:
                pass

class LoadScreen(baseapp): # Loading screen class 
    def __init__(self, root):
        super().__init__(root)
        self.loading_screenn()
    def key_press(self,event): # Method is run to disable editing on text widget
        return "break"
        
    def loading_screenn(self): # This function is the loading screen that loads all the images
        self.width_text = int(self.screen_width * 0.98) 
        self.height_text = int(self.screen_height * 0.90) # This sets the geometry behind the top level
        self.root.geometry(f"{self.width_text}x{self.height_text}+0+0")

        self.width_text_1 = int(self.screen_width/2)
        self.height_text_1 = int(self.screen_height/2)  

        # Create a loading screen
        self.loading_screen = ctk.CTkToplevel(self.root, fg_color="#2a2e38") # Top level is what displays the loading screen
        self.loading_screen.title("Grey Scale Technologies")
        self.loading_screen.geometry(f"{self.width_text_1}x{self.height_text_1}")
        self.loading_screen.attributes("-topmost", True)
        self.loading_screen.resizable(False, False) # This ensures the user cant resize the window as its just a loading screen    

        # Add a label for aestheics 
        self.loading_label = ctk.CTkLabel(self.loading_screen, text="\nLoading...", font=('Arial', 35))
        self.loading_label.pack(expand=True)
        # Helps close the windows 

        self.loading_screen.protocol("WM_DELETE_WINDOW", self.dummy_close)
        self.progressbar=ctk.CTkProgressBar(self.loading_screen,width=380)
        self.progressbar.pack(pady=10)
        # Progress bar intital %0
        self.processed_images = 0
        #Progress bar final 100%
        self.processed_images_total = 100
        self.progressbar.set(self.processed_images)
        #Create the text box widget to show whats being loaded (images) 
        self.load_text=ctk.CTkTextbox(self.loading_screen,height=700,width=350,activate_scrollbars=False)
        self.load_text.pack(pady=(10,30))
        # Disables input into the textbox
        self.load_text.bind("<KeyPress>", self.key_press)
        self.load_text.tag_config('center', justify='center')
        
        # Threading to ensure it starts properly and the first thing to load. 
        
        threading.Thread(target=self.load_images).start()

    def dummy_close(self): # CLoses the frame
        # This method is called when the close button is clicked
        pass

    def load_images(self): # This loads in all the required images
        image_button2 = Image.open('images/education.png').resize((300, 250))  # education image button
        self.image_button2 = ctk.CTkImage(light_image=image_button2, dark_image=image_button2, size=(300, 250))

        image_button3 = Image.open('images/business.png').resize((300, 250))  # business imge button 
        self.image_button3 = ctk.CTkImage(light_image=image_button3, dark_image=image_button3, size=(300, 250))

        image_button1 = Image.open('images/personal.png').resize((300, 250))  # personal image button 
        self.image_button1 = ctk.CTkImage(light_image=image_button1, dark_image=image_button1, size=(300, 250))

        self.photos = {} # Stores the images in this dictionary 
        with open('data3.json') as file: # Opens the jason file 
            self.data = json.load(file)
        # Access the image sizes in the json file 
        image_sizes = self.data['image_sizes'] 
        for key_str, size in image_sizes.items(): # to store and to display image onto text widget for loading screen 
            self.load_text.insert(END, f"loading Image{key_str} and resizing to {size}\n",'center')
            self.load_text.see(END)
            # Convert the key to an integers
            key = int(key_str)
            image_path = f'images/image{key}.png' # Image path 
            image = Image.open(image_path).resize(size)  
            photo = ImageTk.PhotoImage(image)
            self.photos[key] = photo # Stores it in dictionary 
            # Increases the progressbar when an image is loaded. 
            if self.processed_images<self.processed_images_total:
                self.processed_images+=0.013
                self.progressbar.set(self.processed_images)
        # Tells the user its been loadted and is loading text 
        self.load_text.insert(END, f"Loading text...........\n Loading complete\n Displaying login",'center')
        self.loading_screen.destroy()
        setup_program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3)

        
class setup_program(baseapp): # Login menu class 
    def __init__(self, root, photos, data, image_button1, image_button2, image_button3): # Gets attributes from previous class 
        super().__init__(root)
        self.photos = photos
        self.data = data
        self.image_button1 = image_button1
        self.image_button2 = image_button2
        self.image_button3 = image_button3
        self.show_account_noww() # Runs next method 

    def show_account_noww(self): # This function creates the login menu where the user can add or remove the user account 
        self.width_text_1 = int(self.screen_width/2) # This helps adjust the window size depending on the display resolution 
        self.height_text_1 = int(self.screen_height/2)  
        self.width_text_2 = int(self.width_text_1/2)
        self.show_account_now = ctk.CTkToplevel(self.root,fg_color="#2a2e38")
        self.show_account_now.title("User Information")

        self.show_account_now.geometry(f"{self.width_text_1}x{self.height_text_1}")
        self.show_account_now.attributes("-topmost", True)  # This makes sure it's on top
        self.show_account_now.resizable(False, False)
        
        image = Image.open('images/image70.jpg').resize((self.width_text_2,self.height_text_1)) # open image for login menu 
        self.photo=ctk.CTkImage(light_image=image, dark_image=image, size=((self.width_text_2,self.height_text_1)))
    
        self.image_label = ctk.CTkLabel(self.show_account_now, image=self.photo,text='') # Blank text as its an image label 
        self.image_label.pack(side=ctk.LEFT,padx=0)

        self.options=ctk.CTkTabview(self.show_account_now,width=self.width_text_2,height=self.height_text_1,fg_color="#2a2e38")
        self.options.pack(side=ctk.RIGHT)

        self.tab2=self.options.add("Login")
        self.tab1=self.options.add("Create Account")

        self.login_menu()
        self.signup_menu()

        # for better naming for later
        self.account = self.show_account_now
    def login_menu(self): # Displays the login menu 
        ctk.CTkLabel(self.tab2,text="Login",font=('Aerial',24)).pack(pady=(20,0))
        ctk.CTkLabel(self.tab2,text="Full name:").pack()
        self.entry_name2=ctk.CTkEntry(self.tab2,width=300) 
        self.entry_name2.pack()
        ctk.CTkLabel(self.tab2,text="Username").pack()
        self.entry_username2=ctk.CTkEntry(self.tab2,width=300)
        self.entry_username2.pack()
        ctk.CTkLabel(self.tab2,text="Password:").pack()  

        self.entry_password2=ctk.CTkEntry(self.tab2,width=300,show='*')
        self.entry_password2.pack()

        self.select_button2=ctk.CTkButton(self.tab2,text="Login",command=self.login,width=300).pack(pady=5)
        self.select_button3=ctk.CTkButton(self.tab2,text="Clear account list",command=self.clear_account,width=300).pack(pady=5)
        self.select_button4=ctk.CTkButton(self.tab2,text="Clear entry",command=self.clear_acocunt_login,width=300).pack(pady=5)
        self.select_button5=ctk.CTkButton(self.tab2,text="Continue as guest",command=self.nologin,width=300).pack(pady=5)

    def signup_menu(self): # displays sign up menu 
        ctk.CTkLabel(self.tab1,text="Sign Up",font=('Aerial',24)).pack(pady=(30,0))
        ctk.CTkLabel(self.tab1,text="Full name:").pack()
        self.entry_name=ctk.CTkEntry(self.tab1,width=300) 
        self.entry_name.pack()
        ctk.CTkLabel(self.tab1,text="Username").pack()
        self.entry_username=ctk.CTkEntry(self.tab1,width=300)
        self.entry_username.pack()
        ctk.CTkLabel(self.tab1,text="Password:").pack()  
        self.entry_password=ctk.CTkEntry(self.tab1,width=300,show='*')
        self.entry_password.pack()
        self.select_button=ctk.CTkButton(self.tab1,text="Add account",command=self.add_account,width=300).pack(pady=5) 
        self.select_button4=ctk.CTkButton(self.tab1,text="Clear entry",command=self.clear_acocunt_login,width=300).pack(pady=5)

    def clear_acocunt_login(self): # This clears the users selection 
        self.entry_name.delete(0, 'end')
        self.entry_username.delete(0,'end')
        self.entry_password.delete(0,'end')
        self.entry_name2.delete(0, 'end')
        self.entry_username2.delete(0,'end')
        self.entry_password2.delete(0,'end')

    def nologin(self): # This method Logs in as guest
            self.account.destroy()
            account_is_logged_in=False
            Main_Program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3,account_is_logged_in)
        
    def check_info(self): # This method checks if account is in the text file
        self.name = self.entry_name.get().strip() or self.entry_name2.get().strip()
        self.username=self.entry_username.get().strip() or self.entry_username2.get().strip()
        self.password=self.entry_password.get().strip() or self.entry_password2.get().strip()
        if not self.name or not self.username or not self.password:
            messagebox.showerror("Input Error", "Please enter your a username,password and username",parent=self.show_account_now)
            return  
        else:
            with open("account.txt","r") as file:
                self.work=file.readlines()
            for i in self.work:
                self.account_name,self.account_username,self.ac_password = i.strip().split(":")# Splits the acccount name and password.
                if self.name==self.account_name and self.username==self.account_username and self.password ==self.ac_password:
                    self.found=True
                    return
    def add_account(self): # This merhod can create an account that you havnt added
        self.found=False
        self.check_info()
        if not self.found:
            if not self.name or not self.username or not self.password:
                return
            else:
                with open('account.txt',"a") as file:
                    file.write(f"{self.name}:{self.username}:{self.password}\n")
                    messagebox.showinfo("information", "Account has been added",parent=self.show_account_now)
        else:
            messagebox.showerror("information", "You already have this account added to our app",parent=self.show_account_now)
            return
    def login(self): # This method logs the user in if they havnt created an account 
        self.found=False
        self.check_info()
        if self.found:
            self.account.destroy()
            account_is_logged_in=True
            Main_Program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3,account_is_logged_in)
            
        else:
            if not self.name or not self.username or not self.password:
                return
            else:
                messagebox.showerror("Error", "Please enter the correct username, password and name",parent=self.show_account_now)

    def clear_account(self): # This method clears the account list if there username and password is incorrect
        self.found=False
        self.check_info()
        if self.found:
            erase=open('account.txt','w') 
            erase.write('')
            messagebox.showinfo("information", "All accounts have been removed",parent=self.show_account_now)
            return
        else:
            if not self.name or not self.username or not self.password:
                return
            else:
                messagebox.showerror("Input Error", "Please enter the correct username,password and name",parent=self.show_account_now)
                
class Main_Program(baseapp): # This class is the main program, main menu and treeviews.
    def __init__(self,root,photos,data,image_button1,image_button2,image_button3,account_is_logged_in): # This method Passes down attribute
        super().__init__(root)
        self.photos = photos
        self.data = data
        self.image_button1 = image_button1
        self.image_button2 = image_button2
        self.image_button3 = image_button3
        self.account_is_logged_in=account_is_logged_in
        self.change_lan = False 
        self.main_menu()
    def main_menu(self): # This displays 3 image buttons to proceed to next frame and a logout button. 
        self.width_text_1 = int(self.width_text / 2)
        self.height_text_1 = int(self.screen_height)

        # Main Menu Frame
        self.main_menuu = ctk.CTkFrame(self.root, bg_color="#2a2e38", fg_color="#2a2e38")
        self.main_menuu.pack(fill='both', expand=True)
        pading=self.height_text_1/4
        # Create a frame to hold the buttons
        self.button_frame = ctk.CTkFrame(self.main_menuu, fg_color="#2a2e38")
        self.button_frame.pack(anchor='center', pady=(0, 0), padx=(0, 10))
        ctk.CTkLabel(self.button_frame, text="Choose one of these options", font=("Arial", 24)).pack(anchor='center', pady=(180,0))
        # Add image buttons to the button frame and center them horizontally

        self.selection_all=ctk.CTkButton(self.main_menuu,text="View all",command=self.view_all,height=50,width=300).pack(pady=5)
        self.select_button5 = ctk.CTkButton(self.main_menuu, text='languages', command=self.settings_options, height=50, width=300).pack(pady=5)
        self.select_button4 = ctk.CTkButton(self.main_menuu, text='Back', command=self.logout, height=50, width=300).pack(pady=5)

        self.select_button1 = ctk.CTkButton(self.button_frame, image= self.image_button1 , text='', fg_color='white', command=self.select_item, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
        self.select_button2 = ctk.CTkButton(self.button_frame, image= self.image_button2, text='', fg_color='white', command=self.select_item2, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
        self.select_button3 = ctk.CTkButton(self.button_frame, image=self.image_button3 , text='', fg_color='white', command=self.select_item3, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
    def view_all(self): # Expands entire treeview 
        self.next()
        self.tree.item(self.root_item, open=True)
        for child_item in self.tree.get_children(self.root_item):
            self.tree.item(child_item, open=True)
        self.tree.selection_set(self.root_item)
    
    def logout(self): # This goes back to the show accounts. 
        self.main_menuu.destroy()
        self.button_frame.destroy()
        setup_program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3)
    
    def next(self): # This method goes to the treeview 
        self.main_menuu.destroy()
        # Proceed to initialize the main application
        self.main_app()
    def key_press(self,event): # Disables edit for text widget
        return "break"
    def settings_options(self): # Top level to display the language options
        if self.account_is_logged_in:
            self.width_text_1 = int(self.screen_width/2) # This helps adjust the window size depending on the display resolution 
            self.height_text_1 = int(self.screen_height/2)  
            self.width_text_2 = int(self.width_text_1/2)
            self.setting = ctk.CTkToplevel(self.root,fg_color="#2a2e38")
            self.setting.title("Settings")
            self.setting.geometry(f"{self.width_text_1}x{self.height_text_1}")
            self.setting.attributes("-topmost", True)  # This makes sure it's on top
            self.setting.resizable(False, False)

            self.languages={"English": "en","Chinese": "zh","Maori": "mi","Hindi": "hi","Spanish": "es"}
            # Uses combobox for selection 
            ctk.CTkLabel(self.setting,text="Languages",font=('Aerial',24)).pack(pady=(50,0)) 
            ctk.CTkLabel(self.setting,text='This only translates the contents not the treeview of buttons').pack(pady=5)
            self.language_box=ctk.CTkComboBox(self.setting,width=300,values=list(self.languages.keys()))
            #self.language_box.set("English") 
            self.language_box.bind("<KeyPress>", self.key_press)
            self.default_combo()
            self.language_box.pack(pady=5)
            self.apply=ctk.CTkButton(self.setting,width=300,text="Apply language",command=self.lang_1)
            self.apply.pack(pady=5)
            self.close_button=ctk.CTkButton(self.setting,width=300,text="Close",command=self.close_language)
            self.close_button.pack(pady=5) 
        else:
                messagebox.showinfo("Error", "You need an account")
                return
    def default_combo(self): # This method shows the default preset for combo box
        with open("combobox.txt", 'r') as file_combo:
            self.combo = [line.strip() for line in file_combo.readlines()]  # Strip newline characters

        if not self.combo:  # If the combo list is empty
            self.language_box.set("English")
            return
        
        # Set the first item in the combo box if it's not empty
        self.language_box.set(self.combo[0])  
        self.change_lan = True

    def lang_1(self): # This method tells the load_Image_text if you need to translate the program. 
        self.change_lan = False
        self.selected_language = self.language_box.get()
        self.language = self.languages.get(self.selected_language, None)  # Use .get to avoid KeyError

        # Set change_lan based on language selection
        if self.selected_language != "English":
            messagebox.showinfo("Error", "Language has been changed",parent=self.setting)
            with open("combobox.txt", 'w') as file_combo:
                file_combo.write(self.selected_language)
                self.change_lan = True
        else:
            with open("combobox.txt", 'w') as file_combo:
                file_combo.write("")  # Clear the file
                messagebox.showinfo("Error", "Language has been changed",parent=self.setting)
                self.change_lan = False


    def close_language(self):   # This method closes the self.setting top level widget
        self.setting.destroy()   

    def main_app(self): # THis method creates the treeview 
        # Create a frame for the Treeview and its scrollbar
        self.tree_frame = tk.Frame(self.root,width=320, height=self.height_text)
        self.tree_frame.pack(side="left", fill="y")

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.tree_frame,style="Treeview")
        self.tree.pack(fill="both", expand=True)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", 
            fieldbackground="white", foreground="black",bd=0,font=('Aerial', 13))
        
        # Insert items into the treeview
        self.setup_tree()

        # Bind the Treeview select event to the handler
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Create a canvas for the content frame
        self.content_canvas = tk.Canvas(self.root)
        self.content_frame = tk.Canvas(self.content_canvas,background="#2a2e38")
        self.content_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.content_canvas.yview)

        # Place the canvas and scrollbar in the root window
        self.content_canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.content_canvas.configure(yscrollcommand=self.content_scrollbar.set, highlightthickness=0, bd=0)
        
        # Pack the widgets
        self.content_scrollbar.pack(side="right", fill="y")
        self.content_canvas.pack(side="right", fill="both", expand=True)
        self.content_frame.pack(fill="both", expand=True)

        # Update scroll region of the canvas
        self.content_frame.update_idletasks()
        self.content_canvas.config(scrollregion=self.content_canvas.bbox("all"))
    
    def setup_tree(self): # This method loads the treeview
        # Insert a root item
        self.root_item = self.tree.insert("", "end", text="Grey Scale Technology")
        # Define child items and their corresponding sub-items
        self.child_items = self.data['tree_items']

        # Insert child items and their sub-items
        for self.child_text, sub_items in self.child_items.items():
            # Insert child item
            child_item = self.tree.insert(self.root_item, "end", text=self.child_text)
            
            # Insert sub-child items
            for sub_item_text in sub_items:
                self.tree.insert(child_item, "end", text=sub_item_text)

        # Expand all items
        self.tree.item(self.root_item, open=True)

    def select_item_load(self,text): # This method directs the user to the next frame and it also expands the item and sub item the user has clicked on from the tree buttons
        self.next()
        for child_item in self.tree.get_children(self.root_item):
            if self.tree.item(child_item, "text") == text:
                self.tree.selection_set(child_item)
                self.tree.item(child_item, open=True)
                self.tree.focus(child_item)

    def select_item(self): # These method directs what the user has selected to the select item_load method 
       self.select_item_load("Personal")

    def select_item2(self):
       self.select_item_load("Education")

    def select_item3(self):
       self.select_item_load("Business")
        
    def back(self): # This method goes back to the main menu
        self.tree_frame.destroy()
        self.content_canvas.destroy()
        self.content_scrollbar.destroy()
        self.main_menu()
            
    def handle_selection(self): # This methods opens the json file and opens what the user has selected from the json file. )
        with open("data3.json") as file:
            self.data = json.load(file)
        if self.item_text in self.data:
            self.content_section = self.data[self.item_text]
        if not self.content_section: # If what the user has selected isnt in the json file a message box will appear
            messagebox.showinfo("Error", "This topic will be added in the future sorry :(")
        #self.load_image_text()

        threading.Thread(target=self.load_image_text).start() # Can help show translation real time
    def scroll_down(self): # This method scrolls down when the user presses the next button 
        if self.scroll_pos < 1.0:
            self.scroll_pos += self.scroll_preset_value 
            self.t.yview_moveto(self.scroll_pos)
        else:
            print()

    def scroll_up(self): # This method scrolls up if the user has pressed the previous button 
        if self.scroll_pos > 0.0:
            self.scroll_pos -= self.scroll_preset_value 
            self.t.yview_moveto(self.scroll_pos)
    def key_press(self,event): # Disables keybaord input into text widget
        return "break"
    
    def load_image_text(self): # This method loads the acutal content of the tutorial.  
        self.scroll_pos = 0.0  # This sets the scroll position 
        frame_bg_color = self.content_frame.cget("background") # Grabs the backgorund of the frame 

        self.width_text_1 = int(self.width_text /15) # Makes window smaller 
        self.height_text_1 = int(self.screen_height/0.05185185185185185185185185185185)

        for i in range(1, 100): # This for loop finds the scroll preset given in the json file and applies it to the specific subitem buttons 
            self.scroll_preset = f'scroll{i}'
            if self.scroll_preset in self.content_section:
                    self.scroll_preset_value = self.content_section[self.scroll_preset][0]  
                    self.next_button = ctk.CTkButton(self.content_frame, text="Next", command=self.scroll_down)
                    self.next_button.pack(side="right", anchor="se", pady=10, padx=50)

                    # Create and configure the Previous button at the bottom left
                    self.previous_button = ctk.CTkButton(self.content_frame, text="Previous", command=self.scroll_up)
                    self.previous_button.pack(side="left", anchor="sw", pady=10, padx=50)

        # Create and configure the Text widget
        self.t = tk.Text(self.content_frame, yscrollcommand=self.content_scrollbar.set, width=self.width_text_1, height=503, highlightthickness=0, bd=0, wrap="word", background=frame_bg_color) # Text widget is used to display the content of the tutorials
        self.t.pack(pady=10,padx=20,expand=True,side="right")
        # Configure text tags
        self.t.tag_configure('center', justify='center')
        self.t.tag_configure('heading', font=('Arial', 30), foreground="White")
        self.t.tag_configure('body', font=('Arial', 14), foreground="White")
        self.t.bind("<KeyPress>", self.key_press)
        
        # Loop through the range of content items
        for i in range(1, 100):  # This method extracts the contents, headings, and images and puts it into text widget.
            self.content_key = f'Content{i}'  # JSON file has content which contains the order of images and text
            self.heading_key = f'Heading{i}'  # JSON file has headings.
            if self.heading_key in self.content_section:
                self.heading_text = self.content_section[self.heading_key][0]
                if self.change_lan:
                    self.google=translators.server.google( self.heading_text,to_language=f"{self.language}")
                    self.t.insert(END, self.google + "\n", ('center', 'heading'))
                else:
                    self.t.insert(END, self.heading_text + "\n", ('center', 'heading'))
            if self.content_key in self.content_section:
                contents = self.content_section[self.content_key]
                for number in contents:
                    if isinstance(number, int):
                        # Check if it's an image
                        if number in self.photos:
                            self.t.image_create(END, image=self.photos[number])
                            self.t.insert(END, "\n")
                    else:
                        if self.change_lan:
                            self.google=translators.server.google(number,to_language=f"{self.language}")
                            self.t.insert(END, self.google + '\n', 'body')
                        else:
                            self.t.insert(END, number + '\n', 'body')
                self.t.insert(END, "\n")
            # For image and text alignment
            self.t.tag_add('center', '1.0', 'end')  # Ensures everything is centered.
        # Configure scrollbar and disable editing
        self.t.configure(yscrollcommand=self.content_scrollbar.set, state=tk.DISABLED)
        # Configure scrollbar
        self.content_scrollbar.config(command=self.t.yview)        


    def chat_bot(self): # Chatbot gui 
        # Creating label with text
        ctk.CTkLabel(self.content_frame, text="Ask Gemini if you need help:", font=('Arial', 20)).pack(pady=20)

        # Creating entry for question input
        self.question_entry = ctk.CTkEntry(self.content_frame, width=800)
        self.question_entry.pack(pady=5)  # Corrected the pack call from `self.entry_username`

        # Creating button for submitting question
        self.question_button = ctk.CTkButton(self.content_frame, text="Submit", command=self.check_entry)
        self.question_button.pack(pady=5)

        self.textbox_size=self.screen_height/2
        # Creating a Textbox to display the answer
        self.response_textbox =ctk.CTkTextbox(self.content_frame, width=800,height=self.textbox_size)
        self.response_textbox.pack(pady=5)  
        self.response_textbox.bind("<KeyPress>", self.key_press)

        self.clear_button = ctk.CTkButton(self.content_frame, text="clear", command=self.clear_chatbot)
        self.clear_button.pack(pady=5)
    def clear_chatbot(self): # Clears  users entry for chatbot 
        self.response_textbox.delete("1.0", "end")
        self.question_entry.delete(0, 'end')

    
    def check_entry(self):# This method checks if the user has entered in something or not. 
        self.quest = self.question_entry.get().strip()
        if not self.quest:
            messagebox.showerror("Input Error", "Please enter a question for Gemini.")
        else:
            self.gemini_bot()

    def gemini_bot(self): # This method connects the user input into gemini and displays the answer in a text widget. 
        if not self.check_internet():
            self.response_textbox.delete("1.0", "end")
            self.response_textbox.insert("1.0", "No internet connection. Please check your connection and try again.")
            return

        self.API_KEY = "AIzaSyDigomQX1lul0Kd3i-M-N8Vn7osPVJRenE"
        genai.configure(api_key=self.API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        #generate and display response toquestion
        self.answering_question = model.generate_content(f"{self.quest}")

        # clear any text
        self.response_textbox.delete("1.0", "end")
        self.response_textbox.insert("1.0", self.answering_question.text)
    

    def check_internet(self): # This method checks the internet before running gemini 
        try:
            # Try to connect to a well-known host (Google DNS)
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            return False

    def on_tree_select(self, event): # displays the treeview and runs otherm methods
     
        # Get the selected item
        selected_item = self.tree.selection()[0]
        self.item_text = self.tree.item(selected_item, "text")\
        
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.back_button = ctk.CTkButton(self.content_frame, text="Back",command=self.back)
        self.back_button.pack(anchor="sw",pady=10,padx=10)

        if self.item_text == "Chatbot":
            self.chat_bot()
        else:
            self.handle_selection()

        if self.item_text in ("Chromebook", "Linux Ubuntu", "Servers", "School libraries", "Counters", "Google suite"):
            self.t.insert(END,"\n\n") 
            self.t.insert(END,"Coming soon",'heading','\n','center')
            self.t.insert(END,f"\n")
            self.t.insert(END,"The option you have selected is currently not available at the moment. I am sorry for the inconvience :(",'body','\n','center')
            self.t.tag_add('center', '1.0', 'end')

# Create the main window and run the application
if __name__ == "__main__": # This method displays allows the tkinter gui to work. 
    root = ctk.CTk()
    app = LoadScreen(root)
    root.mainloop()

