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

| Name                           | Quantity | Motive |
| ------------------------------ | -------- | ------ |
| Jetson Xavier Nx developer kit | 1        | ---    |
| Camera Web Logitech B5252      | 1        | ---    |
| Arduino Mega 2560              | 1        | ---    |
| H Bridge L298                  | 2        | ---    |
| RPLIDAR                        | 1        | ---    |
| Joystick                       | 1        | ---    |

## Other

| Name                                          | Quantity | Motive |
| --------------------------------------------- | -------- | ------ |
| MDF                                           |          | ---    |
| Couplers for the wheels                       | 4        | ---    |
| Motor supports                                | 4        | ---    |
| Li-Po rechargeable batteries (7.2V and 11.1V) | 2        | ---    |
| Sealed lead acid battery 12Vcc                | 1        | ---    |

# Install Requirements

The following commands must be executed on the computer onboard (Jetson Xavier Nx)

## Software

- [Install ROS](http://wiki.ros.org/noetic/Installation/Ubuntu)
- [Install Arduino](https://docs.arduino.cc/software/ide-v1/tutorials/Linux)

## Packages

### Install joy

```
$ sudo apt-get install ros-noetic-joy
```

### Install arduino packages

```
$ sudo apt-get install ros-noetic-rosserial
$ sudo apt-get install ros-noetic-rosserial-arduino
```

### Install the package robot_upstart

```
$ sudo apt-get install ros-noetic-robot-upstart 
```

## Git

Clone the repository

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/AlexGarciaG/vistech.git
```

# Set up environment.

This section will be executed after all the requirements are installed; otherwise, it will work improperly or fail.

## Arduino

Add our user to the group so the arduino file can be upload without erros.

```
$ sudo usermod -a -G dialout <username>
```

Upload the file [motors.ino](./arduino/motors_ros/motors.ino) to the Arduino Mega

## Joy

To setup, a remote controller executed the following commands extracted from [Configuring and Using a Linux-Supported Joystick with ROS](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick)

Connect your joystick to your computer. Now let's see if Linux recognized your joystick.

```
$ ls /dev/input/
```

You will see a listing of all of your input devices similar to below:

```
by-id    event0  event2  event4  event6  event8  mouse0  mouse2  uinput
by-path  event1  event3  event5  event7  js0     mice    mouse1
```

As you can see above, the joystick devices are referred to by jsX ; in this case, our joystick is js0. Let's make sure that the joystick is working.

```
$ sudo jstest /dev/input/jsX
```

You will see the output of the joystick on the screen. Move the joystick around to see the data change.

```
Driver version is 2.1.0.
Joystick (Logitech Logitech Cordless RumblePad 2) has 6 axes (X, Y, Z, Rz, Hat0X, Hat0Y)
and 12 buttons (BtnX, BtnY, BtnZ, BtnTL, BtnTR, BtnTL2, BtnTR2, BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR).
Testing ... (interrupt to exit)
Axes:  0:     0  1:     0  2:     0  3:     0  4:     0  5:     0 Buttons:  0:off  1:off  2:off  3:off  4:off  5:off  6:off  7:off  8:off  9:off 10:off 11:off
```

Now let's make the joystick accessible for the ROS joy node.

```
$ sudo chmod a+rw /dev/input/jsX
```

To get the joystick data published over ROS we need to start the joy node. First let's tell the joy node which joystick device to use- the default is js0.

```
$ roscore
$ rosparam set joy_node/dev "/dev/input/jsX"
```

Now we can start the joy node.

```
$ rosrun joy joy_node
```

You will see something similar to:

```
[ INFO] 1253226189.805503000: Started node [/joy], pid [4672], bound on [aqy], xmlrpc port [33367], tcpros port [58776], logging to [/u/mwise/ros/ros/log/joy_4672.log], using [real] time

[ INFO] 1253226189.812270000: Joystick device: /dev/input/js0

[ INFO] 1253226189.812370000: Joystick deadzone: 2000
```

Now in a new terminal you can rostopic echo the joy topic to see the data from the joystick:

```
$ rostopic echo joy
```

As you move the joystick around, you will see something similar to :

```
---
axes: (0.0, 0.0, 0.0, 0.0)
buttons: (0, 0, 0, 0, 0)
---
axes: (0.0, 0.0, 0.0, 0.12372203916311264)
buttons: (0, 0, 0, 0, 0)
---
axes: (0.0, 0.0, -0.18555253744125366, 0.12372203916311264)
buttons: (0, 0, 0, 0, 0)
---
axes: (0.0, 0.0, -0.18555253744125366, 0.34022033214569092)
buttons: (0, 0, 0, 0, 0)
---
axes: (0.0, 0.0, -0.36082032322883606, 0.34022033214569092)
buttons: (0, 0, 0, 0, 0)
```

## Ready to go when turned on.

Follow this set of instructions so the Autonomous vehicle is ready to go when it is powered.
For more info see [Make a ROS Launch Start on Boot (robot_upstart)](https://roboticsbackend.com/make-ros-launch-start-on-boot-with-robot_upstart/)

Add robot_upstart roslaunch to systemctl

```
$ rosrun robot_upstart install vistech/launch/vistech/robot_upstart.launch --job robot_upstart_vistech --symlink
```

Enable the robot_upstart_vistech service so its executed when the computer is powered

```
$ sudo systemctl enable robot_upstart_vistech.service
```

Start the robot_upstart_vistech service so its executed in the current session or restart the computer

```
$ sudo systemctl start robot_upstart_vistech.service
```

To stop the robot_upstart_vistech service

```
$ sudo systemctl stop robot_upstart_vistech.service
```

To restart the robot_upstart_vistech.service execute

```
$ sudo systemctl restart robot_upstart_vistech.service
```

# More information

[1st Term Report](./Documentation/1st-Term-Report.pdf)

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
- [Label Images Tool](https://roboflow.com/)
- [Assign a static USB port on Linux](https://msadowski.github.io/linux-static-port/)
- [How to bind USB device under a static name?](https://unix.stackexchange.com/questions/66901/how-to-bind-usb-device-under-a-static-name)
- [USB Multi-Unit Capability](https://forums.basicmicro.com/viewtopic.php?t=442)
- [Driver 4.1.34, Noetic, multiple fixes ](https://github.com/sonyccd/roboclaw_ros/pull/31)
