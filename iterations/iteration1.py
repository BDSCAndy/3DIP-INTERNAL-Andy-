import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Callback function to update the content in the second frame
def on_tree_select(event): # This method selects and loads the contentfame depending on what the user selects
    # Clear the content frame
    for widget in content_frame.winfo_children(): #This for loop destroys the content frame everytime the user has pressed on the items on treeview
        widget.destroy()
    
    # Get the selected item
    selected_item = tree.selection()[0] # This retries the first item selected from treeview and assigns it to selected variable
    item_text = tree.item(selected_item, "text") # This is what the selected item is. 
    
    if item_text == "Basic computing": # Instrucitons for basic computing
        computers = [
        "The most common types of operating systems that your PC could be using is Windows 10/11 or Mac OS.",
        "------------------------------------------------------------------------------------------------------------------\n"
        "To help identify your operating system, if you see a Windows icon at the bottom center or left of your icon, you are using Windows. If you see a Mac logo at the top left, then you are on Mac OS."
        ]
        label_basic = tk.Label(content_frame, text="Basic computing", font=("Arial", 40), wraplength=800)
        label_basic.pack(pady=(50,0),padx=(0,200))
        # Display the computers list in the content frame
        for information in computers:
            list_label = tk.Label(content_frame, text=information, font=("Arial", 16), wraplength=800)
            list_label.pack(padx=(0,200))
        # Load, resize, and convert the image
        image = Image.open('images/image1.png').resize((800,20))
        image2 = Image.open('images/image2.png').resize((800,30))
        image3=Image.open('images/image3.png').resize((800,90))
        image4=Image.open('images/image4.png').resize((800,30))
        image5=Image.open('images/image5.png').resize((500,331))

        photo = ImageTk.PhotoImage(image)
        photo2 = ImageTk.PhotoImage(image2)
        photo3 = ImageTk.PhotoImage(image3)
        photo4 = ImageTk.PhotoImage(image4)
        photo5 = ImageTk.PhotoImage(image5)

        # Display the image in a Label widget
        labeling_name = tk.Label(content_frame, text="Mac OS", font=("Arial", 24)) # Headings
        labeling_name.pack(padx=(0,200),pady=(0,10))

        label_image = tk.Label(content_frame, image=photo) # Image
        label_image.pack(padx=(0,200))
        label_image.image = photo
        
        labeling_name2 = tk.Label(content_frame, text="Windows",font=("Arial", 24)) # heading
        labeling_name2.pack(padx=(0,200))

        label_image2 = tk.Label(content_frame,image=photo2)
        label_image2.pack(padx=(0,200))
        label_image2.image = photo2
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,200))    #


        label_image3 = tk.Label(content_frame,text="How to open an app?",font=("Arial",24))
        label_image3.pack(pady=(0,0),padx=(0,200))

        label_image3_1 = tk.Label(content_frame,text="On the bottom of your screen press on the icons on the taskbar/dock The three main primary apps are web broswers like (Safari,MS Edge),Mailing apps and messaging apps",font=("Arial",16),wraplength=800)
        label_image3_1.pack(pady=(0,0),padx=(0,200))
        
        label_image3 = tk.Label(content_frame,image=photo3)
        label_image3.pack(pady=(0,0),padx=(0,200))
        label_image3.image = photo3

        label_image4 = tk.Label(content_frame,image=photo4)
        label_image4.pack(padx=(0,200),pady=(0,0))
        label_image4.image = photo4

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,200))    

        label_image4 = tk.Label(content_frame,text="How to search an app on Mac OS?",font=("Arial",24))
        label_image4.pack(pady=(0,0),padx=(0,200))

        
        label_image5 = tk.Label(content_frame,text="On Mac OS press command + space to open spotlight search",font=("Arial",16))
        label_image5.pack(pady=(20,0),padx=(0,200))

        label_image_img = tk.Label(content_frame, image=photo5)
        label_image_img.pack(padx=(0,250),pady=(10,0))
        label_image_img.image = photo5
        
        label_image5_1 = tk.Label(content_frame,text="The most used apps on PC/MAC is internet broswers like safari/Microsoft edge, Mail,MS store/appstore, office 365/apple office suite(keynote,pages) etc.",font=("Arial",16),wraplength=800)
        label_image5_1.pack(pady=(20,0),padx=(0,200))

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,200))  

        label_image4 = tk.Label(content_frame,text="How to search an app on windows?",font=("Arial",24))
        label_image4.pack(pady=(0,0),padx=(0,200))

        label_instruct=tk.Label(content_frame,text="Press the windows key and type in the app/file you want to open",font=("Arial",16))
        label_instruct.pack(padx=(0,200))
        image8=Image.open('images/image8.png').resize((500,431))
        photo8 = ImageTk.PhotoImage(image8)

        label_image8 = tk.Label(content_frame, image=photo8)
        label_image8.pack(padx=(0,200),pady=(0,0))
        label_image8.image = photo8

    elif item_text == "Grey Scale Technology (3DIP)":
        label_greyscale = tk.Label(content_frame, text="Grey Scale technolgoy (3DIP)", font=("Arial", 40), wraplength=800)
        label_greyscale.pack(pady=(50,0),padx=(10,0))

        list_label_greyscale = tk.Label(content_frame, text="Welcome to Grey scale technologies where you can find and understand the basics of how to use technology from a business, educational, and personal standpoint.", font=("Arial", 16), wraplength=700)
        list_label_greyscale.pack(padx=(0))  # Adjust this value to move the label further down

    elif item_text =="Ipads": # Shows instructions on how to use an iPad
        image6=Image.open('images/image6.png').resize((450,331))
        photo6 = ImageTk.PhotoImage(image6)

        image7=Image.open('images/image7.png').resize((600,401))
        photo7 = ImageTk.PhotoImage(image7)

        image23=Image.open('images/image23.png').resize((600,401))
        photo23= ImageTk.PhotoImage(image23)

        image24=Image.open('images/image24.png').resize((600,401))
        photo24= ImageTk.PhotoImage(image24)

        image25=Image.open('images/image25.png').resize((600,401))
        photo25= ImageTk.PhotoImage(image25)


        label2 = tk.Label(content_frame, text="Ipads", font=("Arial", 40), wraplength=800)
        label2.pack(pady=(20,0),padx=(0,0))

        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  
        list_label = tk.Label(content_frame, text="The purpose of an Ipad is that it can be used as a tablet or a replacement laptop. A tablet is essentially a smartphone but bigger in size. Why users would want a tablet is its protable while still having a larger screen reesate compared to phones with the power of pc/laptops", font=("Arial", 16), wraplength=800)
        list_label.pack(padx=(0,0))

        label_image6 = tk.Label(content_frame, image=photo6)
        label_image6.pack()
        label_image6.image = photo6

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        list_labelu = tk.Label(content_frame, text="You can use  1-2 fingers to swipe between app pages", font=("Arial", 16), wraplength=800)
        list_labelu.pack(padx=(0,0))
        
        label_image7 = tk.Label(content_frame, image=photo7)
        label_image7.pack(padx=(0,0),pady=(0,0))
        label_image7.image = photo7

        list_labeluu = tk.Label(content_frame, text="If you keep swiping right eventually you will reach the appdraw", font=("Arial", 16), wraplength=800)
        list_labeluu.pack(padx=(0,0))
        
        label_image23 = tk.Label(content_frame, image=photo23)
        label_image23.pack(padx=(0,0),pady=(0,0))
        label_image23.image = photo23 

        list_labeluu = tk.Label(content_frame, text="If you go back to the homescreen and swipedown with 1-2 fingers you can open search", font=("Arial", 16), wraplength=800)
        list_labeluu.pack(padx=(0,0))
        
        label_image25 = tk.Label(content_frame, image=photo25)
        label_image25.pack(padx=(0,0),pady=(0,0))
        label_image25.image = photo25

        list_labeluu = tk.Label(content_frame, text="If you swipt up you can open the appswitcher", font=("Arial", 16), wraplength=800)
        list_labeluu.pack(padx=(0,0))

        label_image24 = tk.Label(content_frame, image=photo24)
        label_image24.pack(padx=(0,0),pady=(0,0))
        label_image24.image = photo24
 
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        label_phone = tk.Label(content_frame, text="The four mains apps you need to learn inorder to use an iphone are:", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(10,0))

        image19=Image.open('images/image19.png').resize((400,101))
        photo19 = ImageTk.PhotoImage(image19)

        label_image19 = tk.Label(content_frame, image=photo19)
        label_image19.pack(padx=(0,0),pady=(0,0))
        label_image19.image = photo19

        #-----------------------
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        label_phone = tk.Label(content_frame, text="How to use Safari", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        
        label_phone_ipad = tk.Label(content_frame, text="Simply press on the topbar then search!", font=("Arial", 16), wraplength=800)
        label_phone_ipad.pack(pady=(0,0),padx=(0,0))
        
        image18=Image.open('images/image18.png').resize((500,400))
        photo18= ImageTk.PhotoImage(image18)

        label_image18 = tk.Label(content_frame, image=photo18)
        label_image18.pack(padx=(0,0),pady=(0,0))
        label_image18.image = photo18

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))      

        label_phone_facetime = tk.Label(content_frame, text="Facetime", font=("Arial", 40), wraplength=800)
        label_phone_facetime.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="Make sure you have a contact added and click on there profile to start a call", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image20=Image.open('images/image20.png').resize((500,400))
        photo20= ImageTk.PhotoImage(image20)

        label_image20 = tk.Label(content_frame, image=photo20)
        label_image20.pack(padx=(0,0),pady=(0,0))
        label_image20.image = photo20

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))      
    
        
        label_phone = tk.Label(content_frame, text="Appstore", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="Essentailly there are 4 options, There are favourites,recents,contacts,keypads, and voice mails", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image21=Image.open('images/image21.png').resize((500,400))
        photo21= ImageTk.PhotoImage(image21)

        label_image21 = tk.Label(content_frame, image=photo21)
        label_image21.pack(padx=(0,0),pady=(0,0))
        label_image21.image = photo21

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))    

        label_phone = tk.Label(content_frame, text="Messages", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="In order to send text do ", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image26=Image.open('images/image26.png').resize((500,400))
        photo26= ImageTk.PhotoImage(image26)

        label_image26 = tk.Label(content_frame, image=photo26)
        label_image26.pack(padx=(0,0),pady=(0,0))
        label_image26.image = photo26

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))    


    elif item_text=="iPhones": # Shows instructions on how to use an iphone

        label_phone = tk.Label(content_frame, text="Iphone", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(10,0),padx=(0,0))

        label_phone_info = tk.Label(content_frame, text="An iPhone is an Apple product used to make phone calls and communicate with others", font=("Arial", 16), wraplength=800)
        label_phone_info.pack(pady=(10,0),padx=(0,0))
        

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        image10=Image.open('images/image10.png').resize((400,400))
        photo10= ImageTk.PhotoImage(image10)

        label_image10 = tk.Label(content_frame, image=photo10)
        label_image10.pack(padx=(0,0),pady=(0,0))
        label_image10.image = photo10

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        label_phone = tk.Label(content_frame, text="Main", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="The four mains apps you need to learn inorder to use an iphone are:", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image9=Image.open('images/image9.png').resize((400,101))
        photo9 = ImageTk.PhotoImage(image9)

        label_image9 = tk.Label(content_frame, image=photo9)
        label_image9.pack(padx=(0,0),pady=(0,0))
        label_image9.image = photo9
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))          

        
        label_phone = tk.Label(content_frame, text="How to use Safari", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0)) 

        label_phone = tk.Label(content_frame, text="Simply tap on the bar at the bottom of the app and search for a website or keywords and press enter", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image12=Image.open('images/image12.png').resize((350,200))
        photo12= ImageTk.PhotoImage(image12)

        label_image12 = tk.Label(content_frame, image=photo12)
        label_image12.pack(padx=(0,0),pady=(0,0))
        label_image12.image = photo12

        
        image11=Image.open('images/image11.png').resize((200,400))
        photo11= ImageTk.PhotoImage(image11)

        label_image11 = tk.Label(content_frame, image=photo11)
        label_image11.pack(padx=(0,0),pady=(0,0))
        label_image11.image = photo11

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))      

        label_phone = tk.Label(content_frame, text="Phone app", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="Essentailly there are 4 options, There are favourites,recents,contacts,keypads, and voice mails. The image shown below is the keypad where you can dial any number.", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image13=Image.open('images/image13.png').resize((700,427))
        photo13= ImageTk.PhotoImage(image13)

        label_image13 = tk.Label(content_frame, image=photo13)
        label_image13.pack(padx=(0,0),pady=(0,0))
        label_image13.image = photo13

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))      
        
        label_phone = tk.Label(content_frame, text="Appstore", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="To navigate throughout the appstore look at the bottom bars given", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image14=Image.open('images/image14.png').resize((400,320))
        photo14= ImageTk.PhotoImage(image14)

        label_image14 = tk.Label(content_frame, image=photo14)
        label_image14.pack(padx=(0,0),pady=(0,0))
        label_image14.image = photo14

        image15=Image.open('images/image15.png').resize((400,350))
        photo15= ImageTk.PhotoImage(image15)

        label_image15 = tk.Label(content_frame, image=photo15)
        label_image15.pack(padx=(0,0),pady=(0,0))
        label_image15.image = photo15


        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))    

        label_phone = tk.Label(content_frame, text="Messages", font=("Arial", 40), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        label_phone = tk.Label(content_frame, text="Click on one of the contacts or add one", font=("Arial", 16), wraplength=800)
        label_phone.pack(pady=(0,0),padx=(0,0))

        image16=Image.open('images/image16.png').resize((350,427))
        photo16= ImageTk.PhotoImage(image16)


        label_image16 = tk.Label(content_frame, image=photo16)
        label_image16.pack(padx=(0,0),pady=(0,0))
        label_image16.image = photo16

        label_phone_2 = tk.Label(content_frame, text="In order to send a message press on the box", font=("Arial", 16), wraplength=800)
        label_phone_2.pack(pady=(0,0),padx=(0,0))

        image17=Image.open('images/image17.png').resize((350,257))
        photo17= ImageTk.PhotoImage(image17)

        label_image17 = tk.Label(content_frame, image=photo17)
        label_image17.pack(padx=(0,0),pady=(0,0))
        label_image17.image = photo17



        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

    elif item_text=="Android phones": #Shows instructions on how to use android phone
        label_anphone = tk.Label(content_frame, text="Android Phone", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="An android phone is a device that can help connect and communicate with others online. Android is an operating system developed by google which are found on devices such as Samsusng, Google(pixel), Oppo, Nothing and more", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image28=Image.open('images/image28.png').resize((150,150))
        photo28= ImageTk.PhotoImage(image28)

        label_image28 = tk.Label(content_frame, image=photo28)
        label_image28.pack(padx=(0,0),pady=(0,0))
        label_image28.image = photo28

        image27=Image.open('images/image27.png').resize((300,607))
        photo27= ImageTk.PhotoImage(image27)

        label_anphone_2 = tk.Label(content_frame, text="All devices that use android have there own look to it. An example of this is Samsusngs One UI", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        label_image27 = tk.Label(content_frame, image=photo27)
        label_image27.pack(padx=(0,0),pady=(0,0))
        label_image27.image = photo27

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  
        label_anphone = tk.Label(content_frame, text="How to navigate your android phone", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))
        
        label_anphone_2 = tk.Label(content_frame, text="Swipe down to open the appdraw(location of the rest of your apps)", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))


        image30=Image.open('images/image30.png').resize((600,551))
        photo30= ImageTk.PhotoImage(image30)

        label_image30 = tk.Label(content_frame, image=photo30)
        label_image30.pack(padx=(0,0),pady=(0,0))
        label_image30.image = photo30

        label_anphone_2 = tk.Label(content_frame, text="Swipe down to open the control centre(location of the rest of your apps)", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image31=Image.open('images/image31.png').resize((600,551))
        photo31= ImageTk.PhotoImage(image31)

        label_image31 = tk.Label(content_frame, image=photo31)
        label_image31.pack(padx=(0,0),pady=(0,0))
        label_image31.image = photo31



        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        label_anphone = tk.Label(content_frame, text="Main apps used on android", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        
        image29=Image.open('images/image29.png').resize((400,101))
        photo29= ImageTk.PhotoImage(image29)

        label_image29 = tk.Label(content_frame, image=photo29)
        label_image29.pack(padx=(0,0),pady=(0,0))
        label_image29.image = photo29

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))  

        label_anphone = tk.Label(content_frame, text="How to use Google chrome", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))
             
        label_anphone_2 = tk.Label(content_frame, text="Launch the app and tap and tap on the bar that says search or type URL (Uniform Resource Locator)", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image32=Image.open('images/image32.png').resize((300,601))
        photo32= ImageTk.PhotoImage(image32)

        label_image32= tk.Label(content_frame, image=photo32)
        label_image32.pack(padx=(0,0),pady=(0,0))
        label_image32.image = photo32

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0)) 

        label_anphone = tk.Label(content_frame, text="How to use phone app", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="There are 3 main features in the phone app being recent, keypad(manually dialing a number) and contacts(peoples number you added)", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image33=Image.open('images/image33.png').resize((300,601))
        photo33= ImageTk.PhotoImage(image33)

        label_image33= tk.Label(content_frame, image=photo33)
        label_image33.pack(padx=(0,0),pady=(0,0))
        label_image33.image = photo33

        label_anphone_2 = tk.Label(content_frame, text="Keypad", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image34=Image.open('images/image34.png').resize((300,601))
        photo34= ImageTk.PhotoImage(image34)

        label_image34= tk.Label(content_frame, image=photo34)
        label_image34.pack(padx=(0,0),pady=(0,0))
        label_image34.image = photo34

        label_anphone_2 = tk.Label(content_frame, text="In order to add a contact press + button at the top right:", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image35=Image.open('images/image35.png').resize((600,601))
        photo35= ImageTk.PhotoImage(image35)

        label_image35= tk.Label(content_frame, image=photo35)
        label_image35.pack(padx=(0,0),pady=(0,0))
        label_image35.image = photo35

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0)) 

        label_anphone = tk.Label(content_frame, text="How to use playstore", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image37=Image.open('images/image37.png').resize((600,601))
        photo37= ImageTk.PhotoImage(image37)

        label_image37= tk.Label(content_frame, image=photo37)
        label_image37.pack(padx=(0,0),pady=(0,0))
        label_image37.image = photo37

        label_anphone_2 = tk.Label(content_frame, text="Press the install button", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image39=Image.open('images/image39.png').resize((300,601))
        photo39= ImageTk.PhotoImage(image39)

        label_image39= tk.Label(content_frame, image=photo39)
        label_image39.pack(padx=(0,0),pady=(0,0))
        label_image39.image = photo39
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0)) 

        label_anphone = tk.Label(content_frame, text="How to use Messages", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Make sure to have added contacts earlier", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image40=Image.open('images/image40.png').resize((600,601))
        photo40= ImageTk.PhotoImage(image40)

        label_image40= tk.Label(content_frame, image=photo40)
        label_image40.pack(padx=(0,0),pady=(0,0))
        label_image40.image = photo40

        label_anphone_2 = tk.Label(content_frame, text="Begin texting", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0)) 
    elif item_text=="Android tablets": #shows instructions for android tablets
        label_anphone = tk.Label(content_frame, text="Android tablet", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="An android tablet  similar to a phone but bigger is a device that can help connect and communicate with others online. Android is an operating system developed by google which are found on devices such as Samsusng, Google(pixel), Oppo, Nothing and more", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image28=Image.open('images/image28.png').resize((150,150))
        photo28= ImageTk.PhotoImage(image28)

        label_image28 = tk.Label(content_frame, image=photo28)
        label_image28.pack(padx=(0,0),pady=(0,0))
        label_image28.image = photo28

        image42=Image.open('images/image42.png').resize((600,401))
        photo42= ImageTk.PhotoImage(image42)

        label_image42= tk.Label(content_frame, image=photo42)
        label_image42.pack(padx=(0,0),pady=(0,0))
        label_image42.image = photo42
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0)) 

        label_anphone = tk.Label(content_frame, text="How to navigate your android tablet.", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Just like an android phone use fingers to swipe up to access the app draw", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        
        image43=Image.open('images/image43.png').resize((600,401))
        photo43= ImageTk.PhotoImage(image43)

        label_image43= tk.Label(content_frame, image=photo43)
        label_image43.pack(padx=(0,0),pady=(0,0))
        label_image43.image = photo43

        label_anphone_2 = tk.Label(content_frame, text=" Use fingers to swipe down to access the control centre", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image44=Image.open('images/image44.png').resize((600,251))
        photo44= ImageTk.PhotoImage(image44)

        label_image44= tk.Label(content_frame, image=photo44)
        label_image44.pack(padx=(0,0),pady=(0,0))
        label_image44.image = photo44

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        label_anphone = tk.Label(content_frame, text="Main apps used on android", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        
        image45=Image.open('images/image45.png').resize((400,101))
        photo45= ImageTk.PhotoImage(image45)

        label_image45 = tk.Label(content_frame, image=photo45)
        label_image45.pack(padx=(0,0),pady=(0,0))
        label_image45.image = photo45

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))
    
        label_anphone = tk.Label(content_frame, text="How to use Google playstore", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Tap on the topbar to search for the app you want to install", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))
    
        image46=Image.open('images/image46.png').resize((700,300))
        photo46= ImageTk.PhotoImage(image46)

        label_image46 = tk.Label(content_frame, image=photo46)
        label_image46.pack(padx=(0,0),pady=(0,0))
        label_image46.image = photo46

        label_anphone_2 = tk.Label(content_frame, text="Search for the app", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image47=Image.open('images/image47.png').resize((700,300))
        photo47= ImageTk.PhotoImage(image47)

        label_image47 = tk.Label(content_frame, image=photo47)
        label_image47.pack(padx=(0,0),pady=(0,0))
        label_image47.image = photo47

        label_anphone_2 = tk.Label(content_frame, text="Press on the app you want and press the install button", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image48=Image.open('images/image48.png').resize((700,300))
        photo48= ImageTk.PhotoImage(image48)

        label_image48 = tk.Label(content_frame, image=photo48)
        label_image48.pack(padx=(0,0),pady=(0,0))
        label_image48.image = photo48
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        label_anphone = tk.Label(content_frame, text="How to use messages", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Make sure you have contacts added to messages", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image49=Image.open('images/image49.png').resize((700,300))
        photo49= ImageTk.PhotoImage(image49)

        label_image49 = tk.Label(content_frame, image=photo49)
        label_image49.pack(padx=(0,0),pady=(0,0))
        label_image49.image = photo49

        label_anphone_2 = tk.Label(content_frame, text="Then tap on the chatbar and start typing and return it to send!", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image50=Image.open('images/image50.png').resize((700,300))
        photo50= ImageTk.PhotoImage(image50)

        label_image50 = tk.Label(content_frame, image=photo50)
        label_image50.pack(padx=(0,0),pady=(0,0))
        label_image50.image = photo50

    elif item_text=="Office 365": #Shows instructions for office 365
        label_anphone = tk.Label(content_frame, text="Office 365", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        
        label_anphone_2 = tk.Label(content_frame, text="Office 365 is a subscription-based service from Microsoft that provides access to various productivity tools like Word, Excel, PowerPoint, and cloud services like OneDrive and Outlook.", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))


        image54=Image.open('images/image54.png').resize((150,150))
        photo54= ImageTk.PhotoImage(image54)

        label_image54 = tk.Label(content_frame, image=photo54)
        label_image54.pack(padx=(0,0),pady=(0,0))
        label_image54.image = photo54

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        label_anphone = tk.Label(content_frame, text="How to use Microsoft word", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Microsoft Word is a word processing software developed by Microsoft, used for creating, editing, and formatting text documents. Begin by pressing the create button", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

       
        image51=Image.open('images/image51.png').resize((800,400))
        photo51= ImageTk.PhotoImage(image51)

        label_image51 = tk.Label(content_frame, image=photo51)
        label_image51.pack(padx=(0,0),pady=(0,0))
        label_image51.image = photo51

        label_anphone_2 = tk.Label(content_frame, text="This can change text colour", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image52=Image.open('images/image52.png').resize((220,300))
        photo52= ImageTk.PhotoImage(image52)

        label_image52 = tk.Label(content_frame, image=photo52)
        label_image52.pack(padx=(0,0),pady=(0,0))
        label_image52.image = photo52

        label_anphone_2 = tk.Label(content_frame, text="Highlight text press on this icon", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image53=Image.open('images/image53.png').resize((220,200))
        photo53= ImageTk.PhotoImage(image53)

        label_image53 = tk.Label(content_frame, image=photo53)
        label_image53.pack(padx=(0,0),pady=(0,0))
        label_image53.image = photo53


        image55=Image.open('images/image55.png').resize((800,400))
        photo55= ImageTk.PhotoImage(image55)

        label_image55 = tk.Label(content_frame, image=photo55)
        label_image55.pack(padx=(0,0),pady=(0,0))
        label_image55.image = photo55


        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        label_anphone = tk.Label(content_frame, text="How to use Onenote", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        
        label_anphone_2 = tk.Label(content_frame, text="OneNote is a digital note-taking application developed by Microsoft that allows users to organize notes, drawings, and other content into notebooks.", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        
        image56=Image.open('images/image56.png').resize((800,400))
        photo56= ImageTk.PhotoImage(image56)

        label_image56 = tk.Label(content_frame, image=photo56)
        label_image56.pack(padx=(0,0),pady=(0,0))
        label_image56.image = photo56

        label_anphone_2 = tk.Label(content_frame, text="Press add notebook", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))
        
        image57=Image.open('images/image57.png').resize((250,300))
        photo57= ImageTk.PhotoImage(image57)

        label_image57 = tk.Label(content_frame, image=photo57)
        label_image57.pack(padx=(0,0),pady=(0,0))
        label_image57.image = photo57

        
        label_anphone_2 = tk.Label(content_frame, text="Select the colour,name and location of your notebook and press create", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        
        image58=Image.open('images/image58.png').resize((800,400))
        photo58= ImageTk.PhotoImage(image58)

        label_image58 = tk.Label(content_frame, image=photo58)
        label_image58.pack(padx=(0,0),pady=(0,0))
        label_image58.image = photo58

           
        label_anphone_2 = tk.Label(content_frame, text="Create a section and page if you have not already and start typing", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        
        image59=Image.open('images/image59.png').resize((800,400))
        photo59= ImageTk.PhotoImage(image59)

        label_image59 = tk.Label(content_frame, image=photo59)
        label_image59.pack(padx=(0,0),pady=(0,0))
        label_image59.image = photo59

        
           
        label_anphone_2 = tk.Label(content_frame, text="You can drag and drop images, and drag the text and images around the notebook", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image60=Image.open('images/image60.png').resize((800,400))
        photo60= ImageTk.PhotoImage(image60)

        label_image60 = tk.Label(content_frame, image=photo60)
        label_image60.pack(padx=(0,0),pady=(0,0))
        label_image60.image = photo60

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))


        label_anphone = tk.Label(content_frame, text="How to use Onedrive", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(10,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="OneDrive is a cloud storage service provided by Microsoft that allows users to store, share, and access files and documents from anywhere with an internet connection.\n On the taskbar icons on windows/mac you can check if your files are synced (assumming you have already setup onedrive)", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

         
        image61=Image.open('images/image61.png').resize((200,400))
        photo61= ImageTk.PhotoImage(image61)

        label_image61 = tk.Label(content_frame, image=photo61)
        label_image61.pack(padx=(0,0),pady=(0,0))
        label_image61.image = photo61

        label_anphone_2 = tk.Label(content_frame, text="In the onedrive folder you can drag and drop files into the folder and it will automatically sync to the onedrive online. You can also free up space or keep the file on your pc by right clicking on the file", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image62=Image.open('images/image62.png').resize((800,500))
        photo62= ImageTk.PhotoImage(image62)

        label_image62 = tk.Label(content_frame, image=photo62)
        label_image62.pack(padx=(0,0),pady=(0,0))
        label_image62.image = photo62
         
        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="More will  office 365 apps will be added in the future", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

    elif item_text=="Printing": #Shows insturctions for printing
        label_anphone = tk.Label(content_frame, text="Printing", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(20,0),padx=(0,0))

        label_anphone_2 = tk.Label(content_frame, text="Printing is needed to make physical copies of information, ensuring it's accessible, shareable, and durable.", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))

        
        label_anphone_2 = tk.Label(content_frame, text="Open system preferences", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))
        
        image63=Image.open('images/image63.png').resize((450,380))
        photo63= ImageTk.PhotoImage(image63)

        label_image63 = tk.Label(content_frame, image=photo63)
        label_image63.pack(padx=(0,0),pady=(0,0))
        label_image63.image = photo63

        label_anphone_2 = tk.Label(content_frame, text="Press the + button at the bottom left to add a printer and then select the printer you want to add", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))
          
        image64=Image.open('images/image64.png').resize((450,350))
        photo64= ImageTk.PhotoImage(image64)

        label_image64 = tk.Label(content_frame, image=photo64)
        label_image64.pack(padx=(0,0),pady=(0,0))
        label_image64.image = photo64

        label_anphone_2 = tk.Label(content_frame, text="Search for the printer you want and add press the add button device button", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))
          
        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))


        label_anphone_2 = tk.Label(content_frame, text="On windows press the windows key and search for printer", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image66=Image.open('images/image66.png').resize((450,350))
        photo66= ImageTk.PhotoImage(image66)

        label_image66 = tk.Label(content_frame, image=photo66)
        label_image66.pack(padx=(0,0),pady=(0,0))
        label_image66.image = photo66

        label_anphone_2 = tk.Label(content_frame, text="Press the add device button for you chosen printer", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))


        image67=Image.open('images/image67.png').resize((650,180))
        photo67= ImageTk.PhotoImage(image67)

        label_image67 = tk.Label(content_frame, image=photo67)
        label_image67.pack(padx=(0,0),pady=(0,0))
        label_image67.image = photo67


        image68=Image.open('images/image68.png').resize((650,350))
        photo68= ImageTk.PhotoImage(image68)

        label_image68 = tk.Label(content_frame, image=photo68)
        label_image68.pack(padx=(0,0),pady=(0,0))
        label_image68.image = photo68

        underline = tk.Label(content_frame, text="------------------------------------------------------------------------------------------------------------------\n",font=("Arial", 16), wraplength=800)
        underline.pack(padx=(0,0))


        label_anphone_2 = tk.Label(content_frame, text="In order to print e.g. word documents,txt files,pdf or images usually you have to find the print button in the app or use shortcuts like command/control + p", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(0,0))

        image69=Image.open('images/image69.png').resize((650,380))
        photo69= ImageTk.PhotoImage(image69)

        label_image69 = tk.Label(content_frame, image=photo69)
        label_image69.pack(padx=(0,0),pady=(0,0))
        label_image69.image = photo69
    elif item_text in ["Chromebook", "Linux Ubuntu/Server", "School libraries","Counters"]:# Tutorials which I have not added yet
        label_anphone_2 = tk.Label(content_frame, text="Coming soon!", font=("Arial", 40), wraplength=800) # Messages to let the user know i have not added it yet
        label_anphone_2.pack(pady=(0,0),padx=(50,0))
        label_anphone_2 = tk.Label(content_frame, text="The option you have selected is currently not available at the moment. I am sorry for the inconvience :(", font=("Arial", 16), wraplength=800)
        label_anphone_2.pack(pady=(0,0),padx=(50,0))
    elif item_text=="Personal":# heading for perosnal tehcnolgoy
        label_anphone = tk.Label(content_frame, text="Personal technology", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(20,0),padx=(150,0))
           
    elif item_text=="Education": #heading for educational technolgy
        label_anphone = tk.Label(content_frame, text="Educational technology", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(20,0),padx=(150,0))
    elif item_text=='Business': #headings for business technology
        label_anphone = tk.Label(content_frame, text="Business technology", font=("Arial", 40), wraplength=800)
        label_anphone.pack(pady=(20,0),padx=(150,0))
           
# Create the main window
root = tk.Tk()
root.title("Grey Scale technology")
root.geometry("1440x900")

# Create a canvas for the content frame
content_canvas = tk.Canvas(root) # This is used for scrolling
content_frame = tk.Frame(content_canvas) # The canvas goes inside the frame 
content_scrollbar = tk.Scrollbar(root, orient="vertical", command=content_canvas.yview) # allows scrolling

# Place the canvas and scrollbar in the root window
content_canvas.create_window((230, 0), window=content_frame, anchor="nw") #This helps asign the postion and width of the canvas
content_canvas.configure(yscrollcommand=content_scrollbar.set)# Allows scrolling

# Pack the widgets
tree_frame = tk.Frame(root, width=320, height=720) # The frame that holds the tree view
tree_frame.pack(side="left", fill="y") # position the tree view to the left

content_scrollbar.pack(side="right", fill="y") # positon the scrollbar to the right
content_canvas.pack(side="right", fill="both", expand=True)

# Update the canvas scroll region
def on_frame_configure(event):# Allows the scrollbar to be anywhere
    content_canvas.configure(scrollregion=content_canvas.bbox("all"))
content_frame.bind("<Configure>", on_frame_configure) #Helps adjust scrollregion when the frame is resized

# Create a Treeview widget
tree = ttk.Treeview(tree_frame) # The treeview
tree.pack(fill="both", expand=True)

# Bind the tree view select event to the callback function
tree.bind("<<TreeviewSelect>>", on_tree_select) #This is triggered when the user selects an item and on_tree_select is run

# Insert a root item
root_item = tree.insert("", "end", text="Grey Scale Technology (3DIP)")

# Insert child items
child1_item = tree.insert(root_item, "end", text="Personal")
child2_item = tree.insert(root_item, "end", text="Business")
child3_item = tree.insert(root_item, "end", text="Education")

# Insert sub-child items
tree.insert(child1_item, "end", text="Basic computing")
tree.insert(child1_item, "end", text="Ipads")
tree.insert(child1_item, "end", text="iPhones")
tree.insert(child1_item, "end", text="Android phones")
tree.insert(child1_item, "end", text="Android tablets")

tree.insert(child2_item, "end", text="Basic computing")
tree.insert(child2_item, "end", text="Office 365")
tree.insert(child2_item, "end", text="Printing")
tree.insert(child2_item, "end", text="Linux Ubuntu/Server")
tree.insert(child2_item, "end", text="Counters")

tree.insert(child3_item, "end", text="Basic computing")
tree.insert(child3_item, "end", text="Printing")
tree.insert(child3_item, "end", text="Chromebook")
tree.insert(child3_item, "end", text="School libraries")

# Expand the all the item
tree.item(root_item, open=True)
tree.item(child1_item, open=True)
tree.item(child2_item, open=True)
tree.item(child3_item, open=True)
tree.selection_set(root_item)

# Start the tkinter event loop
root.mainloop()
