import logging
from flask import Blueprint, request, jsonify

app_02 = Blueprint('app_02', __name__)
logger = logging.getLogger()


@app_02.route('/app', methods=['POST'])
def app():
    try:
        param = request.get_json()
        logger.info(f'##########################')
        logger.info(f'app02')
        logger.info(f'##########################')
        logger.info(f'[REQ] {param}')

        return jsonify(status='OK')
    except Exception as e:
        logger.fatal(f'【システムエラー】{str(e)}：{str(request.get_json())}')
        return jsonify(status='NG', error_code=500, message='【システムエラー】処理に失敗しました。\n{}'.format(str(e)))


