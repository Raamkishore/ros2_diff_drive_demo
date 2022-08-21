# Copyright 2021 Stogl Robotics Consulting UG (haftungsbeschränkt)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class CyclicDiffDriveCommandPublisher(Node):
    def __init__(self):
        super().__init__("cyclic_diff_drive_command_publisher")
        # Declare all parameters
        self.declare_parameter("wait_sec_between_publish", 5)
        self.declare_parameter("goal_names", [""])

        # Read parameters
        wait_sec_between_publish = self.get_parameter("wait_sec_between_publish").value
        goal_names = self.get_parameter("goal_names").value

        # Read all positions from parameters
        self.goals = []
        for name in goal_names:
            self.declare_parameter(name)
            goal = self.get_parameter(name).value
            if goal is None or len(goal) == 0:
                raise Exception(f'Values for goal "{name}" not set!')

            float_goal = []
            for value in goal:
                float_goal.append(float(value))
            self.goals.append(float_goal)

        publish_topic = "/diff_drive_base_controller/cmd_vel_unstamped"

        self.get_logger().info(
            f'Publishing {len(goal_names)} goals on topic "{publish_topic}"\
              every {wait_sec_between_publish} s'
        )

        self.publisher_ = self.create_publisher(Twist, publish_topic, 1)
        self.timer = self.create_timer(wait_sec_between_publish, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.goals[self.i][0]
        msg.angular.z = self.goals[self.i][1]
        self.get_logger().info(f'Publishing -> Linear : "{msg.linear.x}" and Angular : "{msg.angular.z}"')
        self.publisher_.publish(msg)
        self.i += 1
        self.i %= len(self.goals)

        if self.i == 0:
            raise Exception(f'End of positions!')


def main(args=None):
    rclpy.init(args=args)

    cyclic_diff_drive_command_publisher = CyclicDiffDriveCommandPublisher()

    rclpy.spin(cyclic_diff_drive_command_publisher)
    cyclic_diff_drive_command_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()