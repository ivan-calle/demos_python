#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------#
# 1. LIBRARIES
#---------------------------------------------------------------------------#
import rclpy
from std_msgs.msg import String


#---------------------------------------------------------------------------#
# 2. CREATE THE NODE
#---------------------------------------------------------------------------#
rclpy.init()
node = rclpy.create_node('publisher_py')
publisher = node.create_publisher(String, 'topic', 10)


#---------------------------------------------------------------------------#
# 3. LOOP TO SHOW MESSAGES
#---------------------------------------------------------------------------#
#  3.1. SET THE LOOP RATE
rate = node.create_rate(0.5)
msg = String()
#  3.2. SHOW MESSAGES WHILE THE NODE IS OK
i = 0
while rclpy.ok():
	msg.data = 'Hello World: %d' % i
	i += 1
	# Show message
	publisher.publish(msg)
	node.get_logger().info('Publishing: "%s"' % msg.data)
	# Sleep
	rclpy.spin_once(node)
	rate.sleep()
