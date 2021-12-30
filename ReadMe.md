### Environment configuration

update the qt and opencv-python env
~~~shell
sudo bash install.sh
~~~

if you sys has an early opencv-python please uninstall it and install other version
such as opencv-python==4.2.0.32,which you can make an shell order like
~~~shell
pip uninstall opencv-python
pip install opencv-python==4.2.0.32
~~~
<br>
<font color= green>Remember do not use the same path to load the images and save the images</font>

#### please enjoy the program


The program just use to resize of the images in a dir,but if the user want to use the face detection,please make sure of the opencv face detect 'xml' path