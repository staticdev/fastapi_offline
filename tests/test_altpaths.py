from fastapi.testclient import TestClient
from fastapi import FastAPI
from fastapi_offline import FastAPIOffline

DOC = "/asdf"
REDOC = "/qwerty"

# Custom paths for both
app1 = FastAPIOffline(docs_url=DOC, redoc_url=REDOC)
client1 = TestClient(app1)

# Disable redoc
app2 = FastAPIOffline(docs_url=DOC, redoc_url=None)
client2 = TestClient(app2)

# Disable Swagger
app3 = FastAPIOffline(docs_url=None, redoc_url=REDOC)
client3 = TestClient(app3)


def test_swagger():
    """Make sure Swagger appears at the right place"""
    assert client1.get("/docs").status_code == 404
    assert client1.get(DOC).status_code == 200

    assert client2.get("/docs").status_code == 404
    assert client2.get(DOC).status_code == 200

    assert client3.get("/docs").status_code == 404
    assert client3.get(DOC).status_code == 404


def test_custom_redocs():
    """Make sure Redoc appears at the right place"""
    assert client1.get("/redoc").status_code == 404
    assert client1.get(REDOC).status_code == 200

    assert client2.get("/redoc").status_code == 404
    assert client2.get(REDOC).status_code == 404

    assert client3.get("/redoc").status_code == 404
    assert client3.get(REDOC).status_code == 200
