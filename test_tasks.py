import unittest
from services import app, get_db, init_db
from tasks import collect_weather
import json

class TestTasks(unittest.TestCase):

    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Clean the Data Base - every test
        with app.app_context():
            db = get_db()
            db.execute('DELETE FROM weather_data')
            db.execute('DELETE FROM requested_ID_weather')
            db.commit()
            
    def test_get_progress(self):
        with app.app_context():
            db = get_db()
            curr = db.execute('SELECT request_id AS rq FROM requested_ID_weather ORDER BY RANDOM() LIMIT 1')
            db.commit()
            
            result = curr.fetchone()

        if(result is not None):   
            request_id_DB = curr.fetchone()['rq'] 
            response = self.app.get('/weather/' + request_id_DB)
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data(as_text=True))
            print("Data progress")
            print(data['progress'])
            self.assertIsNotNone(data['progress'])
        else:
            print("EMPTY DB")
           #print(f"Request ID DB: {request_id_DB}")

    def test_post_weather(self):
        response = self.app.post('/weather', data=json.dumps({
            'user_id': 'user123',
            'city_ids': [3439525, 3439781, 3440645, 3442098, 3442778, 3443341, 3442233, 3440781,
                         3441572, 3441575, 3443207, 3442546, 3441287, 3441242, 3441686, 3440639,
                         3441354, 3442057, 3442585, 3442727, 3439705, 3441890, 3443411, 3440054,
                         3441684, 3440711, 3440714, 3440696, 3441894, 3443173, 3441702, 3442007,
                         3441665, 3440963, 3443413, 3440033, 3440034, 3440571, 3443025, 3441243,
                         3440789, 3442568, 3443737, 3440771, 3440777, 3442597, 3442587, 3439749,
                         3441358, 3442980, 3442750, 3443352, 3442051, 3441442, 3442398, 3442163,
                         3443533, 3440942, 3442720, 3441273, 3442071, 3442105, 3442683, 3443030,
                         3441011, 3440925, 3440021, 3441292, 3480823, 3440379, 3442106, 3439696,
                         3440063, 3442231, 3442926, 3442050, 3440698, 3480819, 3442450, 3442584,
                         3443632, 3441122, 3441475, 3440791, 3480818, 3439780, 3443861, 3440780,
                         3442805, 7838849, 3440581, 3440830, 3443756, 3443758, 3443013, 3439590,
                         3439598, 3439619, 3439622, 3439652, 3439659, 3439661, 3439725, 3439748,
                         3439787, 3439831, 3439838, 3439902, 3440055, 3440076, 3440394, 3440400,
                         3440541, 3440554, 3440577, 3440580, 3440596, 3440653, 3440654, 3440684,
                         3440705, 3440747, 3440762, 3440879, 3440939, 3440985, 3441074, 3441114,
                         3441377, 3441476, 3441481, 3441483, 3441577, 3441659, 3441674, 3441803,  
                         3441954, 3441988, 3442058, 3442138, 3442206, 3442221, 3442236, 3442238,
                         3442299, 3442716, 3442766, 3442803, 3442939, 3443061, 3443183, 3443256,
                         3443280, 3443289, 3443342, 3443356, 3443588, 3443631, 3443644, 3443697,
                         3443909, 3443928, 3443952, 3480812, 3480820, 3480822, 3480825]
        }), content_type='application/json')

        self.assertEqual(response.status_code, 202)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('request_id', data)

    
    def test_post_weather_missing_parameters(self):
        response = self.app.post('/weather', data=json.dumps({
            'user_id': '',
            'city_ids': []
        }), content_type='application/json')

        self.assertEqual(response.status_code, 422)
    
    def test_get_missing_parameters(self):
        response = self.app.get('/weather/' + "0")
        self.assertEqual(response.status_code, 422)



if __name__ == '__main__':
    unittest.main()
