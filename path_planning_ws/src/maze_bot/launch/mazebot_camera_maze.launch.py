from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory , get_package_prefix
import os
from launch.actions import ExecuteProcess
from scripts  import GazeboRosPaths
def generate_launch_description():
    pkgPath = get_package_share_directory('maze_bot')
    urdfFile = os.path.join(pkgPath, 'urdf', 'maze_bot.urdf')
    world_file = os.path.join(pkgPath,"worlds","maze_2.world")

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
            cmd=['gazebo', '--verbose',world_file ,'-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='robot_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "bazu"]),
    ]
    # return LaunchDescription(
    # [
    #     ExecuteProcess(
    #         cmd=["gazebo","--verbose",world_file,"-s","libgazebo_ros_factory.so"],
    #         output="screen",
    #         # additional_env=env,
    #     ),
    #     Node(
    #         package="gazebo_ros",
    #         executable="spawn_entity.py",
    #         arguments=["-entity","maze_bot","-b","-file", urdfFile,
    #         ],
    #     ),
    #     Node(
    #         package="robot_state_publisher",
    #         executable="robot_state_publisher",
    #         output="screen",
    #         arguments=[urdfFile],
    #     ),
    # ]
    )