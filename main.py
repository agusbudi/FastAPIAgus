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
    bmi: float
    children: int
    smoker: int
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
    age: requess.age
    sex: requess.sex
    bmi: requess.bmi
    children: requess.children
    smoker: requess.smoker
    region: requess.region
    data = []

#     data.append(int(age))
#     data.append(int(sex))
#     data.append(float(bmi))
#     data.append(int(children))
#     data.append(int(smoker))
#     data.append(int(region))
    
#     prediction = model.predict([data])
#     output = round(prediction[0], 2)
    output= 1
    return {"message": f"Your annual insurance is: {output} USD"}        
    
#     #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)
