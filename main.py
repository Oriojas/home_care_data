import os
import uvicorn
import psycopg2
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

USERNAME_DB = os.environ["USERNAME_DB"]
PASSWORD_DB = os.environ["PASSWORD_DB"]
URL_DB = os.environ["URL_DB"]


@app.get("/send_data/")
async def send_data(user: str, bpm: float, spo2: int):
    """
    This function send data to IPFS with AWS endpoint
    :param user: str, user identifier
    :param bpm: float, user data BPM
    :param spo2: int, user SpO2
    :return: json object
    """

    conn = psycopg2.connect(host=URL_DB,
                            port="5432",
                            database="postgres",
                            user=USERNAME_DB,
                            password=PASSWORD_DB)

    cursor = conn.cursor()

    df_sensor = pd.read_csv('temp_data/temp_data.csv', index_col=0)

    date_c = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    data = {'bpm': bpm,
            "spo2": spo2,
            'date_c': date_c,
            'user': user}

    df_data = pd.DataFrame([data])
    df_sensor = pd.concat([df_sensor, df_data], ignore_index=True, axis=0)

    bpm = data.get('bpm')
    spo2 = data.get('spo2')
    date_c = data.get('date_c')
    user_data = data.get('user')

    try:
        cursor.execute(f"INSERT INTO public.data_sensors (bpm, spo2, date_c, user_data) VALUES ({bpm}, {spo2}, '{date_c}', '{user_data}');")

        conn.commit()
        cursor.close()
        conn.close()
        json_resp = jsonable_encoder(data)

    except Exception as exception:

        json_resp = jsonable_encoder({'bpm': False,
                                      "spo2": False,
                                      'date_c': False,
                                      'user': False})
        print("Exception query: ")
        print(exception)

    df_sensor.to_csv('temp_data/temp_data.csv')
    return JSONResponse(content=json_resp)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
