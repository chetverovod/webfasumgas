#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fastapi.testclient import TestClient
from fasumgaz import app

client = TestClient(app)


def test_read_fasumgaz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":  "Fasumgaz application is online!"}


def test_read_empty():
    response = client.post("/predict/",
        json={"text": ""}
    )
    json_data = response.json() 
    print("json_data =<", json_data, ">" )
    assert response.status_code == 200
    assert json_data == 'Error: text is absent.'


def test_read_text():
    f = open("texts/text1.txt")
    fd = f.read()
    f.close()
    response = client.post("/predict/",
        json={ "text": fd }
    )
    json_data = response.json() 
    print("json_data = <", json_data, ">" )
    f = open("texts/answer1.txt")
    reference_text = f.read()
    f.close()
    print("reference_data = <", reference_text, ">" )
    assert response.status_code == 200
    assert ( reference_text.strip() in json_data ) == True


