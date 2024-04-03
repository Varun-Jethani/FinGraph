
echo "Build Start"
python3.9 -m pip install --upgrade pip

pip install -r req2.txt
echo "Requirements installed"
python3.9 manage.py collectstatic --no-input --clear
echo "Build End"