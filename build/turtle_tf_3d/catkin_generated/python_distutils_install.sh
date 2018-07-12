#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/canix/ros-tf-ria/src/turtle_tf_3d"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/canix/ros-tf-ria/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/canix/ros-tf-ria/install/lib/python2.7/dist-packages:/home/canix/ros-tf-ria/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/canix/ros-tf-ria/build" \
    "/usr/bin/python" \
    "/home/canix/ros-tf-ria/src/turtle_tf_3d/setup.py" \
    build --build-base "/home/canix/ros-tf-ria/build/turtle_tf_3d" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/canix/ros-tf-ria/install" --install-scripts="/home/canix/ros-tf-ria/install/bin"
