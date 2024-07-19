import pickle  
import streamlit as st

st.title("MovieMate")

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
    for i in distances[1:6]:
        ans.append(new.iloc[i[0]].title)
    print(ans)
    return ans

input_data = st.selectbox('Enter the Movie Name:',new['title'].values)
if input_data:
    if st.button("Recommend"):

        result = recommendmovie(input_data)  
        for i in result:
            st.write(i)

