from app import app
from tasks import run

if __name__ == "__main__":
    run.delay()
