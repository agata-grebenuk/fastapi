from fastapi import FastAPI
# точки входа эмпоинт
app = FastAPI(
    title="MyApp",
    docs_url="/documentation",
    redoc_url= None
)

app_users = [
    {"id": 1, "role": "admin", "name": "Dog"},
    {"id": 2, "role": "margen", "name": "agan"},
    {"id": 3, "role": "user", "name": "hepi"}
]

trades = [
    {"id": 1,"user_id": 1, "currency": "BTC", "side": "buy", "price": 123,},
    {"id": 2,"user_id": 1, "currency": "BTC", "side": "buy", "price": 123,},
    {"id": 3,"user_id": 2, "currency": "BTC", "side": "buy", "price": 123,}
]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in app_users if user["id"] == user_id]



@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list( filter(lambda user: user.get("id") == user_id, app_users) )[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

@app.get("/trades")
def get_trades(limit: int = 10, offset: int = 0):
    return trades[offset:][:limit]
