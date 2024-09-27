import tkinter as tk
from tkinter import ttk, messagebox, END
from PIL import Image, ImageTk

class Program: # Houses the entire program
    def __init__(self, root):
        self.root = root
        self.root.title("Greyscale Technology App")
        self.root.geometry("1440x900")
        
        # Initialize lists to store images and PhotoImage objects
        self.photos = []

        # Load images
        self.load_images()

        # Create and display the initial verification for name and age
        self.show_initial_veri()

    def show_initial_veri(self): # Login menu 
        # Create a new frame to show age and name entries
        veri = tk.Frame(self.root)
        veri.pack()
        self.root.geometry("300x200")
        
        # Create labels and entry fields for name and age
        tk.Label(veri, text="Name:").pack()
        self.name_entry = tk.Entry(veri)
        self.name_entry.pack()
        
        tk.Label(veri, text="Age:").pack()
        self.age_entry = tk.Entry(veri)
        self.age_entry.pack()

        # Create a submit button
        submit_button = tk.Button(veri, text="Submit", command=self.submit_info)
        submit_button.pack(pady=5)
        
        # Store reference to the verification window
        self.veri = veri

    def submit_info(self): # Checks if the name and age is valid 
        self_age=self.age_entry.get()
        self.name=self.name_entry.get()
        try:
            age = int(self_age)
            if not age and not self.name:
                messagebox.showerror("Error", "Please enter a valid name and age.")
                return
            elif 1 <= age <= 110 and self.name:
                self.veri.destroy()
                self.main_app()
            else:
                messagebox.showerror("Error", "Please enter a valid name and age.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid name and age.")

    def main_app(self): # The mainapp (treeview with content frame)
        self.root.geometry("1440x900")
        # Create a frame for the Treeview and its scrollbar
        self.tree_frame = tk.Frame(self.root, width=320, height=900)
        self.tree_frame.pack(side="left", fill="y")

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(fill="both", expand=True)

        # Insert items into the Treeview
        self.setup_tree()

        # Bind the Treeview select event to the handler
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Create a canvas for the content frame
        self.content_canvas = tk.Canvas(self.root)
        self.content_frame = tk.Frame(self.content_canvas)
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

    def setup_tree(self): # This method sets up the treeview by loading it
        #Insert a root item
        self.root_item = self.tree.insert("", "end", text="Grey Scale Technology (3DIP)")
        #Define child items and their corresponding sub-items
        child_items = {
            "Personal": ["Basic computing", "iPads", "iPhones", "Android phones", "Android tablets"],
            "Business": ["Basic computing","Office 365", "Printing","Servers","Linux Ubuntu","Counters"],
            "Education": ["Basic computing","Printing","Office 365","School libraries",'Google suite']
        }

        # Insert child items and their sub-items
        for child_text, sub_items in child_items.items():
            # Insert child item
            child_item = self.tree.insert(self.root_item, "end", text=child_text)

            # Insert sub-child items
            for sub_item_text in sub_items:
                self.tree.insert(child_item, "end", text=sub_item_text)

        # Expand all items
        self.tree.item(self.root_item, open=True)
        for child_item in self.tree.get_children(self.root_item):
            self.tree.item(child_item, open=True)
        
        # Select the root item
        self.tree.selection_set(self.root_item)
    def content(self): # Holds the main content for the tutorials
            self.basic_computing = {
                "content": [
                    "Basic computing",
                    "Mac OS",
                    "Windows",
                    "How to open an app?",
                    "How to search an app on Mac OS?",
                    "How to search an app on windows?"
                ],
                "details": [
                    "The most common types of operating systems that your PC could be using is Windows 10/11 or Mac OS.",
                    "To help identify your operating system, if you see a Windows icon at the bottom center or left of your icon, you are using Windows. If you see a Mac logo at the top left, then you are on Mac OS.",
                    "On the bottom of your screen press on the icons on the taskbar/dock The three main primary apps are web broswers like (Safari,MS Edge),Mailing apps and messaging apps",
                    "On Mac OS press command + space to open spotlight search",
                    "The most used apps on PC/MAC is internet broswers like safari/Microsoft edge, Mail,MS store/appstore, office 365/apple office suite(keynote,pages) etc.",
                    "Press the windows key and type in the app/file you want to open"
                ]
            }

            self.grey_scale_technology = {
                "title": "Grey Scale technolgoy (3DIP)",
                "content": [],
                "details": [
                    "Welcome to Grey scale technologies where you can find and understand the basics of how to use technology from a business, educational, and personal standpoint."
                ]
            }
            self.ipads = {
                "content": [
                    "Ipads",
                    "How to use Safari",
                    "Facetime",
                    "Appstore",
                    "Messages"
                ],
                "details": [
                    "The purpose of an Ipad is that it can be used as a tablet or a replacement laptop. A tablet is essentially a smartphone but bigger in size. Why users would want a tablet is its protable while still having a larger screen reesate compared to phones with the power of pc/laptops",
                    "You can use  1-2 fingers to swipe between app pages",
                    "If you keep swiping right eventually you will reach the appdraw",
                    "If you go back to the homescreen and swipedown with 1-2 fingers you can open search",
                    "If you swipt up you can open the appswitcher",
                    "The four mains apps you need to learn inorder to use an iphone are:",
                    "Simply press on the topbar then search!",
                    "Make sure you have a contact added and click on there profile to start a call",
                    "Essentailly there are 4 options, There are favourites,recents,contacts,keypads, and voice mails",
                    "In order to send text do"
                ]
            }
            self.iphones = {
                "content": [
                    "Iphone",
                    "Main",
                    "How to use Safari",
                    "Phone app",
                    "Appstore",
                    "Messages"
                ],
                "details": [
                    "An iPhone is an Apple product used to make phone calls and communicate with others",
                    "The four mains apps you need to learn inorder to use an iphone are:",
                    "Simply tap on the bar at the bottom of the app and search for a website or keywords and press enter",
                    "Essentailly there are 4 options, There are favourites,recents,contacts,keypads, and voice mails. The image shown below is the keypad where you can dial any number.",
                    "To navigate throughout the appstore look at the bottom bars given",
                    "Click on one of the contacts or add one",
                    "In order to send a message press on the box"
                ]
            }
            self.android_phones = {
                "content": [
                    "Android Phone",
                    "How to navigate your android phone",
                    "Main apps used on android",
                    "How to use Google chrome",
                    "How to use phone app",
                    "How to use playstore",
                    "How to use Messages"
                ],
                "details": [
                    "An android phone is a device that can help connect and communicate with others online. Android is an operating system developed by google which are found on devices such as Samsusng, Google(pixel), Oppo, Nothing and more",
                    "All devices that use android have there own look to it. An example of this is Samsungs One UI:",
                    "Swipe down to open the appdraw(location of the rest of your apps)",
                    "Swipe down to open the control centre(location of the rest of your apps)",
                    "Launch the app and tap and tap on the bar that says search or type URL (Uniform Resource Locator)",
                    "There are 3 main features in the phone app being recent, keypad(manually dialing a number) and contacts(peoples number you added)",
                    "keypad",
                    "In order to add a contact press + button at the top right:",
                    "Search for the app and tap on the app you want",
                    "Then tap the install button",
                    "Make sure to have added contacts earlier and begin texting!"
                ]
            }
            self.android_tablets = {
                "content": [
                    "Android tablet",
                    "How to navigate your android tablet.",
                    "Main apps used on android",
                    "How to use Google playstore",
                    "How to use messages"
                ],
                "details": [
                    "An android tablet  similar to a phone but bigger is a device that can help connect and communicate with others online. Android is an operating system developed by google which are found on devices such as Samsusng, Google(pixel), Oppo, Nothing and more",
                    "Just like an android phone use fingers to swipe up to access the app draw",
                    "Use fingers to swipe down to access the control centre",
                    "Tap on the topbar to search for the app you want to install",
                    "Search for the app",
                    "Press on the app you want and press the install button",
                    "Make sure you have contacts added to messages",
                    "Then tap on the chatbar and start typing and return it to send!"
                ]
            }
            self.office_365 = {
                "content": [
                    "Office 365",
                    "How to use Microsoft word",
                    "How to use Onenote",
                    "How to use Onedrive"
                ],
                "details": [
                    "Office 365 is a subscription-based service from Microsoft that provides access to various productivity tools like Word, Excel, PowerPoint, and cloud services like OneDrive and Outlook.",
                    "Microsoft Word is a word processing software developed by Microsoft, used for creating, editing, and formatting text documents. Begin by pressing the create button",
                    "This can change text colour",
                    "Highlight text press on this icon",
                    "OneNote is a digital note-taking application developed by Microsoft that allows users to organize notes, drawings, and other content into notebooks.",
                    "Press add notebook",
                    "Select the colour,name and location of your notebook and press create",
                    "Create a section and page if you have not already and start typing",
                    "You can drag and drop images, and drag the text and images around the notebook",
                    "OneDrive is a cloud storage service provided by Microsoft that allows users to store, share, and access files and documents from anywhere with an internet connection.\n On the taskbar icons on windows/mac you can check if your files are synced (assumming you have already setup onedrive)",
                    "In the onedrive folder you can drag and drop files into the folder and it will automatically sync to the onedrive online. You can also free up space or keep the file on your pc by right clicking on the file",
                    "More will  office 365 apps will be added in the future"
                ]
            }
            self.printing = {
                "content": ["Printing"],
                "details": [
                    "Printing is needed to make physical copies of information, ensuring it's accessible, shareable, and durable.",
                    "Open system preferences",
                    "Press the + button at the bottom left to add a printer and then select the printer you want to add",
                    "Search for the printer you want and add press the add button device button",
                    "On windows press the windows key and search for printer",
                    "Press the add device button for you chosen printer",
                    "In order to print e.g. word documents,txt files,pdf or images usually you have to find the print button in the app or use shortcuts like command/control + p"
                ]
            }
    def load_images(self): # Load images before starting the program
        # Dictionary to store specific sizes for each image
        image_sizes = {
            1: (800, 20), 2: (800, 30), 3: (800, 90), 4: (800, 30), 5: (500, 331),6: (450, 331), 7: (600, 401), 8: (500, 431), 9: (400, 101), 10: (400, 400),11: (200, 400), 12: (350, 200), 13: (700, 427), 14: (400, 320), 15: (400, 350),16: (350, 427), 17: (350, 257), 18: (500, 400), 19: (400, 101), 20: (500, 400),21: (500, 400), 23: (600, 401), 24: (600, 401), 25: (600, 401), 26: (500, 400),27: (300, 607), 28: (150, 150), 29: (400, 101), 30: (600, 551), 31: (600, 551),32: (300, 601), 33: (300, 601), 34: (300,601), 35: (600, 601), 36: (300, 601),
            37: (600, 601), 38: (300, 601), 39: (300, 601), 40: (600, 601), 41: (300, 601),42: (600, 401), 43: (600, 401), 44: (600, 251), 45: (400, 101), 46: (700, 300),47: (700, 300), 48: (700, 300), 49: (700, 300), 50: (700, 300), 51: (800, 400),52: (220, 300), 53: (220, 200), 54: (150, 150), 55: (800, 400), 56: (800, 400),57: (250, 300), 58: (800, 400), 59: (800, 400), 60: (800, 400), 61: (200, 400),
            62: (800, 500), 63: (450, 380), 64: (450, 350), 66: (450, 350), 67: (650, 180), 68: (650, 350), 69: (650, 380)
        }
        # Loop through the image file names and sizes
        for i in range(1, 70):
            image_path = f'images/image{i}.png'
            if i in image_sizes:
                self.load_image(image_path, image_sizes[i])

    def load_image(self, path, size): # Stores the photos into a list
        # Open and resize image
        image = Image.open(path).resize(size)
        photo = ImageTk.PhotoImage(image)
    
        # Append the image and PhotoImage to the lists
        self.photos.append(photo)

    def on_tree_select(self, event): # Loads the treeview and all the contents
        # Clear the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Get the selected item
        selected_item = self.tree.selection()[0]
        item_text = self.tree.item(selected_item, "text")
      
        self.content()
           # Get the background color of the content frame
        frame_bg_color = self.content_frame.cget("background")

         # Create and configure the Text widget
        self.t = tk.Text(self.content_frame, yscrollcommand=self.content_scrollbar.set, width=120, height=5000,highlightthickness=0, bd=0,wrap="word",background=frame_bg_color)
        #highlightthickness=0, bd=0,wrap="word",background=frame_bg_color
        self.t.pack(padx=20)

        # Configure text tags
        self.t.tag_configure('center', justify='center')
        self.t.tag_configure('heading', font=('Arial', 24))
        self.t.tag_configure('body', font=('Arial', 11))
        # Loads the acutal content
        if item_text=="Personal":
            self.t.insert(END,"\n\n")
            self.t.insert(END,"Personal technology",'heading',"\n",'center'+ END,"",'body',"\n",'center',"\n\n") # Heading basic computing
            self.t.tag_add('center', '1.0', 'end')
        elif item_text=="Education":
            self.t.insert(END,"\n\n")
            self.t.insert(END,"Educational technology",'heading',"\n",'center'+ END,"",'body',"\n",'center',"\n\n") # Heading basic computing
            self.t.tag_add('center', '1.0', 'end')
        elif item_text=='Business':
            self.t.insert(END,"\n\n")
            self.t.insert(END,"Technology for businesses",'heading',"\n",'center'+ END,"",'body',"\n",'center',"\n\n") # Heading basic computing
            self.t.tag_add('center', '1.0', 'end')

        elif item_text == "Basic computing":
            # Insert text with 'center' tag and additional content
            self.t.insert(END,"\n\n")
            self.t.insert(END,self.basic_computing["content"][0],'heading',"\n",'center'+ END,self.basic_computing["details"][0],'body',"\n",'center'+ END,self.basic_computing["details"][1],'body',"\n",'center'+END,"\n\n") # Heading basic computing
            self.t.insert(END,self.basic_computing["content"][1],'heading',"\n",'center') # Mac os heading
            self.t.image_create(END, image=self.photos[0]) #mac bar image
            self.t.insert(END,"\n") 
            self.t.insert(END,self.basic_computing["content"][2],'heading',"\n",'center') #  Windows heading
            self.t.image_create(END, image=self.photos[1]) #windows bar image
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.basic_computing["content"][3],'heading',"\n") #  how to open an app
            self.t.insert(END,self.basic_computing["details"][2],'body',"\n",'center')# description of opening app
            self.t.image_create(END, image=self.photos[2]) #mac image
            self.t.insert(END,"\n") 
            self.t.image_create(END, image=self.photos[3]) # windows image
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.basic_computing["content"][4],'heading','\n') #  How to search an app on mac os
            self.t.insert(END,self.basic_computing["details"][3],'body',"\n",'center')# command key
            self.t.image_create(END, image=self.photos[4]) # windows image
            self.t.insert(END,"\n \n")
            self.t.insert(END,self.basic_computing["details"][4],'body','\n','center')# most used app
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.basic_computing["content"][5],'heading','\n','center') #  How to search an app on Windows
            self.t.insert(END,self.basic_computing["details"][5],'body',"\n",'center')# most used app
            self.t.image_create(END, image=self.photos[7]) # windows image
            self.t.tag_add('center', '1.0', 'end')

        elif item_text=="iPads":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.ipads["content"][0],'heading','\n','center') # heading
            self.t.insert(END,self.ipads["details"][0],'body','\n','center') # purpose of the ipad 
            self.t.image_create(END, image=self.photos[5]) # ipad image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.ipads["details"][1],'body','center') # You can use finger to swipe betweeb pages
            self.t.image_create(END, image=self.photos[6]) # swipe up and down image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.ipads["details"][2],'body','center') #swipe to app draw
            self.t.image_create(END, image=self.photos[21]) # Ipad app draw image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.ipads["details"][3],'body','\n','center')# Swipe up to search
            self.t.image_create(END, image=self.photos[23]) # Ipad search image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.ipads["details"][4],'body','\n','center')# swipe up to appswitcher
            self.t.image_create(END, image=self.photos[22]) # Ipad app switcher image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.ipads["details"][5],'body','\n','center') # the 4 main apps text
            self.t.image_create(END, image=self.photos[18]) # Ipad 4 main apps image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.ipads["content"][1],'heading','\n','center') # How to use safari
            self.t.insert(END,self.ipads["details"][6],'body','\n','center') # how to search with safari
            self.t.image_create(END, image=self.photos[17]) # image of safari
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.ipads["content"][2],'heading','\n','center') # facetime heading
            self.t.insert(END,self.ipads["details"][7],'body','\n','center') # facetime desccription
            self.t.image_create(END, image=self.photos[19]) # Ipad facetime image
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.ipads["content"][3],'heading','\n','center') # appstore heading
            self.t.insert(END,self.ipads["details"][8],'body','\n','center') # appstore search
            self.t.image_create(END, image=self.photos[20]) #appstore
            self.t.insert(END,f"\n\n") 
            self.t.insert(END,self.ipads["content"][4],'heading','\n','center') # messages heading
            self.t.insert(END,self.ipads["details"][9],'body','\n','center') # message description
            self.t.image_create(END, image=self.photos[24]) # Ipad messsages
            self.t.tag_add('center', '1.0', 'end')

        elif item_text=="iPhones":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.iphones["content"][0],'heading','\n','center') # iphone heading
            self.t.insert(END,self.iphones["details"][0],'body','\n','center') # iphone description
            self.t.image_create(END, image=self.photos[9]) # iphone image
            self.t.insert(END,f"\n\n")

            self.t.insert(END,self.iphones["content"][1],'heading','\n','center') # The main 4 apps description
            self.t.insert(END,self.iphones["details"][1],'body','\n','center') # desciption of the 4 main apps
            self.t.image_create(END, image=self.photos[8]) # iphone main apps image
            self.t.insert(END,f"\n\n")
            
            self.t.insert(END,self.iphones["content"][2],'heading','\n','center') # The main 4 apps description
            self.t.insert(END,self.iphones["details"][2],'body','\n','center') # desciption of the 4 main apps
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[11]) # safari bar 
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[10]) # safari search image
            self.t.insert(END,f"\n\n")

            self.t.insert(END,self.iphones["content"][3],'heading','\n','center') # Phone app heading
            self.t.insert(END,self.iphones["details"][3],'body','\n','center') # Phone app description
            self.t.image_create(END, image=self.photos[12]) # phone app image
            self.t.insert(END,f"\n\n")

            self.t.insert(END,self.iphones["content"][4],'heading','\n','center') # appstore heading
            self.t.insert(END,self.iphones["details"][4],'body','\n','center') # appstore description

            self.t.image_create(END, image=self.photos[13]) # appstore search image
            self.t.image_create(END, image=self.photos[14]) # appstore get image
            self.t.insert(END,f"\n\n")

            self.t.insert(END,self.iphones["content"][5],'heading','\n','center') # messages heading
            self.t.insert(END,self.iphones["details"][5],'body','\n','center') # messages description

            self.t.image_create(END, image=self.photos[15]) # imessage  image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.iphones["details"][6],'body','\n','center') # messages description
            self.t.image_create(END, image=self.photos[16]) # texting someone imessage image
            self.t.insert(END,f"\n\n")
            self.t.tag_add('center', '1.0', 'end')

        elif item_text == "Android phones":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.android_phones["content"][0],'heading','\n','center') # appstore heading
            self.t.insert(END,self.android_phones["details"][0],'body','\n','center') # appstore description
            self.t.image_create(END, image=self.photos[26]) # Android logo image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_phones["details"][1],'body','\n','center') # appstore description
            self.t.image_create(END, image=self.photos[25]) # Android screenshot one ui image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][1],'heading','\n','center') # navigation heading
            self.t.insert(END,self.android_phones["details"][2],'body','\n','center') # navigation desccription
            self.t.image_create(END, image=self.photos[28]) #  andorid app draw image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_phones["details"][3],'body','\n','center') # navigation desccription
            self.t.image_create(END, image=self.photos[29]) # android control centre image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][2],'heading','\n','center') # 4 main apps heading
            self.t.image_create(END, image=self.photos[27]) # main apps
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][3],'heading','\n','center') # chrome heading
            self.t.insert(END,self.android_phones["details"][4],'body','\n','center') # description of chrome heading
            self.t.image_create(END, image=self.photos[30]) # google chrome image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][4],'heading','\n','center') # Phone app heading
            self.t.insert(END,self.android_phones["details"][5],'body','\n','center') # phone app description
            self.t.image_create(END, image=self.photos[31]) # phone app image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_phones["details"][6],'body','\n','center') # desciption  of  keypad
            self.t.image_create(END, image=self.photos[32]) # keypad image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_phones["details"][7],'body','\n','center') # desciption of  contact 
            self.t.image_create(END, image=self.photos[33]) # add contact image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][5],'heading','\n','center') # Playstore heading
            self.t.insert(END,self.android_phones["details"][8],'body','\n','center') # play store desciption
            self.t.image_create(END, image=self.photos[35]) # playstore image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_phones["details"][9],'body','\n','center') # play store desciption
            self.t.image_create(END, image=self.photos[37]) # install app from playstore image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_phones["content"][6],'heading','\n','center') # Playstore heading
            self.t.insert(END,self.android_phones["details"][10],'body','\n','center') # play store desciption
            self.t.image_create(END, image=self.photos[38]) # messages image
            self.t.tag_add('center', '1.0', 'end')
        elif item_text == "Android tablets":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.android_tablets["content"][0],'heading','\n','center') # Heading of android tablet
            self.t.insert(END,self.android_tablets["details"][0],'body','\n','center') # description of an android ipad 
            self.t.image_create(END, image=self.photos[26]) # Android logo image
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[40]) # Android os on tablet logo
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["content"][1],'heading','\n','center') # Heading of android tablet
            self.t.insert(END,self.android_tablets["details"][1],'body','\n','center') # description of an android ipad 
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[41]) # Android swipe up for appdraw image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["details"][2],'body','\n','center') # use fingers to swipe
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[42]) # Android swipe down for control centre image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_tablets["content"][2],'heading','\n','center') # Heading of main apps for android tablet
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[43]) # Android 3 main apps
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_tablets["content"][3],'heading','\n','center')
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["details"][3],'body','\n','center')
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[44]) # Android playstore image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["details"][4],'body','\n','center')
            self.t.image_create(END, image=self.photos[45]) # Android playstore search image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["details"][5],'body','\n','center')# messages description
            self.t.image_create(END, image=self.photos[46]) # Android playstore install  image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.android_tablets["content"][4],'heading','\n','center')# Messages heading
            self.t.insert(END,self.android_tablets["details"][6],'body','\n','center')# messages description
            self.t.image_create(END, image=self.photos[47]) # Android messages image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.android_tablets["details"][7],'body','\n','center')# messages description
            self.t.image_create(END, image=self.photos[48]) # Android texting  image
            self.t.tag_add('center', '1.0', 'end')
        elif item_text =="Office 365":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.office_365["content"][0],'heading','\n','center') # Heading of android tablet
            self.t.insert(END,self.office_365["details"][0],'body','\n','center') # description of an android ipad 
            self.t.image_create(END, image=self.photos[52]) # Office icon image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.office_365["content"][1],'heading','\n','center') # Heading of android tablet
            self.t.insert(END,self.office_365["details"][1],'body','\n','center') # description of an android ipad 
            self.t.image_create(END, image=self.photos[49]) # word home screen image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.office_365["details"][2],'body','\n','center') # Change text colour 
            self.t.image_create(END, image=self.photos[50]) # colour palette image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.office_365["details"][3],'body','\n','center') # highlight colour 
            self.t.image_create(END, image=self.photos[51]) # highlight image

            self.t.image_create(END, image=self.photos[53]) # Save image
            self.t.insert(END,f"\n")
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.office_365["content"][2],'heading','\n','center') # heading of ontnote 

            self.t.insert(END,self.office_365["details"][4],'body','\n','center') # description of onenote
            self.t.image_create(END, image=self.photos[54]) # onenote homescreen image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.office_365["details"][5],'body','\n','center') # Select notebook 

            self.t.image_create(END, image=self.photos[55]) # make onenote image
            self.t.insert(END,f"\n") 
            self.t.insert(END,self.office_365["details"][6],'body','\n','center') # create section 
            self.t.image_create(END, image=self.photos[56]) # type name of  notebook image 
            self.t.insert(END,f"\n") 
            self.t.insert(END,self.office_365["details"][7],'body','\n','center') # create section 
            self.t.image_create(END, image=self.photos[55]) # make onenote image
            self.t.insert(END,f"\n") 
            self.t.insert(END,self.office_365["details"][8],'body','\n','center') # create section 
            self.t.image_create(END, image=self.photos[57]) # type in text in the notebook image
            self.t.insert(END,f"\n") 
            self.t.insert(END,self.office_365["details"][9],'body','\n','center') # create section
            self.t.image_create(END, image=self.photos[58]) # drag the text image
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.office_365["content"][3],'heading','\n','center') # heading of ontnote
            self.t.insert(END,self.office_365["details"][9],'body','\n','center') # create section 
            self.t.insert(END,f"\n") 
            self.t.image_create(END, image=self.photos[59]) # onedrive topbar image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.office_365["details"][10],'body','\n','center') # create section  
            self.t.image_create(END, image=self.photos[60]) # onedrive add/remove from device image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.office_365["details"][11],'body','\n','center') # create section
            self.t.tag_add('center', '1.0', 'end')
        elif item_text=="Printing":
            self.t.insert(END,"\n\n") 
            self.t.insert(END,self.printing["content"][0],'heading','\n','center') # Heading of android tablet
            self.t.insert(END,self.printing["details"][0],'body','','center') # description of an android ipad 
            self.t.insert(END,f"\n\n")
            self.t.insert(END,self.printing["details"][1],'body','\n','center') # description of an android ipad 
            self.t.image_create(END, image=self.photos[61]) # system prefes search image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.printing["details"][2],'body','\n','center') # description of an android ipad
            self.t.image_create(END, image=self.photos[62]) # add printer system pref image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.printing["details"][3],'body','\n','center') # description of an android ipad
            self.t.image_create(END, image=self.photos[63]) # windows search printer image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.printing["details"][4],'body','\n','center') # description of an android ipad
            self.t.image_create(END, image=self.photos[64]) # add printer windows image
            self.t.insert(END,f"\n")
            self.t.image_create(END, image=self.photos[65]) # connect printer windows image
            self.t.insert(END,f"\n")
            self.t.insert(END,self.printing["details"][5],'body','\n','center') # description of an android ipad
            self.t.image_create(END, image=self.photos[66]) # command+p image
            self.t.tag_add('center', '1.0', 'end')
        elif item_text in ["Chromebook", "Linux Ubuntu",'Servers', "School libraries","Counters",'Google suite']:
                self.t.insert(END,"\n\n") 
                self.t.insert(END,"Coming soon",'heading','\n','center')
                self.t.insert(END,f"\n")
                self.t.insert(END,"The option you have selected is currently not available at the moment. I am sorry for the inconvience :(",'body','\n','center')
                self.t.tag_add('center', '1.0', 'end')
        elif item_text=="Grey Scale Technology (3DIP)":
                    self.t.insert(END,"\n\n") 
                    self.t.insert(END,f"\n")
                    self.t.insert(END,"3DIP Grey Scale Technology",'heading')
                    self.t.insert(END,f"\n")
                    self.t.insert(END,"Welcome to Grey scale technologies where you can find and understand the basics of how to use technology from a business, educational, and personal standpoint.",'body','\n','center')
                    self.t.tag_add('center', '1.0', 'end')
        elif item_text in ["Chromebook", "Linux Ubuntu",'Servers', "School libraries","Counters",'Google suite']:
                self.t.insert(END,"Coming soon",'heading','\n','center')
                self.t.insert(END,f"\n")
                self.t.insert(END,"The option you have selected is currently not available at the moment. I am sorry for the inconvience :(",'body','\n','center')
                self.t.tag_add('center', '1.0', 'end')
        elif item_text=="Grey Scale Technology (3DIP)":
                    self.t.insert(END,f"\n")
                    self.t.insert(END,"3DIP Grey Scale Technology",'heading')
                    self.t.insert(END,f"\n")
                    self.t.insert(END,"Welcome to Grey scale technologies where you can find and understand the basics of how to use technology from a business, educational, and personal standpoint.",'body','\n','center')
                    self.t.tag_add('center', '1.0', 'end')

        
        # Configure scrollbar
        self.t.configure(yscrollcommand=self.content_scrollbar.set, state=tk.DISABLED) # does not allow editing
        self.content_scrollbar.config(command=self.t.yview) # configures scrollbar

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Program(root)
    root.mainloop()
