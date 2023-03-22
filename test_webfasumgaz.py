#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""Unit-tests for websumgaz program.
  Parameters
  ----------
      article_text : str
          Input text.

  Returns
  -------
      str
          Summary of input text.
"""


from fastapi.testclient import TestClient
from webfasumgaz import app

CLIENT = TestClient(app)


def test_read_webfasumgaz():
    """Test checks handling of empty GET request.
    """
    response = CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":  "Webfasumgaz application is online!"}


def test_read_empty():
    """Test checks handling of empty arg by prediction function.
    It sends to service empty string, after that it checks status
    and answer equation to string 'Error: text is absent.'
    """
    response = CLIENT.post("/predict/",
                           json={"text": ""}
                           )
    json_data = response.json()
    print("json_data =<", json_data, ">")
    assert response.status_code == 200
    assert json_data == 'Error: text is absent.'


def test_read_text():
    """Test checks prediction. It sends to service reference text
    from file "text1.txt" and compare responce with reference
    string from file "answer1.txt".
    """
    file = open("texts/text1.txt")
    f_data = file.read()
    file.close()

    response = CLIENT.post("/predict/",
                           json={"text": f_data}
                           )

    json_data = response.json()
    print("json_data = <", json_data, ">")
    file = open("texts/answer1.txt")
    reference_text = file.read()
    file.close()
    print("reference_data = <", reference_text, ">")
    assert response.status_code == 200
    # assert (reference_text.strip() in json_data) == True
    assert reference_text.strip() in json_data
