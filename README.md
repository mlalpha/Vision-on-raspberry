# Vision-on-raspberry

This is a Flask Application

# Installation Guide 
(Please download your vision api key and put insider the repo)
```
export GOOGLE_APPLICATION_CREDENTIALS=./vision.json
virtualenv env
source activate env/bin/activate
pip install -r requriement.txt
```

# Running the web api
```
export GOOGLE_APPLICATION_CREDENTIALS=./vision.json
source activate env/bin/activate
python app.py
```
gcloud auth application-default login