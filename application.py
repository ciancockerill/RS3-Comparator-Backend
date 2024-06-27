from flask import Flask, jsonify, request

import api_request
import rs_data_processor

# In regular use, a Flask instance is called app. However in AWS EB, it searches for callable "application".
application = Flask(__name__)


@application.route('/rs3player', methods=['GET'])
def get_runescape_data():
    # http request would be .../rs3player?user=playerName
    playerName = request.args.get('user')
    requestedData = api_request.requestPlayerData(playerName)
    formattedData = rs_data_processor.DataProcessor(requestedData).getFormattedData()

    return jsonify(formattedData)


if __name__ == '__main__':
    application.run(debug=False)
