import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class DiffDriveCommandPublisher(Node):

    def __init__(self):
        super().__init__('diff_drive_command_publisher')

        self.declare_parameters(
            namespace='',
            parameters=[
                ('linear_velocity', 0.0),
                ('angular_velocity', 0.0)
            ]
        )
    
        self.publisher_ = self.create_publisher(Twist, '/diff_drive_base_controller/cmd_vel_unstamped', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        self.param_linear_velocity = self.get_parameter('linear_velocity').value
        self.param_angular_velocity = self.get_parameter('angular_velocity').value

        self.msg = Twist()
        self.msg.linear.x = self.param_linear_velocity
        self.msg.angular.z = self.param_angular_velocity
        self.publisher_.publish(self.msg)
        self.get_logger().info('Publishing')


def main(args=None):
    rclpy.init(args=args)

    diff_drive_command_publisher = DiffDriveCommandPublisher()

    rclpy.spin(diff_drive_command_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    diff_drive_command_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
