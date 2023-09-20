import pyttsx3 # ten thu vien

robot_brain = "Hello Dung"
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
#pip de cai dat cac thu vien