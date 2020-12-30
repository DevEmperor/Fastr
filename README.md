[![asciicast](https://asciinema.org/a/381831.svg)](https://asciinema.org/a/381831)



# Fastr

**Small python script to transcribe speech**

- Written with Python 3.9.1
- Compatible with all **Linux** distributions



# Installation

### Linux

1. Clone this git-repository:

   `git clone https://github.com/DevEmperor/Fastr.git`

   

2. Make sure Python3 is installed:

   `python3 --version`
   
   If you get something like `Python 3.*.*` you have Python3 installed.
   
   If you don't have Python3 installed, you can find it in your packet-manager.
   
   
   
3. Install **Python3-Pandas** and **Python3-PyAudio** with your packet-manager from your terminal. On Debian-based systems this would be:

   `sudo apt-get install python3-pandas python3-pyaudio`

   On other systems this can easily be done by using either the systems packet-manager or using ***pip***:

   `pip3 install pandas pyaudio`

   

4. Install the "**SpeechRecognition**"-package using pip:

   `pip3 install SpeechRecognition`



# Usage

After going into the "fastr"-directory, simply type

`python3 fastr.py`

You'll get asked whether you want to choose your microphone manually. If you want to use your default input device, just hit *ENTER* (this will use the default answer which is in this case "NO"). Otherwise you can select the microphone of your choice by typing the number of the input device.

If you want to transcribe in another language than English, you now need to specify the language code. A list of all languages that the recognition engine understands, can be found [here](https://cloud.google.com/speech-to-text/docs/languages).

If you don't want Fastr to copy the result immediately to your clipboard, type "no" now. Otherwise just hit *ENTER*.



Now press any key to start the recording. **Fastr will record everything you say until he cannot understand any speech for more than 2 seconds.**

After Fastr printed the recognized text, you can simply hit *ENTER* again, to restart the recording/recognition. If you want the program to stop, type "no". 



# About

<u>I programmed Fastr to submit answers faster in online classes.</u> Therefore Fastr is especially optimized for speed and through the interactive use very simple but still really effective. Of course, Fastr can also be used for other purposes, such as quickly dictating WhatsApp messages in an Android emulator.



# License

Fastr is under the terms of the [Apapche 2.0 license](https://www.apache.org/licenses/LICENSE-2.0), following all clarifications stated in the [license file](https://raw.githubusercontent.com/DevEmperor/Fastr/master/LICENSE)