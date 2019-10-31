
# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess

from flask import Flask
from flask import request

app = Flask(__name__)
pascal_executable = '/app/roman'


@app.route('/')
def convert_to_roman():
    # Parameter must be bytes to send to spawned program
    number = request.args.get('number', 'N/A').encode()

    result = subprocess.run(pascal_executable, input=number, capture_output=True)

    if result.returncode != 0:
        # Maybe the user sent an invalid value (can't be read as an integer) or
        # maybe the Pascal program has an error. Not going to try to tell them
        # apart here, just say something went wrong.
        return result.stderr, 500
    elif result.stderr != b'':
        # The Pascal program wrote an error message, so this is a user error
        return result.stderr, 400
    else:
        return result.stdout, 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))