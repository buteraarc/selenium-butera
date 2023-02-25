#install docker

docker run -p 6080:80 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc

nomachine:

curl -sLkO https://is.gd/nomachinewindows10 ; bash nomachinewindows10

curl -sLkO https://is.gd/nomachinewine ; bash nomachinewine

curl -sLkO https://is.gd/nomachineMATE ; bash nomachineMATE

curl -sLkO https://is.gd/nomachinexfce4 ; bash nomachinexfce4


# selenium-butera

install chrome ubuntu 

1. wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

2. sudo apt update

3. sudo apt install -f ./google-chrome-stable_current_amd64.deb -y

install webdriver

1. mkdir tests && cd tests

2. apt-get install python3-venv -y

3. python3 -m venv venv

4. source venv/bin/activate

5. pip install selenium webdriver-manager
