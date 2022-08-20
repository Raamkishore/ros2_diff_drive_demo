import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('command_publisher_package'),
        'config',
        'diff_drive_params.yaml'
        )

    start_publisher_node = Node(
            package='command_publisher_package',
            executable='diff_drive_publisher_node',
            parameters = [config]
        )


    return LaunchDescription([
        start_publisher_node,
    ])
