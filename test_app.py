from app import app
import json

def test_songs():
    response = app.test_client().get('/songs/<string:name>')

    json_data = json.loads(response.data)
    assert json_data == [
  "Fill Me Up (Live)", 
  "Nobody Greater", 
  "His Blood Still Works", 
  "Chasing After You", 
  "You Reign", 
  "Status", 
  "Turning Around for Me", 
  "Be Fruitful (live)", 
  "Joy", 
  "My Worship is For Real by Vashawn Mitchell"
]
    assert response.status_code == 200

