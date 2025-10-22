# you can switch the corresponding jetpack version
FROM ultralytics/ultralytics:latest-jetson-jetpack6

WORKDIR /app/fitness

COPY . /app/fitness