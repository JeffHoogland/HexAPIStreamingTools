# Hex API Streaming Tools

This is a collection of python scripts and a pyside GUI that tie into the [HexTCG](https://www.hextcg.com/) client side API to provide added value for twitch streams.

![alt text](http://i.imgur.com/W3qNu2f.png "Hex API Dashboard")

![alt text](http://i.imgur.com/w9zNNNi.png "StackIt Decklist Export")

By: [Jeff Hoogland](http://www.jeffhoogland.com/)

# Installation

* Install [Python 2.7](https://www.python.org/downloads/) 
* Install [Pip](https://pip.pypa.io/en/stable/installing/)
* Download the [latest source code](https://github.com/JeffHoogland/HexAPIStreamingTools/archive/master.zip)
* Extract and Navigate to the source code directory and run: *pip install -r requirements.txt*
* Run: *python MainWindow.py*

# Configuration

* From the menu select *Setup->Add API entry*
* If your api.ini file is not automatically located, navigate to the directory where your Hex is installed using the file selector
* Click "Add Listener to Hex's api.ini" (You will need to restart Hex if it is running)
* Click "Start API Listener"

# Usage

While the Listener is running decklists will automatically be populated in your output directory whenever you save a decklist in game. 
You can point your streaming software, such as OBS, to the *LastDeckExport.png* image. This is updated every time you save a new deck.

# Trouble Shooting

If the Listener starts, but does not seem to be getting any data, check your [firewall settings](https://github.com/JeffHoogland/HexAPIStreamingTools/wiki/Configuring-Windows-Firewall-with-API-Tools).
