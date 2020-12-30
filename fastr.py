# !/usr/bin/env python3

# Check for missing dependencies which are: SpeechRecognition, Pandas and PyAudio
try:
    import os
    import speech_recognition as sr
    from pandas.io.clipboard import copy as cp
except ImportError as e:
    exit(f"\033[91mMissing dependency: {e.name}. Please check your installation!")

# Colors used to make the terminal look nicer
GREEN, YELLOW, RED, CYAN, PURPLE, RESET = '\033[92m', '\033[93m', '\033[91m', '\033[96m', '\033[95m', '\033[0m'
restart = "yes"

# Always check for ctrl+c
try:
    # Create recognizer and microphone
    r = sr.Recognizer()
    m = sr.Microphone()
    mics = m.list_microphone_names()

    # Clear up all debug messages from PyAudio and print the heading
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""
          f"\n ███████{RED}╗{RESET} █████{YELLOW}╗{RESET} ███████{GREEN}╗{RESET}████████{CYAN}╗{RESET}██████{PURPLE}╗{RESET} "
          f"\n ██{RED}╔════╝{RESET}██{YELLOW}╔══{RESET}██{YELLOW}╗{RESET}██{GREEN}╔════╝{CYAN}╚══{RESET}██{CYAN}╔══╝{RESET}██{PURPLE}╔══{RESET}██{PURPLE}╗{RESET}"
          f"\n █████{RED}╗{RESET}  ███████{YELLOW}║{RESET}███████{GREEN}╗   {RESET}██{CYAN}║{RESET}   ██████{PURPLE}╔╝{RESET}"
          f"\n ██{RED}╔══╝{RESET}  ██{YELLOW}╔══{RESET}██{YELLOW}║{GREEN}╚════{RESET}██{GREEN}║   {RESET}██{CYAN}║{RESET}   ██{PURPLE}╔══{RESET}██{PURPLE}╗{RESET}"
          f"\n ██{RED}║{RESET}     ██{YELLOW}║{RESET}  ██{YELLOW}║{RESET}███████{GREEN}║{RESET}   ██{CYAN}║{RESET}   ██{PURPLE}║  {RESET}██{PURPLE}║{RESET}"
          f"\n {RED}╚═╝     {YELLOW}╚═╝  ╚═╝{GREEN}╚══════╝   {CYAN}╚═╝   {PURPLE}╚═╝  ╚═╝{RESET}"
          "\n     by DevEmperor\n\n")

    # Check if there are no input devices and then exit
    if len(mics) == 0:
        exit(f"[{RED}-{RESET}] Could't find any microphone/soundcard on your device. Exiting! :-(")

    # Ask the user if he wants to choose the mic manually
    if input(f"[{CYAN}?{RESET}] Do you want to choose your microphone manually? [yes/NO] ").lower() == "yes":
        print(f"[{GREEN}+{RESET}] These microphones/soundcards were found:")
        for index, name in enumerate(mics):  # List all devices
            print(f"     {index} = {name}")
        while True:
            mic_index = input(f"[{CYAN}?{RESET}] Which input device do you want to use? ")
            if mic_index.isdigit():
                if int(mic_index) > len(mics) - 1:
                    continue
                m = sr.Microphone(device_index=int(mic_index))  # Override the microphone with another device_index
                break
            continue

    with open("./language_codes.dat", "r") as f:
        codes = f.read().splitlines()  # Read all language-codes

    while True:
        lang = input(f"[{CYAN}?{RESET}] Enter the language code of your language [en-US]: ")
        if lang == "":  # default language
            lang = "en-US"
        elif len(lang) == 2 and not any(lang in s for s in codes):  # check for short codes
            print(f"[{RED}-{RESET}] I don't know this language...")
            continue
        elif len(lang) != 2 and lang not in codes:  # check for long codes
            print(f"[{RED}-{RESET}] I don't know this language...")
            continue
        break

    copy = input(f"[{CYAN}?{RESET}] Should I copy the result to your clipboard? [YES/no] ")
    if copy.lower() == "no":
        copy = False
    else:
        copy = True

    input(f"[{CYAN}?{RESET}] Press any key to start...\n")  # last confirmation

    while restart.lower() != "no":  # always repeat the recording/recognation
        print(f"[{GREEN}+{RESET}] Now start talking and I'll try to recognize what you said...")
        with m as source:
            try:
                r.pause_threshold = 2  # Stop after 3 seconds of silence
                audio = r.listen(m, timeout=10)  # Start listening...
            except sr.WaitTimeoutError:  # ... and exit if there isn't any signal
                exit(f"[{RED}-{RESET}] Didn't get any input signal. Exiting! :-(")

        print(f"[{GREEN}+{RESET}] Recognizing...")
        try:
            result = str(r.recognize_google(audio, language=lang)).strip('\n')  # Start recognization...
            result = result[0].upper() + result[1:]  # (to start with a capital letter)
            print(f"[{GREEN}+{RESET}] I think you said:\n\n\033[1m{result}\n")  # ...print the result...
            if copy:
                cp(result)  # ...and copy it to your system clipboard
                print(f"[{GREEN}+{RESET}] Copied this result to your clipboard! ;-)")
        except sr.UnknownValueError:  # Error if nothing was said...
            print(f"[{RED}-{RESET}] Couldn't understand your speech!")
        except sr.RequestError as e:  # ...or if Google couldn't handle the request
            print(f"[{RED}-{RESET}] Could not request results from Google Speech Recognition service; {e}")
        restart = input(f"[{CYAN}?{RESET}] Do you want me to recognize something else? [YES/no] ")  # Ask for repeat

    print(f"{GREEN}Have a nice day!")
    exit(0)
except KeyboardInterrupt:
    print(f"\n{RED}Exiting... Bye!")
