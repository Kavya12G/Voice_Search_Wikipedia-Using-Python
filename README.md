Voice-Search-Wikipedia
=======================
A Python-based project that allows users to perform voice-activated searches on Wikipedia.
Converts user voice input to text, searches Wikipedia, and provides the results via text or audio output.

Features
----------------------------------------------------------------------------------------------
* Voice recognition for input.
  
* Fetches concise and accurate information from Wikipedia.
  
* Text-to-speech functionality to read the results aloud.
  
* Handles errors for invalid searches or no internet connection.
  
To install the above modules on your system, use the following :
-------------------------------------------------------------------------
1. pip install pyttsx3
   
   * A python package that supports common text to speech engines on Mac OS, Windows and Linux.

2. pip install SpeechRecognition

   * Library for performing speech recognition, with support for several engines and APIs, like CMU Sphinx, Microsoft Bing Voice Recognition, Google Cloud Speech API etc.

3. pip install wolframalpha

   * Python’s support library for WolframAlpha computational intelligence .

4. pip install wikipedia

   * Python’s library that makes it easy to access and parse data from Wikipedia.
     
Technologies Used
---------------------------------------
* **Python**: Core programming language.
  
* **Libraries:**
  
    * speech_recognition: For voice-to-text conversion.
  
    * wikipedia-api: To fetch content from Wikipedia.
  
    * pyttsx3 or gTTS: For text-to-speech conversion.
  
    * pyaudio (optional): Backend for audio input.
  
How It Works
-----------------
1. The application listens to the user's voice input.
   
2. Converts the speech to text using speech_recognition.
   
3. Searches the corresponding topic on Wikipedia using wikipedia-api.
   
4. Outputs the result as text and/or reads it aloud using a text-to-speech library.

   
