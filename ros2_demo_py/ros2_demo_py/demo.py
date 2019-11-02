import rclpy
from rclpy.node import Node
import base64

from std_msgs.msg import String

def readImage():
    with open('/home/luis/Documents/ros2_examples/ros2_demo_py/ros2_demo_py/testimage.jpg', 'rb') as f:
        file = f.read()
        file2 = String()
        #file2 = base64.b64encode(file, 'utf-8')
        file2 = str(file)
        #file2 = str(file, 'utf-8')
        print('tipo archivo', type(file2), file2)
        return file2
    return "empty"


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('ros2_demo_py')
        self.publisher_ = self.create_publisher(String, 'topic')
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        msg.data = readImage()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()