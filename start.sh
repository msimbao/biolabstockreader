# For development use (simple logging, etc):
# python3 -m nltk.downloader universal_tagset
# python3 -m spacy download en 

# wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
# tar -xvf  s2v_reddit_2015_md.tar.gz

python3 app.py
# For production use: 
# gunicorn server:app -w 1 --log-file -