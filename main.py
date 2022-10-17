from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()


model_file = open('insurance_model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

class Msg(BaseModel):
    msg: str

class Req(BaseModel):
    age: int
    sex: int
    smoker: int
    bmi: float
    children: int
    region: int

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

@app.get("/predict/{path_id}")
async def predict(path_id: int):
     return {"message":  f"This is /predict/{path_id} endpoint, use post request to retrieve result"}
    
@app.post("/predict")
async def predict(requess: Req):
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age = requess.age
    sex = requess.sex
    smoker = requess.smoker
    bmi = requess.bmi
    children = requess.children
    region = requess.region
    data = []

    data.append(int(age))
    data.extend([int(sex)])
    data.extend([float(bmi)])
    data.extend([int(children)])
    data.extend([int(smoker)])
    data.extend([int(region)])  
    # if sex == 'Male':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if smoker == 'Yes':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)
    return {"message": f"Your annual insurance is: {output} USD"}        
    
#     #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)