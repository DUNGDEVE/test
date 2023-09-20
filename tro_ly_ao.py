import pyttsx3 # ten thu vien
import speech_recognition
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=" "

while True:
	with speech_recognition.Microphone( ) as mic:
		print("Robot: I'm listening")
		audio=robot_ear.listen(mic)
	print("Robot:...")

	try:
		you = robot_ear.recognize_google(audio)
	except:	
		you ==" "
	print("you: "+ you)

	if you == "":
		robot_brain = "i can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Dung"
	elif "today" in you:
		today = date.today()
		robot_brain= today.strftime("%B %d, %Y")
	elif "time" in you:
		now= datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "president" in you:
		robot_brain = "Joe Biden"
	elif "bye" in you:
		robot_brain = "Bye Viet Dung"
		print("Robot"+ robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	#pip de cai dat cac thu vien
		break
	else:
		robot_brain = "I'm fine thank you and you"
	print("Robot: "+ robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
	#pip de cai dat cac thu vien