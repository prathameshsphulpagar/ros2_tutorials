# ros2_tutorials
 all tutorials code
 
1) Creating the workspace in ros2
 ```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
 ```
 
2) If you wanted to open ws in any perticular folder then remove the ~/ part from the command and create the ws. 

 ```
mkdir -p ros2_ws/src
cd ros2_ws/src
 ```
 
3) create pakage 
```
ros2 pkg create --build-type ament_cmake <package_name>
``` 

4) To delete some files through terminal
'''
rm -r include/ src/
'''

5) To only run the perticular pakage not the other pakages
```
colcon build --packages-select my_robot_interfaces
```
