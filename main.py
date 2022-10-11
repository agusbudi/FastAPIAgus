from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()


model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}


@app.post("/predict")
async def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, sex, smoker = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    if sex == 'Laki-laki':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if smoker == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)
    
    return {"it works"}
    #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)
