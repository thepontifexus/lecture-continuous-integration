FROM ros:melodic-ros-core

# Copy talker project folder to /app/src
COPY . /app/src
# Define work directory
WORKDIR /app

# Build the listener application
RUN bash -c "source /opt/ros/melodic/setup.bash && catkin_make listener"

