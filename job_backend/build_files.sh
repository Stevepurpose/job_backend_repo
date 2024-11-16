# Modify this line as needed for your package manager (pip, poetry, 
pip install -r requirements.txt

# Apply any outstanding database migrations
python3.9 manage.py migrate


# Convert static asset files
python3.9 manage.py collectstatic
