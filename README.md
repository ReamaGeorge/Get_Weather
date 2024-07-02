# Get_Weather


A Flask-based web application that provides an API endpoint to greet a visitor and display the current weather in their location.

## Features

- **API Endpoint**: `/api/hello`
  - Accepts a `visitor_name` parameter to personalize the greeting.
  - Returns a JSON response with the visitor's IP address, city based on IP, and current temperature in Celsius.

## How to Use

### Setup

1. **Clone the repository**:

2. **Set API keys**:
   - Replace placeholders in `app.py` with your actual OpenWeatherMap and IPinfo API keys.

### Local Development

 **Access the API**:
   Open your browser and go to `http://127.0.0.1:5000/api/hello?visitor_name=Mark`.

### Deployment on PythonAnywhere

1. **Upload files**:
   - Upload your project files to PythonAnywhere.

2. **Configure WSGI**:
   - Edit the WSGI configuration to point to your Flask application.

3. **Reload web app**:
   - Use PythonAnywhere dashboard to reload your web app.

## Example

### Request

```bash
curl "http://yourusername.pythonanywhere.com/api/hello?visitor_name=Mark"
```

### Response

```json
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, Mark!, the temperature is 11 degrees Celsius in New York"
}
```
### Challenge
{"error":"Could not retrieve location or weather information"}

Need to rectify the error.
