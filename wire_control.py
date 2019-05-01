#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from rosserial_arduino.msg import Adc

class wire_control:
	def __init__(self)
		rospy.init_node('control',anonymous=True)
		self,poten_sub = rospy.Subscriber("/adc", Adc, self.callback)
		self.action_c_pub = rospy_publisher("/control", Float32, queue=10)
		self.poten = Adc()
		self.action = 0
		self.pitch = 0
		self.yaw = 0

	def callback_poten(self, data):
		self.poten = data
		
		if self.poten.adc0 > 20
			
			self.action_c = 2

		else if self,poten.adc1 > 20

			self.action_c = 1

		else: 
			self.action_c = 0

		self.action_c_pub.publish(self.control)

if __name__ = '__main__'
	wc =wire_control()
	try:
	
		rospy.spin()
	except KeyboardInterrupt:
	print("Shutting Down")

