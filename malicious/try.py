# import speech_recognition as sr
# import pyttsx3
# from os import path
# import sys

# """VOICE"""
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')  # object creation
# engine.setProperty('voice', voices[1].id)  # female voice

# """RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# engine.setProperty('rate', 180)     # setting up new voice rate

# """VOLUME"""

# # getting to know current volume level (min=0 and max=1)
# volume = engine.getProperty('volume')
# engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

# r1 = sr.Recognizer()


# def create(speech):
#     try:
#         list_of_words = speech.split()
#         file_name = list_of_words[list_of_words.index('create') + 1] + '.txt'
#         file_present = path.exists(f"files/{file_name}")
#         if file_present == False:
#             file = open(f"files/{file_name}", "w+")
#             if 'write' in speech:
#                 file.write(f"{write}")
#         else:
#             engine.say(
#                 'File already exist!! Do you want to try with another name?')
#             engine.runAndWait()
#             try:
#                 with sr.Microphone() as source:
#                     print("Speak:", end=" ")
#                     audio = r1.listen(source)
#                     r1.adjust_for_ambient_noise(source)
#                     create_reply_bool = r1.recognize_google(audio)
#                     print(create_reply_bool)
#                     if "yes" in create_reply_bool:
#                         engine.say("okay, say another name!")
#                         engine.runAndWait()
#                         assistant()
#                         # with sr.Microphone() as source:
#                         #     print("Speak:", end=" ")
#                         #     audio = r1.listen(source)
#                         #     create_another_file = r1.recognize_google(audio)
#                         #     print(create_another_file)
#             except sr.UnknownValueError:
#                 engine.say("Could not understand your voice. Try again!")
#                 engine.runAndWait()
#                 assistant()
#     except:
#         print("Oops!", sys.exc_info()[0], 'Occured.')


# def assistant():
#     try:
#         with sr.Microphone() as source:
#             print("Speak:", end=" ")
#             r1.pause_threshold = 0.6
#             r1.adjust_for_ambient_noise(source)
#             audio = r1.listen(source)
#             speech = r1.recognize_google(audio, language='en-in')
#             speech = speech.lower()
#             print(speech)
#         if 'create' in speech:
#             create(speech)
#             # engine.say(speech)
#             # engine.runAndWait()
#         else:
#             engine.say("That's not a command. Try again!")
#             engine.runAndWait()
#             assistant()
#     except sr.UnknownValueError:
#         engine.say("Could not understand your voice. Try again!")
#         engine.runAndWait()
#         assistant()
#     except:
#         print("Oops!", sys.exc_info()[0], 'Occured.')


# assistant()

# from chatterbot import ChatBot
# import tkinter as tk
# try:
#     import ttk as ttk
#     import ScrolledText
# except ImportError:
#     import tkinter.ttk as ttk
#     import tkinter.scrolledtext as ScrolledText
# import time


# class TkinterGUIExample(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         """
#         Create & set window variables.
#         """
#         tk.Tk.__init__(self, *args, **kwargs)

#         self.chatbot = ChatBot(
#             "GUI Bot",
#             storage_adapter="chatterbot.storage.SQLStorageAdapter",
#             logic_adapters=[
#                 "chatterbot.logic.BestMatch"
#             ],
#             database_uri="sqlite:///database.sqlite3"
#         )

#         self.title("Chatterbot")

#         self.initialize()

#     def initialize(self):
#         """
#         Set window layout.
#         """
#         self.grid()

#         self.respond = ttk.Button(
#             self, text='Get Response', command=self.get_response)
#         self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

#         self.usr_input = ttk.Entry(self, state='normal')
#         self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

#         self.conversation_lbl = ttk.Label(
#             self, anchor=tk.E, text='Conversation:')
#         self.conversation_lbl.grid(
#             column=0, row=1, sticky='nesw', padx=3, pady=3)

#         self.conversation = ScrolledText.ScrolledText(self, state='disabled')
#         self.conversation.grid(column=0, row=2, columnspan=2,
#                                sticky='nesw', padx=3, pady=3)

#     def get_response(self):
#         """
#         Get a response from the chatbot and display it.
#         """
#         user_input = self.usr_input.get()
#         self.usr_input.delete(0, tk.END)

#         response = self.chatbot.get_response(user_input)

#         self.conversation['state'] = 'normal'
#         self.conversation.insert(
#             tk.END, "Human: " + user_input + "\n" +
#             "ChatBot: " + str(response.text) + "\n"
#         )
#         self.conversation['state'] = 'disabled'

#         time.sleep(0.5)


# gui_example = TkinterGUIExample()
# gui_example.mainloop()
