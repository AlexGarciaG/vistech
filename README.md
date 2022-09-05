# vistech
Vistech aims to apply vision and technology to design an autonomous vehicle that can go from A to B while identifying traffic signs, other cars, traffic lights, and persons.
# Table of contents
- [Objectives.](#objectives)
- [Equitment used.](#equitment-used)
  * [Software](#software)
  * [Hardware](#hardware)
- [Install Requirements](#install-requirements)
    + [Software](#software-1)
    + [Packages](#packages)
    + [Git](#git)
- [Set up environment.](#set-up-environment)
  * [Arduino](#arduino)
  * [Joy](#joy)
  * [Ready to go when turned on.](#ready-to-go-when-turned-on)
- [More Information](#more-information)
- [Authors](#authors)
- [Other sources.](#other-sources)
# Objectives.
The main objective of this project is to create a differential robot representing a car that will travel autonomously while following the basic traffic signs(speed limit, stop, turns ), other vehicles, traffic lights, and persons. 
The secondary objective is to implement a directional Akerman direction so the robot can more significantly represent actual car behavior. 

# Equitment used.
The section will list all the hardware and Software used so that any user can recreate this project. 
You could use different hardware, but it will impact the performance and behavior, which implies an adjustment in the Software.

## Software
The project must be installed on ROS noetic and ubuntu 20.04; in other environments, the project may not work correctly. 
## Hardware
This project was built using the following equipment:
Jetson Xavier Nx developer kit
Camera Web Logitech B5252
# Install Requirements
The following commands must be executed on the computer onboard (Jetson Xavier Nx)
### Software
[Install ROS](http://wiki.ros.org/noetic/Installation/Ubuntu)
[Install Arduino](https://docs.arduino.cc/software/ide-v1/tutorials/Linux)
### Packages
### Git
# Set up environment.
This section will be executed after all the requirements are installed; otherwise, it will work improperly or fail.
## Arduino
Upload the file [.......] to the Arduino Mega
## Joy
To setup, a remote controller executed the following commands extracted from [..........]
## Ready to go when turned on.
Follow this set of instructions so the Autonomous vehicle is ready to go when it is powered. 
# More information
# Authors
- [Alexis Garcia Gutierrez](https://github.com/AlexGarciaG)


- [Rodrigo Gutiérrez Alvarez](https://github.com/D3ceiver)


- [Laura Aylín Rivero López](https://github.com/LauRivero150920)


- [Mónica Jimena Juárez Espinosa](https://github.com/Monica3751)

# Other sources.
- [Download Arduino](https://www.arduino.cc/en/software)
- [Install Arduino on Ubuntu](https://docs.arduino.cc/software/ide-v1/tutorials/Linux)
- [Install ROS on Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)
- [ROS tutorials](http://wiki.ros.org/ROS/Tutorials)
- [Make a ROS Launch Start on Boot (robot_upstart)](https://roboticsbackend.com/make-ros-launch-start-on-boot-with-robot_upstart/)
- [Configuring and Using a Linux-Supported Joystick with ROS](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick)
- [Converting between ROS images and OpenCV images (Python)](http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython) 
- [JetPack SDK](https://developer.nvidia.com/embedded/jetpack)
- [Write Image to the MicroSD Card](https://developer.nvidia.com/embedded/learn/get-started-jetson-xavier-nx-devkit#write) 
- [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/)
