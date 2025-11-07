cd ~
git clone https://github.com/SrinidhiPRao/PAGE-LMS.git
cd PAGE-LMS
python3 -m venv .venv
source .venv/bin/activate


pip install -r requirements.txt

uvicorn backend.main:app --host 0.0.0.0 --port 8000
