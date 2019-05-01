#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
from rosserial_arduino.msg import Adc

class wire_control:
        def __init__(self):
		rospy.init_node('control',anonymous=True)
		self.poten_sub = rospy.Subscriber("/adc", Adc, self.callback_poten)
		self.action_pub = rospy.Publisher("/action", Int8, queue_size=1)
		self.poten = Adc()
		self.action = 0
		self.pitch = 0
		self.yaw = 0

	def callback_poten(self, data):
		self.poten = data
		
                if self.poten.adc0 > 30:
			
			self.action = 2

                elif self.poten.adc0 < 10 or self.poten.adc1 > 0:

			self.action = 1

		else:
			self.action = 0
                print 'action =', self.action
		self.action_pub.publish(self.action)

if __name__ == '__main__':
	wc =wire_control()
	try:
	
		rospy.spin()
	except KeyboardInterrupt:
        	print("Shutting Down")

