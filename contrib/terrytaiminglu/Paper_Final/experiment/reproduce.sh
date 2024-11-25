conda create -n privacy python=3.9
conda activate privacy

pip install datasets spacy tqdm matplotlib pandas seaborn openai
!python -m spacy download en_core_web_sm

python analysis.py