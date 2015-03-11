AutoPidact
==========
A simplistic vision-based learning algorithm to allow a Raspberry Pi to learn to launch a ball into a goal.

NOTE: This project was a project for my CS202 class and due to time constraints was never completed. It serves mostly as a reference for (faulty -- see below) OpenCV blob detection and simplistic PWM control between a Raspberry Pi and an FPGA board. If both Max and Foster gain access to the parts of the robot again, development may continue but it is unlikely.

I've since learned OpenCV blob detection works much better if you threshold HSV values. Most of this code can be used for blob detection, but use HSV thresholding instead of leaving the image in BGR format.
