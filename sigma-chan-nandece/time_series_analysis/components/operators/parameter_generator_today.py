# coding: utf-8

import datetime

def obtain_todays_inference_parameter(duration: int) -> dict:
    today = str(datetime.datetime.now().strftime("%Y/%m/%d"))
    today_without_slash = today.replace("/", "")
    data_save_path = f"data/fx/dexjpus_{today_without_slash}.npy"

    parameter_dict = {
        "source": "fred",
        "target": "DEXJPUS",
        "end": today,
        "duration": str(duration),
        "data_save_path": data_save_path
    }

    return parameter_dict
