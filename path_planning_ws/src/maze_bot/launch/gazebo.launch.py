# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import ExecuteProcess
# from launch_ros.actions import Node
# from scripts import GazeboRosPaths

# def generate_launch_description():
#     package_share_dir = get_package_share_directory("maze_bot")
#     urdf_file = os.path.join(package_share_dir, "urdf", "maze_bot.urdf")

#     model_path, plugin_path, media_path = GazeboRosPaths.get_paths()
#     env = {
#         "GAZEBO_MODEL_PATH": model_path, 
#         "GAZEBO_PLUGIN_PATH": plugin_path,
#         "GAZEBO_RESOURCE_PATH": media_path,
#     }
#     return LaunchDescription(
#         [
#             ExecuteProcess(
#                 cmd=["gazebo","-s","libgazebo_ros_factory.so",],
#                 output="screen",
#                 additional_env=env,
#             ),
#             Node(
#                 package="gazebo_ros",
#                 executable="spawn_entity.py",
#                 arguments=["-entity","maze_bot","-b","-file", urdf_file,
#                 ],
#             ),
#             Node(
#                 package="robot_state_publisher",
#                 executable="robot_state_publisher",
#                 output="screen",
#                 arguments=[urdf_file],
#             ),
#         ]
#     )
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory , get_package_prefix
import os
from launch.actions import ExecuteProcess

def generate_launch_description():
    pkgPath = get_package_share_directory('maze_bot')
    urdfFile = os.path.join(pkgPath, 'urdf', 'maze_bot.urdf')

    mesh_pkg_share_dir = os.pathsep + os.path.join(get_package_prefix('maze_bot'), 'share')

    if 'GAZEBO_MODEL_PATH' in os.environ:
        os.environ['GAZEBO_MODEL_PATH'] += mesh_pkg_share_dir
    else:
        os.environ['GAZEBO_MODEL_PATH'] =  mesh_pkg_share_dir

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdfFile]),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='robot_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "bazu"]),

    ])