# coding: utf-8

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

finish_stats = [
    {
        'id': 0,
        'player_name': u'Alpha',
        'time': 999999999,
        'level': 0
    },
    {
        'id': 1,
        'player_name': u'Beta',
        'time': 1000000000,
        'level': 0
    }
]


def sort_finish_stats():
    finish_stats.sort(key=lambda x: x['time'])


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/finish_stats/<int:stat_id>', methods=['GET'])
def get_stat(stat_id):
    stat = [stat for stat in finish_stats if stat['id'] == stat_id]
    if len(stat) == 0:
        abort(404)
    return jsonify({'stat': stat[0]})


@app.route('/finish_stats', methods=['GET'])
def get_stats():
    return jsonify({'stats': finish_stats})


@app.route('/finish_stats', methods=['POST'])
def create_stat():
    print(request.json)
    if not request.json or \
            'player_name' not in request.json or \
            'time' not in request.json or \
            'level' not in request.json:
        abort(400)
    stat = {
        'id': len(finish_stats),
        'player_name': request.json['player_name'],
        'time': request.json['time'],
        'level': request.json['level']
    }
    finish_stats.append(stat)
    sort_finish_stats()
    return jsonify({'stat': stat}), 201


@app.route('/finish_stats/<int:stat_id>', methods=['PUT'])
def update_stat(stat_id):
    stat = [stat for stat in finish_stats if stat['id'] == stat_id]
    if len(stat) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'player_name' in request.json and type(request.json['player_name']) is not str:
        abort(400)
    if 'time' in request.json and type(request.json['time']) is not int:
        abort(400)
    if 'level' in request.json and type(request.json['level']) is not int:
        abort(400)
    stat[0]['player_name'] = request.json.get('player_name', stat[0]['player_name'])
    stat[0]['time'] = request.json.get('time', stat[0]['time'])
    stat[0]['level'] = request.json.get('level', stat[0]['level'])
    sort_finish_stats()
    return jsonify({'stat': stat[0]})


@app.route('/finish_stats/<int:stat_id>', methods=['DELETE'])
def delete_stat(stat_id):
    stat = [stat for stat in finish_stats if stat['id'] == stat_id]
    if len(stat) == 0:
        abort(404)
    finish_stats.remove(stat[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host='0.0.0.0')
