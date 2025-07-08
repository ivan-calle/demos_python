#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------#
# 1. LIBRARIES
#---------------------------------------------------------------------------#
import rclpy
import sys
from time import sleep

#---------------------------------------------------------------------------#
# 2. CREATE THE NODE
#---------------------------------------------------------------------------#
rclpy.init()
node = rclpy.create_node('blinker_py')

#---------------------------------------------------------------------------#
# 3. LOOP TO SHOW MESSAGES EVERY 2s
#---------------------------------------------------------------------------#
#  3.1. SET THE LOOP RATE
rate = node.create_rate(2)
#  3.2. SHOW MESSAGES WHILE THE NODE IS OK
while rclpy.ok():
     # Show message
     node.get_logger().info('Hello Malena UNI from python3!')
     # Sleep
     sleep(0.5)
