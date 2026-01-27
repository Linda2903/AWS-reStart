echo "start activation venv"

source venv/bin/activate

cd todolist

echo "ti trovi in: "

python manage.py makemigrations 
echo "le migrazioni sono state create, inizio a migrare"
python manage.py migrate