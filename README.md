### ROS Visualizer of TIAGo facial expressions on a screen ### 



#### Package:
- **face_builder** folder contains all the png images used to build the robot's face.
- **launch** folder contains the ros launch file
- **script** folder contains the code to build the face. Most of the code has been got from the work of Bilgehan NAL and just a few things have been edited or removed in order to get it working with the TIAGo.



## USAGE ###

First you need to run the ros node which builds the robot facial expressions (repo [robot_face_expression](https://github.com/aandriella/robot_face_expression)):

``` 
 roslaunch robot_face_expression robot_face_expression.launch 
```

Then you can visualise the different facial expressions by running:

``` 
 rosrun robot_face_visualizer face_visualizer.py
```

You can change facial expression and the pupil position in the eyes as follows:
``` 
rostopic pub /facial_expression std_msgs/String "data: 'expression'" 
```
esxpression can be "sad", "angry", "confused", "happy", "neutral", eyes can be moved with "look_X_Y"
