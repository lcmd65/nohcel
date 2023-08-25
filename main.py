from app.view.view import loginViewQT
import gc

if __name__ == "__main__":
    loginViewQT()
    gc.collect()
    

# python3 -m pip install -r requirements.txt
# python3 -m venv .env
# source .env/bin/activate