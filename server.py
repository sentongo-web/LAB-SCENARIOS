# # Building a RESTful Weather API using LangChain and LangServe

# ## Setup and Configuration

# Install LangServe and its dependencies
# ! pip install langserve[all]

# Install the nest_asyncio library
# ! pip install nest_asyncio

# Import LangChain components
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Import FastAPI and LangServe
from fastapi import FastAPI
from langserve import add_routes

# Import nest_asyncio
import nest_asyncio

# Assign the model name to be used in this project
MODEL = "gpt-4o-mini"


# ## LangChain Components

# Create the prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Extract the {weather_property} from the given weather description"),
    ("user", "{weather_description}")
])

# Create the model
model = ChatOpenAI(
    model=MODEL, 
    temperature=0, 
)

# Create the output parser
parser = StrOutputParser()

# Create the chain
chain = prompt_template | model | parser

# Test the chain
result = chain.invoke({
    "weather_property": "temperature",
    "weather_description": "Today is sunny, making it a perfect day to spend outdoors with clear skies and bright sunshine. As you step outside, you might feel a gentle breeze adding to the pleasant atmosphere. With temperatures reaching a comfortable 75 degrees Fahrenheit, it is an ideal time for outdoor activities or simply relaxing in the sun. Although the humidity is 25%, it can get a rainfall of 20mm daily."
})

print(result)


# ## Integrate LangServe with FastAPI

# Host the API endpoint using FastAPI
app = FastAPI(
    title="Weather Assistant",
    version="1.0",
    description="A simple weather report generator"
)

# Add weather route to the app
add_routes(
    app, 
    chain,
    path="/weather"
)


# ## Host the API

# Apply nest_asyncio to allow nested event loops in the notebook
nest_asyncio.apply()

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
