Install ROS2

gedit ~/.bashrc

source /opt/ros/humble/setup.bash

export ROS_DOMAIN_ID=5

------------------------Install YDLidar-SDK---------------------------

sudo apt update
sudo apt install git
sudo apt install cmake
sudo apt install pkg-config
sudo apt install pkg-config

Create a directory for the SDK (Optional, but good practice):

mkdir -p ~/YDLidar-SDK
cd ~/YDLidar-SDK

Clone the YDLidar-SDK Repository:

git clone https://github.com/YDLIDAR/YDLidar-SDK.git .

Create a build directory and navigate into it:

mkdir build
cd build

Configure the build with CMake:

cmake ..

Install the SDK:

sudo make install

cd aamabot_ws

colcon build --packages-select ydlidar_ros2_driver

---------------------------------------------------------------------

ros2 launch ydlidar_ros2_driver ydlidar_launch.py params_file:=/home/ihsl/aamabot_ws/src/ydlidar_ros2_driver/params/X2.yaml

sudo apt update
sudo apt install ros-humble-cartographer
sudo apt install ros-humble-cartographer-ros
ros2 pkg list | grep cartographer
. install/setup.bash

ros2 launch robot_cartographer_config mapping.launch.py (Only for creating new map)

Install Navigation2

sudo apt update
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup

source /opt/ros/humble/setup.bash
source /home/ihsl/aamabot_ws/install/setup.bash # Make sure your workspace is sourced too!

colcon build

. install/setup.bash

sudo apt update
sudo apt install ros-humble-rviz2

ros2 launch navigation navigation2.launch.py

ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py

