IMU-datalogger
==============

--What is it?--
This is an inertial datalogging system using low-cost hardware.
Currently the hardware setup is comprised of a Beaglebone Black, a Pololu AltIMU-10, and an 8 GB micro-SD card for data storage.

--Why?--
I plan to compare the quality of this <$100 system to that of professional systems worth >$10,000.
As my first Beaglebone project and first tech project in a while, it also serves as a useful exercise to learn the workings of Linux, remote development, I2C communication, and basic filtering.

--What is the current status?--
The code is currently being developed in Python but once a working version is reached development will be switched to C++.  So far there is functionality to read the output from the angular rate sensor, pressure sensor, and accelerometer.

--What is planned?--
Implement recording and basic software filtering of 3 axes of acceleration and angular rate.  As goals are reached more will be added.
