from sanic import Sanic
from sanic.response import json, html, file, text
import aiohttp
import asyncio
import os
from sanic.request import RequestParameters

import time

BASE = os.getcwd()

app = Sanic()
app.static('/src', BASE + '/src')

app.static('/', BASE)
app.static('/main.js', './dist/main.js', name='main.js')


@app.route('/')
async def index(request):
    return await file('./dist/index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8000)),
        workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
        debug=bool(os.environ.get('DEBUG', '')))

'''
Sanic - React App

'''



