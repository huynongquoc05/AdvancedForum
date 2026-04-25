from flask import Flask
import os
import redis

app = Flask(__name__)
# Đảm bảo Redis server đang chạy ở background trên port 6379 nhé
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)

@app.route('/')
def hello():
    # Mỗi lần có người truy cập, tăng biến đếm 'hits' lên 1

    return f'Hello! This page has been visited {cache.incr("hits")} times.'

if __name__ == '__main__':
     # Gán host='::' để Flask lắng nghe trên IPv6
     app.run(host='::', port=5000)