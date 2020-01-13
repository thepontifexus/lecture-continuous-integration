FROM ros:melodic-ros-core

COPY . /app/src
WORKDIR /app
RUN bash -c "source /opt/ros/melodic/setup.bash && catkin_make listener"
