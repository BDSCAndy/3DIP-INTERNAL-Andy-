import tkinter as tk
from tkinter import ttk, messagebox, END
import json                                                                              
from PIL import Image, ImageTk
import customtkinter as ctk

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

class LoadScreen(baseapp):# this class load images
    def __init__(self, root):#initialize the parent class to set up attributes
        super().__init__(root)
        self.load_images()

    def load_images(self): # This loads in all the required images
        image_button3 = Image.open('images/education.png') # education
        self.image_button3 = ctk.CTkImage(light_image=image_button3, dark_image=image_button3, size=(300, 250))

        image_button2 = Image.open('images/personal.png') # Personal
        self.image_button2 = ctk.CTkImage(light_image=image_button2, dark_image=image_button2, size=(300, 250))

        image_button1 = Image.open('images/business.png') # business
        self.image_button1 = ctk.CTkImage(light_image=image_button1, dark_image=image_button1, size=(300, 250))

        self.photos = {} # Stores the images in this dictionary 
        with open('data1.json') as file: # Opens the jason file 
            self.data = json.load(file)
        # Access the image sizes in the json file 
        image_sizes = self.data['image_sizes'] 
        for key_str, size in image_sizes.items(): # to store and to display image onto text widget for loading screen 
            # Convert the key to an integers
            key = int(key_str)
            image_path = f'images/image{key}.png' # Image path 
            image = Image.open(image_path).resize(size)  
            photo = ImageTk.PhotoImage(image)
            self.photos[key] = photo # Stores it in dictionary 
        setup_program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3)
        
class setup_program(baseapp):#This class is login menu
    def __init__(self, root, photos, data, image_button1, image_button2, image_button3):
        super().__init__(root)
        self.photos = photos
        self.data = data
        self.image_button1 = image_button1
        self.image_button2 = image_button2
        self.image_button3 = image_button3
        self.show_account_noww()

    def show_account_noww(self): # This function creates the login menu where the user can add or remove the user account 
        self.width_text_1 = int(self.screen_width/2) # This helps adjust the window size depending on the display resolution 
        self.height_text_1 = int(self.screen_height/2)  
        self.width_text_2 = int(self.width_text_1/2)
        self.show_account_now = ctk.CTkToplevel(self.root,fg_color="#2a2e38")
        self.show_account_now.title("User Information")
        self.show_account_now.geometry(f"{self.width_text_1}x{self.height_text_1}")
        self.show_account_now.attributes("-topmost", True)  # This makes sure it's on top
        
        image = Image.open('images/image70.jpg').resize((self.width_text_2,self.height_text_1)) # open image for login menu 
        self.photo=ctk.CTkImage(light_image=image, dark_image=image, size=((self.width_text_2,self.height_text_1)))
    
        self.image_label = ctk.CTkLabel(self.show_account_now, image=self.photo,text='') # Blank text as its an image label 
        self.image_label.pack(side=ctk.LEFT,padx=0)

        ctk.CTkLabel(self.show_account_now,text="Account",font=('Aerial',24)).pack(pady=(50,0))        
        ctk.CTkLabel(self.show_account_now,text="Full name:").pack()  
        self.entry_name=ctk.CTkEntry(self.show_account_now,width=300) 
        self.entry_name.pack()

        ctk.CTkLabel(self.show_account_now,text="Username:").pack() 
        self.entry_username=ctk.CTkEntry(self.show_account_now,width=300)
        self.entry_username.pack()

        ctk.CTkLabel(self.show_account_now,text="Password:").pack()   
        self.entry_password=ctk.CTkEntry(self.show_account_now,width=300,show='*')
        self.entry_password.pack()
        
        self.select_button=ctk.CTkButton(self.show_account_now,text="Add account",command=self.add_account,width=300).pack(pady=5) 
        self.select_button2=ctk.CTkButton(self.show_account_now,text="Login",command=self.login,width=300).pack(pady=5)
        self.select_button3=ctk.CTkButton(self.show_account_now,text="Clear account list",command=self.clear_account,width=300).pack(pady=5)
        # for better naming for later
        self.account = self.show_account_now
      
    def check_info(self): # This method checks if account is in the text file
        self.name=self.entry_name.get().strip() 
        self.username=self.entry_username.get().strip()
        self.password=self.entry_password.get().strip()
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
                    messagebox.showerror("information", "Account has been added",parent=self.show_account_now)
        else:
            messagebox.showerror("information", "You already have this account",parent=self.show_account_now)
            return
    def login(self): # This method logs the user in if they havnt created an account 
        self.found=False
        self.check_info()
        if self.found:
            self.account.destroy()
            Main_Program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3)
        else:
            if not self.name or not self.username or not self.password:
                return
            else:
                messagebox.showerror("Error", "Please enter the correct username,password and name",parent=self.show_account_now)

    def clear_account(self): # This method clears the account list if there username and password is incorrect
        self.found=False
        self.check_info()
        if self.found:
            erase=open('account.txt','w') 
            erase.write('')
            messagebox.showerror("information", "All accounts have been removed",parent=self.show_account_now)
            return
        else:
            if not self.name or not self.username or not self.password:
                return
            else:
                messagebox.showerror("Input Error", "Please enter the correct username,password and name",parent=self.show_account_now)
class Main_Program(baseapp):# This class is where the main program is
    def __init__(self,root,photos,data,image_button1,image_button2,image_button3):
        super().__init__(root)
        self.photos = photos
        self.data = data
        self.image_button1 = image_button1
        self.image_button2 = image_button2
        self.image_button3 = image_button3
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
        ctk.CTkLabel(self.button_frame, text="Choose one of these options", font=("Arial", 24)).pack(anchor='center', pady=(pading, 0))
        # Add image buttons to the button frame and center them horizontally
        self.select_button4 = ctk.CTkButton(self.main_menuu, text='Logout', command=self.logout, height=50, width=300).pack(pady=10)
        self.select_button1 = ctk.CTkButton(self.button_frame, image= self.image_button1 , text='', fg_color='white', command=self.select_item, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
        self.select_button2 = ctk.CTkButton(self.button_frame, image= self.image_button2, text='', fg_color='white', command=self.select_item2, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
        self.select_button3 = ctk.CTkButton(self.button_frame, image=self.image_button3 , text='', fg_color='white', command=self.select_item3, height=250, width=300).pack(side=ctk.LEFT, padx=(10, 0))
      
    def logout(self): # This goes back to the show accounts. 
        self.main_menuu.destroy()
        self.button_frame.destroy()
        setup_program(self.root, self.photos, self.data, self.image_button1, self.image_button2, self.image_button3)
    
    def next(self): # This method goes to the treeview 
        self.main_menuu.destroy()
        # Proceed to initialize the main application
        self.main_app()

    def main_app(self): # THis method creates the treeview 
        # Create a frame for the Treeview and its scrollbar
        self.tree_frame = tk.Frame(self.root,width=520, height=self.height_text)
        self.tree_frame.pack(side="left", fill="y")
        # Create a Treeview widget
        self.tree = ttk.Treeview(self.tree_frame,style="Treeview")
        self.tree.pack(fill="both", expand=True)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", 
                        fieldbackground="white", foreground="black",bd=0)
        
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
        self.child_items = {
            "Personal": ["Basic Computing", "iPads", "iPhones", "Android phones", "Android tablets"],
            "Business": ["Basic Computing","Office 365", "Printing","Servers","Linux Ubuntu","Counters"],
            "Education": ["Basic Computing","Printing","Office 365","School libraries",'Google suite'],
        }
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

    def select_item(self): # This method directs what the user has selected to the select item_load method 
       self.select_item_load("Business")

    def select_item2(self):
       self.select_item_load("Personal")

    def select_item3(self):
       self.select_item_load("Education")
        
    def back(self): # This method goes back to the main menu
        self.tree_frame.destroy()
        self.content_canvas.destroy()
        self.content_scrollbar.destroy()
        self.main_menu()

    def handle_selection(self): # This methods opens the json file and opens what the user has selected from the json file. 
        with open('data1.json') as file:
            self.data = json.load(file)
        if self.item_text in self.data:
            self.content_section = self.data[self.item_text]
        if not self.content_section: # If what the user has selected isnt in the json file a message box will appear
          messagebox.showerror("Error", "This topic will be added in the future sorry :(")
        self.load_image_text()

    def load_image_text(self): # This method loads the acutal content of the tutorial. 
        frame_bg_color = self.content_frame.cget("background") # Grabs the backgorund of the frame 

        self.width_text_1 = int(self.width_text /15) # Makes window smaller 
        self.height_text_1 = int(self.screen_height/0.05185185185185185185185185185185)

        # Create and configure the Text widget
        self.t = tk.Text(self.content_frame, yscrollcommand=self.content_scrollbar.set, width=self.width_text_1, height=503, highlightthickness=0, bd=0, wrap="word", background=frame_bg_color) # Text widget is used to display the content of the tutorials
        self.t.pack(pady=10,padx=20,expand=True,side="right")

        # Configure text tags
        self.t.tag_configure('center', justify='center')
        self.t.tag_configure('heading', font=('Arial', 24), foreground="White")
        self.t.tag_configure('body', font=('Arial', 11), foreground="White")
        # Loop through the range of content items
        for i in range(1, 100):  # This method extracts the contents, headings, and images and puts it into text widget.
            self.content_key = f'Content{i}'  # JSON file has content which contains the order of images and text
            self.heading_key = f'Heading{i}'  # JSON file has headings.
            if self.heading_key in self.content_section:
                self.heading_text = self.content_section[self.heading_key][0]
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
                        # Else insert body text
                        self.t.insert(END, number + '\n', 'body')
                self.t.insert(END, "\n")
            # For image and text alignment
            self.t.tag_add('center', '1.0', 'end')  # Ensures everything is centered.
        # Configure scrollbar and disable editing
        self.t.configure(yscrollcommand=self.content_scrollbar.set, state=tk.DISABLED)

    def on_tree_select(self, event): # displays the treeview and runs otherm methods
     
        # Get the selected item
        selected_item = self.tree.selection()[0]
        self.item_text = self.tree.item(selected_item, "text")\
        
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.back_button = ctk.CTkButton(self.content_frame, text="Back",command=self.back)
        self.back_button.pack(anchor="sw",pady=10,padx=10)

        self.handle_selection()

        # Configure scrollbar
        self.content_scrollbar.config(command=self.t.yview)
# Create the main window and run the application
if __name__ == "__main__": # This method displays allows the tkinter gui to work. 
    root = ctk.CTk()
    app = LoadScreen(root)
    root.mainloop()

