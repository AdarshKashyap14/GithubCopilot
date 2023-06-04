# GithubCopilot
# Weather Forecasting Tool

This command-line tool is built in Python and utilizes the OpenWeatherMap API to retrieve the current weather forecast for a given city. The tool demonstrates the usage of GitHub Copilot to assist with API usage, data parsing, and error handling.

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Obtain an API key from OpenWeatherMap. Visit [OpenWeatherMap API](https://openweathermap.org/api) to sign up and get your API key.

4. Create a `.env` file in the project root directory and add the following line:

```bash
API_KEY=YOUR_API_KEY
```
Replace `YOUR_API_KEY` with the API key obtained from OpenWeatherMap.

## Usage

Run the tool using the following command:

```bash
python weather_tool.py
```

The tool will prompt you to enter the name of a city. Type the name of the city and press Enter.

The tool will then retrieve the current weather forecast for the specified city using the OpenWeatherMap API. The forecast will include information such as temperature, humidity, wind speed, and weather conditions.

## GitHub Copilot Usage

GitHub Copilot has been instrumental in developing this tool by providing AI-powered code suggestions for various tasks:

1. API Usage: Copilot assists in generating code snippets to make API calls to the OpenWeatherMap API and fetch weather data.

2. Data Parsing: Copilot suggests efficient code snippets for parsing the received JSON data and extracting the necessary information for the weather forecast.

3. Error Handling: Copilot provides suggestions for handling errors and exceptions, ensuring a robust and reliable tool.

## Example Output

```
Enter the name of a city: London

Weather Forecast for London:
Temperature: 17°C
Humidity: 70%
Wind Speed: 12 km/h
Weather Condition: Clouds
```

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore the code, experiment with GitHub Copilot, and enhance the tool based on your requirements. Happy forecasting!
