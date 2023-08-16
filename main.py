import os
import pyodbc
import uvicorn
import pandas as pd
from fastapi import FastAPI
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PK = os.environ["PK"]
PSW = os.environ["PSW"]
BATCH = os.environ["BATCH"]
SERVER = os.environ["SERVER"]
DRIVER = os.environ["DRIVER"]
DELAY = int(os.environ["DELAY"])
INSTANCE = os.environ["INSTANCE"]
DATABASE = os.environ["DATABASE"]
USERNAME = os.environ["USERNAME"]
FOLDER_D = os.environ["FOLDER_D"]

CONEXION_BD = 'DRIVER=' + DRIVER + ';SERVER=tcp:' + SERVER + ';PORT=1433;DATABASE=' + DATABASE + ';UID=' + USERNAME + ';PWD=' + PSW


@app.get("/send_data/")
async def send_data(user: str, bpm: float, spo2: int):
    """
    This function send data to IPFS with AWS endpoint
    :param user: str, user identifier
    :param bpm: float, user data BPM
    :param spo2: int, user SpO2
    :return: json object
    """
    df_sensor = pd.read_csv('temp_data/temp_data.csv', index_col=0)

    date_c = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    data = {'BPM': bpm,
            "SPO2": spo2,
            'DATE_C': date_c,
            'USER': user}

    df_data = pd.DataFrame([data])
    df_sensor = pd.concat([df_sensor, df_data], ignore_index=True, axis=0)

    bpm = data.get('BPM')
    spo2 = data.get('SPO2')
    date_c = data.get('DATE_C')
    user_data = data.get('USER')

    with pyodbc.connect(CONEXION_BD) as conn:
        with conn.cursor() as cursor:
            count = cursor.execute(
                f"INSERT INTO {INSTANCE} (BPM, SPO2, DATE_C, USER_DATA) VALUES ({bpm}, {spo2}, '{date_c}', '{user_data}');").rowcount
            conn.commit()
            print(f'Rows inserted: {str(count)}')

    df_sensor.to_csv('temp_data/temp_data.csv')

    json_resp = jsonable_encoder(data)

    return JSONResponse(content=json_resp)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
