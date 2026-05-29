# Vivaldi Widgets:
Sup, these are some widgets i made ( vibe coded, I'm lazy) I'll try me best to make the setup process as clear as I can, I just do this for fun so don't expect anything professional and bear with me, I'm literally looking up tutorials to learn how to format this instruction readme thing :P

## The following are the widgets included 
- Clock widget
- Pixel day progress
- Spotify widget
- System resources


Out of the 4 widgets the Clock and the Pixel day widget should work out of the box, the other 2 require some amount of set up.


## Setup

The setup process for all the widgets are pretty much the same ( additional steps for the spotify and system resources) as they all involve loading the widgets as lets say a mini website in vivaldi. For simiplicty sake I'll use the clock widget as an example to explain the setup process.

- ### Step 1 :P
Download the widget( if that wasn't obvious)

- ### Step 2
Copy the location of the widget, it should be soemthing like "/home/NAME/FOLDER/clock_widget.html"

- ### Step 3
Open vivaldi and click add widget and chosse the "***Webpage option***"

![image](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_16-48-27.png?raw=true)
![image](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_17-15-35.png?raw=true)

- ### Step 4
Paste the location in the box in the following format "file:///home/NAME/FOLDER/clock_widget.html" and click done, ***MAGIC!***

### Note: Don't forget to add file:// before the location of the widget

![iamge](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_17-15-47.png?raw=true)






#### Tips with Rai: After downloading the widgets I suggest making a dedicated folder for all the widgets so its easier to manage.



# Spotify and system resources

## Spotify widget 

![widgetspotify](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_16-04-12.png?raw=true)

This widget consists of two main parts:

- [html file](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/spotify-widget.html)

- [Local server](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/spotify-server.py)

  
The widgets setup is similar, for this the only difference is that it is dependant on the local server for it's info, to set up the local server, open a terminal and change directory to where the spotify-server.py file is and execute the following command "python3 spotify-server.py" and it should work

### Note this widget gets it's information from playerctl so install it if not present


## System resources

![image](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/screenshot-1780059298.png?raw=true)

The setup process for this widget is the exact same just do "python3 sys_stats.py" in a terminal


### Note this widget gets its infomation from proc which is only on linux 






## Run on startup

You could technically use it as mentioned but turning your system on and constantly running the python command is annoying so I suggest making an sh file then making it executable and running it on startup ( just ask Chat GPT how to do that), I've linked my [sh](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/start_widgets.sh) file just modify it with your directory :)


## Add custom CSS

Don't forget to add cutom [css](https://github.com/Raikuzurenko/Vivaldi-widgets-/tree/main/vivaldi_dark/vivaldi_css) to obtain the exact result of my setup

To add it just follow this guide I ripped of google

To add custom CSS to Vivaldi, you need to enable the experimental CSS modifications feature and point the browser to a specific folder on your computer where your .css files are stored.

### Step 1: Enable CSS Modifications
Open Vivaldi and type vivaldi://experiments into the address bar.Find the option labeled "Allow for using CSS modifications" and check the box.Restart Vivaldi for the change to take effect.

### Step 2: Prepare Your CSS Files
Create a new folder on your computer (e.g., in your Documents or a dedicated "VivaldiMods" folder) to store your custom styles.Create a new text file inside this folder, rename it to something like custom.css, and paste your CSS code into it.Note: Vivaldi will automatically load every .css file it finds in this selected folder.

### Step 3: Link the Folder to Vivaldi
Open Vivaldi Settings (Ctrl+F12 or Command+,).Navigate to the Appearance section.Scroll down to the Custom UI Modifications section.Click Select Folder (or "Add folder") and choose the folder you created in Step 2.Restart the browser once more to apply your custom styles.

### Note: Once you add the CSS, the setting option on the widgets will not be visible, they are there just click on it and youll eventually hit it :P
I
## Dancing girl widget(idk if anyone wants this :P)

Um the setup for this is similar and kinda stupid, just open a terminal and go into the folder where you've downloaded your GIF and just start a python web server that serves the download folder (or if you wanna be safer make another folder for this GIF only and serve that) by executing the command 
"python3 -m http.server 8000"
just change the port to any free port and in the file box paste "http://127.0.0.1:8000/dance.gif" replace the 8000 port number with your port that you chose earlier  and the "dance.gif" in the command with whatever name you saved the GIF as, you can also make it display images or videos , upto you lol. you could just ask chat gpt on how to make it auto start or just do what I do and start it every now and then whenever it breaks, its a janky setup but im lazy lowekey, regardless good luck if you have any problems, do ask and ill try and help as much as possible :)





