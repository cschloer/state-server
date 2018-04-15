# state-server
Only tested with Python 3.5.2


To run:
```
pip install -r requirements.txt;
cp .env.default .env;
set -a;
source .env;
python -m flask run;
```
Then curl http://127.0.0.1:5000/

To run tests:
```
pip install -r requirements.txt;
cp .env.default .env;
set -a;
source .env;
python state_tests.py
```

Note:

Heavily utilitized the ray-casting algorithm example found at
https://rosettacode.org/wiki/Ray-casting_algorithm

Also drew heavily for the algorithm to determine if a point is on a
line segment from here  https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment#answer-328110

Lastly, there is a Deprecation warning when you run the tests, it's something that will be fixed in the next release of Flask (https://github.com/pallets/flask/issues/2549)
