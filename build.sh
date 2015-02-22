sudo apt-get -y update
sudo apt-get -y install vim
sudo apt-get -y install git
sudo apt-get -y install python-pip
pip install virtualenvwrapper
sudo pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh 
mkvirtualenv --python=`which python` python3env
#lsvirtualenv 
pip install django
sudo apt-get -y install add-apt-repository
sudo apt-get -y install python-software-properties
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get -y update
sudo apt-get -y install python3.4
mkvirtualenv --python=`which python3.4` python34env
workon python34env
pip install mysql-connector-python --allow-all-external
pip install django
sudo apt-get -y install mysql-server
