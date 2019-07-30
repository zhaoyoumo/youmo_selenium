#-*-coding:utf-8-*- 
__author__ = 'Youmo' 
def suspect(event):
	if event == "t kill p":
		print "the suspect is t"
	elif event == "t kill p`friend":
		print "the suspect is t"
	elif event == "p kill p`friend":
		print "the suspect is p"
	elif event == "p kill t":
		print "the suspect is p"
	else:
		print "the suspect is p`friend"