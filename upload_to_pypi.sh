echo 'Install the requirements-pypi.txt...'
sudo pip install -r requirements-pypi.txt

echo 'Do you really want to upload this package? [y/n]'
read ANSWER

case $ANSWER in
    'y') 
        echo 'Uploading started...'
        python3 setup.py sdist
        twine upload dist/*
        ;;
    'n')
        echo 'Cancelation...'
        ;;
esac