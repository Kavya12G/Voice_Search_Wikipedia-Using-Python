# Python package supporting common text-to-speech engines 
import pyttsx3 

# For understanding speech 
import speech_recognition as sr 

# For fetching the answers 
# to computational queries 
import wolframalpha 

# for fetching wikipedia articles 
import wikipedia 


# Function to search the query 
# that is either entered or spoken 
# by user 
def search(query): 
	
	# try is used for searching with wolframAlpha 
	try: 
		
		# Generate your App ID from WolframAlpha 
		app_id = "Your WolframAlpha App ID here"
		client = wolframalpha.Client(app_id) 
		res = client.query(query) 
		answer = next(res.results).text 
		print(answer) 
		SpeakText("Your answer is " + answer) 
		
	# If the query cannot be searched using 
	# WolframAlpha then it is searched in 
	# wikipedia 
	except: 
		
		query = query.split(' ') 
		query = " ".join(query[0:]) 
		
		SpeakText("I am searching for " + query) 
		print(wikipedia.summary(query, sentences = 3)) 
		SpeakText(wikipedia.summary(query, 
									sentences = 3)) 
		
	
# Function to convert text to 
# speech 
def SpeakText(command): 
		
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 

	
# Driver's code 
# input query from the user by 
# typing or by voice 
query = input() 
query = query.lower() 

# if query is blank then user 
# is prompted to speak something. 
if query == '': 
	r = sr.Recognizer() 

	# uses the default microphone 
	# as the source to record voice 
	with sr.Microphone() as source: 
		print("Say Something ") 

		# reduces the background disturbances 
		# and noise for 2 seconds 
		r.adjust_for_ambient_noise(source, 2) 
		
		# listening to source 
		audio = r.listen(source) 
	try: 
		speech = r.recognize_google(audio) 
		search(speech) 

	# Handling Exceptions if speech 
	# is not understood. 
	except sr.UnknownValueError: 
		print("Google Speech Recognition could not \ understand audio") 

	# Couldn't handle requests, occurs 
	# mainly because of network errors 
	except sr.RequestError as e: 
		print("Could not request results from Google \ Speech Recognition service;{0}".format(e)) 
else: 
	search(query) 

