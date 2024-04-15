
echo "Build Start"
python3.9 -m pip install --upgrade pip
echo "apt start"
sudo apt-get update
sudo apt-get install gcc libmysqlclient-dev python3-dev
echo "apt end"
pip install -r requirements.txt
echo "Requirements installed"
python3.9 manage.py collectstatic --no-input --clear
echo "Build End"