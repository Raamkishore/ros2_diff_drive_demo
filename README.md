# ros2_diff_drive_demo

Please find below the versions where the packages have been tested

OS : Ubuntu 20.04 \
ROS2 : Galactic

## Clone the package

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
