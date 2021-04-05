from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from mypostgresql import *

if __name__ == '__main__':
	db.bind(provider='postgres', user='postgres', password='xpj', host='172.17.0.2', database='runoobdb')
	db.generate_mapping(create_tables=True)


	app = FastAPI()
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)


	@app.get("/")
	async def root():
		return {"message": "Hello World"}

	@app.post("/User")
	def create_user(name: str, password: str):
		add_user(name, password)
	@app.get("/User")
	def find_user_password(name: str):
		return find_user_password_by_name(name)

	uvicorn.run(app,host="127.0.0.1",port=8000)

