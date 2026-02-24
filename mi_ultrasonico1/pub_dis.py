import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import random  


class MyPublisher(Node):

    def __init__(self):
        super().__init__('mi_nodo_clases_jiji')
        self.publisher_ = self.create_publisher(String, 'ignaciop', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()

        numero = random.randint(1, 5)  
        msg.data = f'Numero aleatorio: {numero}'

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MyPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()