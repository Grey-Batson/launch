from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    zbar_node = Node(
	    package='zbar_ros',
	    executable='barcode_reader'
	)
    listener_node = Node(
        package='cpp_pubsub',
        executable='listener'
    )
    barcode_node = Node(
        package='locateBarcodeLocation',
        executable='locateBarcodeLocation'
    )
    
    ld.add_action(zbar_node)
    ld.add_action(listener_node)
    ld.add_action(barcode_node)
    
    return ld
