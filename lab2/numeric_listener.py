import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericListener(Node):
    def __init__(self):
        super().__init__('numeric_listener')
        # Original string subscriber
        self.string_subscription = self.create_subscription(
            String,
            'chatter',
            self.string_callback,
            10)
        
        # New numeric subscriber
        self.numeric_subscription = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.numeric_callback,
            10)
        
        # Prevent unused variable warnings
        self.string_subscription
        self.numeric_subscription

    def string_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')

    def numeric_callback(self, msg):
        self.get_logger().info(f'I heard number: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    numeric_listener = NumericListener()
    rclpy.spin(numeric_listener)


if __name__ == '__main__':
    main()