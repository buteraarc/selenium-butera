#install docker

docker run -p 6080:80 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc


# selenium-butera

install chrome ubuntu 

1. wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

2. sudo apt update

3. sudo apt install -f ./google-chrome-stable_current_amd64.deb -y

install webdriver

1. mkdir tests && cd tests

2. python3 -m venv venv

3. source venv/bin/activate

4. pip install selenium webdriver-manager
