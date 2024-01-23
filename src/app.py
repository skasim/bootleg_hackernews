# Imports
import os
from flask import Flask
from flask_graphql import GraphQLView
from dotenv import load_dotenv

load_dotenv()
from schema import schema
from modules import app

# Routes
app.add_url_rule(
    "/gql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.route("/")
def index():
    return "welcome to bootleg hacker rank"
if __name__ == "__main__":
    app.run(host=f"{os.getenv('GQL_HOST')}", port=5000)
