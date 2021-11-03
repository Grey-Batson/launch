from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zbar_ros',
            namespace='barcode_reader',
            executable='barcode_reader',
            name='barcode_reader'
        ),
        Node(
            package='cpp_pubsub',
            namespace='listener',
            executable='listener',
            name='listener'
        ),
        Node(
            package='locateBarcodeLocation',
            namespace='locateBarcodeLocation',
            executable='locateBarcodeLocation',
            name='locateBarcodeLocation'
        )
    ])
