#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------#
# 1. LIBRARIES
#---------------------------------------------------------------------------#
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


#---------------------------------------------------------------------------#
# 2. LIBRARIES
#---------------------------------------------------------------------------#
class MinimalSubscriber(Node):
	def __init__(self):
		# Set node
		super().__init__('subscriber')
		# Topic subscription
		self.subscription = self.create_subscription(
			String,
			'topic',
			self.listener_callback,
			10)
		self.subscription  # prevent unused variable warning

	def listener_callback(self, msg):
		self.get_logger().info('I heard: "%s"' % msg.data)


#---------------------------------------------------------------------------#
# 3. MAIN FUNCTION
#---------------------------------------------------------------------------#
def main(args=None):
	# Initialize and create a subscriber
	rclpy.init(args=args)
	minimal_subscriber = MinimalSubscriber()
	rclpy.spin(minimal_subscriber)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	minimal_subscriber.destroy_node()
	rclpy.shutdown()


#---------------------------------------------------------------------------#
# 4. ACTIVATE AUTOMATICALLY WHEN USED AS A CONSOLE PROGRAM
#---------------------------------------------------------------------------#
if __name__ == '__main__':
	main()