This package allows the Youbot to navigate to different sets of blocks. It is the navigation part of a larger Youbot project.

Introduction
============

This package takes advantage of the ROS navigation stack to drive the Youbot's base to desired locations. After arriving at various locations, the Youbot will align itself so that the target is directly in front of the Hokuyo laser scanner.

Dependencies
============

1. [ROS navigation stack](http://wiki.ros.org/navigation)

2. [eband_local_planner](http://wiki.ros.org/eband_local_planner)

3. [youbot_driver_ros_interface](https://github.com/youbot/youbot_driver_ros_interface)

4. [hokuyo_node](http://wiki.ros.org/hokuyo_node)

Running the Demo
================

Currently, the files in this folder are calibrated to work in a specific lab environment. It uses the map for that particular space, so the map should be replaced with a customized map of its environment. In addition, while the setup requirements in this particular space do not have to be extremely precise, reliable results are guaranteed by the following set up for use within Northwestern University's D110 lab:

Align the back wheels of the youBot to be roughly on the two small pieces of tape within the closed off area.
Place two stacks of 3 blocks on the two green pluses in the closed off area.

Run the following:

```bash
roslaunch youbot_nav_msr
rosrun youbot_nav_msr fineTuneActionServer_odom.py
rosrun youbot_nav_msr fineTuneClient.py
```

By default, the fineTuneClient.py file will cause the robot to navigate to only one particular set of blocks. To navigate to the other set of blocks, comment out the actions to navigate to the default set of blocks and uncomment the actions to navigate to the desired set of blocks.

How the Navigation Works
========================

The action server node provides different navigation actions for the Youbot. The client requests these actions in a particular serial order. As a result, the action server published the move-base commands in the same serial order, in order to drive the youBot in to a set of blocks and align itself directly in front of them. Depending on the type of action requested, the youBot can move in different directions as required.

Helpful Links
================

The following are useful tools to help in development:
[Original youbot_nav_msr package developed by Jarvis Schultz and Matt Derry](https://github.com/NU-MSR/youbot_nav_msr)
[Youbot Teleop Package](https://github.com/youbot/youbot_driver_ros_interface/blob/hydro-devel/src/examples/youbot_keyboard_teleop.py)
