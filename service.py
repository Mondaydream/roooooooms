
from flask import *
import json
from db import *
import copy
from conf import *

app = Flask(__name__)


resp = {
    'result': [],
    'desc': '请求成功',
    'statusCode': 0
}


@app.route('/v1/city/queryRentRooms', methods=['GET'])
def add_post():
    city = request.args.get('city', '')
    circle = request.args.get('cityCircle', '')
    num = request.args.get('pageNumber', 0)
    size = request.args.get('pageSize', 10)

    res = search_rentRooms(city, circle, num, size)
    r = resp.deepcopy(resp)  
    r['result'] = res
    return json.dumps(r)

@app.route('/queryRoom', methods=['GET'])
def queryEstatle():
    rid = request.args.get('roomID', '')
    res = search_root(rid)
    r = resp.deepcopy(resp)
    if len(res) > 0:
        r['result'] = [res]
    return json.dumps(r)
    
    

@app.route('/queryEstatle', methods=['GET'])
def queryEstatle():
    eid = request.args.get('estatleID', '')
    etitle = request.args.get('estatleTitle', '')
    num = request.args.get('pageNumber', 0)
    size = request.args.get('pageSize', 10)
    res = search_estatle(eid, etitle, num, size)
    r = resp.deepcopy(resp)
    r['result'] = res
    return json.dumps(r)


@app.route('/uploadPhoneNumber', methods=['POST'])
def upload_phone():
    try:
        dt = request.get_data()
        data = json.loads(dt)
    except BaseException as e:
        print (e)
    
    insert_phone(data['phoneNumber'])
    r = resp.deepcopy(resp)
    return json.dumps(r)

if __name__ == '__main__':
    app.run(host = server_port, port=server_port)
