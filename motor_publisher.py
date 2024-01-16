#!/usr/bin/env python3
import RPi.GPIO as GPIO
import curses
import rospy
from std_msgs.msg import String
from time import sleep
en,in1,in2=25,23,24
en1,in3,in4=17,22,27
temp1=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.LOW)
GPIO.setup(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.LOW)
GPIO.setup(in4,GPIO.LOW)
p1 = GPIO.PWM(en,555)
p2 = GPIO.PWM(en1,555)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1.start(25)
p2.start(25)
print("working")
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)
pub=rospy.Publisher('chatter',String,queue_size=10)
rospy.init_node('talker',anonymous=True)
try:
        while True:
                char = screen.getch()
                if char == curses.KEY_UP:
                        str="MOVING FORWARD"
                        rospy.loginfo(str)
                        pub.publish(str)
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.HIGH)
                        GPIO.output(in4,GPIO.LOW)
                        char2 = screen.getch()
                        if char2 == curses.KEY_DOWN:
                                str1="STOPPED FBACK"
                                rospy.loginfo(str1)
                                pub.publish(str1)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.LOW)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.LOW)

                if char == curses.KEY_DOWN:
                        str2="MOVING BACKWARD"
                        rospy.loginfo(str2)
                        pub.publish(str2)
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.HIGH)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.HIGH)
                        char3 = screen.getch()
                        if char3 == curses.KEY_UP:
                                str3="STOPPED"
                                rospy.loginfo(str3)
                                pub.publish(str3)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.LOW)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.LOW)
                        if char3 == curses.KEY_RIGHT:
                                str4="MOVING BACK RIGHT"
                                rospy.loginfo(str4)
                                pub.publish(str4)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.LOW)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.HIGH)
                        if char3 == curses.KEY_LEFT:
                                str5="MOVING BACK LEFT"
                                rospy.loginfo(str5)
                                pub.publish(str5)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.HIGH)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.LOW)
                if char == curses.KEY_RIGHT:
                        str6="MOVING RIGHT"
                        rospy.loginfo(str6)
                        pub.publish(str6)
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.LOW)
                        char4 = screen.getch()
                        if char4 == curses.KEY_LEFT:
                                str7="STOPPED"
                                rospy.loginfo(str7)
                                pub.publish(str7)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.LOW)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.LOW)
                if char == ord(' '):
                        print("BRAKE")
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.LOW)
                if char == curses.KEY_LEFT:
                        str8="MOVING LEFT"
                        rospy.loginfo(str8)
                        pub.publish(str8)
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.HIGH)
                        GPIO.output(in4,GPIO.LOW)
                        char5 = screen.getch()
                        if char5 == curses.KEY_RIGHT:
                                str9="STOPPED"
                                rospy.loginfo(str9)
                                pub.publish(str9)
                                GPIO.output(in1,GPIO.LOW)
                                GPIO.output(in2,GPIO.LOW)
                                GPIO.output(in3,GPIO.LOW)
                                GPIO.output(in4,GPIO.LOW)

                if char == ord('q'):
                        GPIO.cleanup()
                        break
finally:
                curses.nocbreak();screen.keypad(0);curses.echo()
                curses.endwin()
