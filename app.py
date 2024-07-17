from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle  

app = Flask(__name__)
CORS(app)

# Loading pre-trained recommendation model
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)
with open('movie_list.pkl','rb') as file:
    new = pickle.load(file)

print(new)
print(similarity)
def recommendmovie(movie):
    index = new[new['title'] == movie].index[0]
    print(index)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    ans = []
    for i in distances[1:16]:
        ans.append(new.iloc[i[0]].title)
    print(ans)
    return ans
recommendations = recommendmovie('Kung Fu Panda 2')
print(recommendations)
@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie')
    if not movie_name:
        return jsonify({'error': 'Please provide a movie name'}), 400

    try:
        recommendations = recommendmovie(movie_name)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
   

if __name__ == '__main__':
    app.run(debug=True,port=8080)
