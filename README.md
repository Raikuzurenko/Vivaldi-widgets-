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
Paste the location in the box and click done, ***MAGIC!***

![iamge](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_17-15-47.png?raw=true)






#### Tips with Rai: After downloading the widgets I suggest making a dedicated folder for all the widgets so its easier to manage.



# Spotify and system resources

## Spotify widget 

![widgetspotify](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_16-04-12.png?raw=true)

This widget consists of two main parts:

- [html file](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/spotify-widget.html)

- [Local server](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/spotify-server.py)

  
The widgets setup is similar, for this the only difference is that it is dependant on the local server for it's info, to set up the local server, open a termianl and change directory to where the spotify-server.py file is and execute the following command "python3 spotify-server.py" and it should work

### Note this widget gets it's information from playerctl so install it if not present


## System resources

![image](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/readme_ss/2026-05-29_16-04-12.png?raw=true)

The setup process for this widget is the exact same just do "python3 sys_stats.py" in a terminal


### Note this widget gets its infomation from proc which is only on linux 






## Run on startup

You could technically use it as mentioned but turning your system on and constantly running the python command is annoying so I suggest making an sh file then making it executable and running it on startup ( just ask Chat GPT how to do that), I've linked my [sh](https://github.com/Raikuzurenko/Vivaldi-widgets-/blob/main/vivaldi_dark/start_widgets.sh) file just modify it with your directory :)


## Add custom CSS

Don't forget to add cutom [css](https://github.com/Raikuzurenko/Vivaldi-widgets-/tree/main/vivaldi_dark/vivaldi_css) to obtain the exact result of my setup


