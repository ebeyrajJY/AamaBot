from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Package share directories
    ydlidar_pkg = get_package_share_directory('ydlidar_ros2_driver')
    rf2o_pkg = get_package_share_directory('rf2o_laser_odometry')
    nav2_pkg = get_package_share_directory('navigation')  # or 'nav2_bringup' if you're using that

    # YDLIDAR config path
    ydlidar_param = os.path.join(ydlidar_pkg, 'params', 'X2.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ydlidar_pkg, 'launch', 'ydlidar_launch.py')),
            launch_arguments={'params_file': ydlidar_param}.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(rf2o_pkg, 'launch', 'rf2o_laser_odometry.launch.py')
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_pkg, 'launch', 'navigation2.launch.py')
            )
        ),
    ])

