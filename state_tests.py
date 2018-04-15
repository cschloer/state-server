import state
import unittest
import json

class StateTestCase(unittest.TestCase):

    def setUp(self):
        state.app.testing = True
        self.app = state.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        assert r._status_code == 405

    def test_no_params(self):
        r = self.app.post('/', data={})

        assert r._status_code == 400

    def test_bad_params(self):
        r = self.app.post('/', data={
            'longitude': 'test1',
            'latitude': 'test2',
        })

        assert r._status_code == 400

    def test_pennsylvania(self):
        r = self.app.post('/', data={
            'longitude': -77.036133,
            'latitude': 40.513799,
        })
        data = json.loads(r.get_data(as_text=True))

        assert r._status_code == 200
        assert len(data) == 1
        assert data[0] == 'Pennsylvania'

    def test_pacific_ocean(self):
        r = self.app.post('/', data={
            'longitude': -164.401727,
            'latitude': 31.617229,
        })
        data = json.loads(r.get_data(as_text=True))

        assert r._status_code == 200
        assert len(data) == 0

    def test_colorado_utah_corner(self):
        r = self.app.post('/', data={
            'longitude': -109.048314,
            'latitude': 40.998433,
        })
        data = json.loads(r.get_data(as_text=True))

        assert r._status_code == 200
        assert len(data) == 2
        assert data[0] == 'Utah'
        assert data[1] == 'Colorado'



if __name__ == '__main__':
    unittest.main()
