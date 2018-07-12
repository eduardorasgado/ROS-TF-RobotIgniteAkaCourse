execute_process(COMMAND "/home/canix/ros-tf-ria/build/turtle_tf_3d/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/canix/ros-tf-ria/build/turtle_tf_3d/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
