import os
import redis

from flask import Flask

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
cache = redis.StrictRedis(host=redis_host, port="6379", db=0, decode_responses=True)


@app.route('/ping')
def status_ok():  # put application's code here
    return {"status": "ok"}


@app.route('/count')
def visiter_counter():  # put application's code here
    count_visit = cache.get('count_visit')

    count_visit = int(count_visit) + 1 if count_visit else 1

    cache.set('count_visit', count_visit)

    return f"Visit count: {count_visit}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
