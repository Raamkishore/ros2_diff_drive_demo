# ros2_diff_drive_demo

This repository will help you understand how to control a differential drive robot with ros2_control. There are two main packages used to view and control the robot.  

## ign_gazebo_robot_package

The package ```ign_gazebo_robot_package``` is used to visualize the robot in Gazebo and load the controllers to control the robot. The controller ```diff_drive_base_controller``` is used here to control the robot.  

## command_publisher_package

The package ```command_publisher_package``` is used to publish commands for the robot to move around. It uses the message type ```Twist``` to send commands. The differential drive robot takes two parameters, the linear position along x axis and angular position along z axis.

### yaml

The command publishing package uses yaml file to load commands for the robot to move. The parameter ```goal_names``` of type STRING_ARRAY define how many positions has to be passed to the robot. The goal names are then used as parameters to define linear and angular values respectively.

## Versions tested

Please find below the versions where the packages have been tested

OS : Ubuntu 20.04 \
ROS2 : Galactic \
Gazebo : Gazebo Edifice

## Clone the repository

Open terminal and follow the commands mentioned below

```shell
mkdir -p dev_ws/src
cd dev_ws/src
```

 Clone the packages of the repository inside the src folder

 ## Build packages

 Make sure to build the package inside dev_ws folder and not inside src folder

```shell
 colcon build
 ```

 ## Source environment

 Source both the underlay and overlay environment

 ```shell
 source /opt/ros/galactic/setup.bash
 source install/setup.bash
 ```

 ## Visualize robot

 Visualize the robot in Gazebo by running the following command

 ```shell
 ros2 launch ign_gazebo_robot_package diff_drive_example.launch.py
 ```

 You can view a differential drive robot inside Gazebo

 ## Move the robot

 Move the robot by running the following command

 ```shell
 ros2 launch command_publisher_package cyclic_command_publisher.launch.py
 ```

 You can also provide your own number of positions inside the ```dev_ws/src/command_publisher_package/config/cyclic_diff_drive_params.yaml``` file. Make sure to build the packages again after editing the yaml file.

 ## References

 1) [Gazebo Robot](https://github.com/ros-controls/gz_ros2_control)
 2) [Command Publisher](https://github.com/ros-controls/ros2_control_demos)
