
# XML to Json converter
The goal of this project is to create a small tool that can convert predefined data sources that are delivered in an XML-format and convert these to a JSON format for later use with the JSON diff api (link) for later comparison. 
## How to run
`python3 start.py`
## Improvements
### Command line arguments.
One of the requirements on this tool was that it could be used as a scheduled task to read and convert multiple data sources that are released at different intervals and times. As of now the tool only reads and converts NSL but more data sources could be added at a later date. This would require the app to be able to take which data source to read as a command line argument. Suggested operation:
* No arguments: “python3 start.py” reads and converts all defined data sources
* With argument: “python3 start.py nsl” reads the data source named: “nsl” and converts it

### Replace simplejson with the JSON library from the python standard library
This project currently depends on simplejson(link) for JSON encoding. This should probably be replaced with the JSON library from the python standard library to minimize the dependencies on external libraries. 


