# AI Developer Performance Prediction

A complete machine learning solution for predicting developer performance metrics. This project includes both a **FastAPI REST API** and an **interactive Streamlit web interface** that analyzes various developer metrics including code output, AI tool usage, cognitive load, and task duration to provide performance predictions.

## 🚀 Features

- **REST API** built with FastAPI for programmatic access
- **Interactive Web UI** built with Streamlit for user-friendly predictions
- **Machine Learning Model** for performance prediction
- **Docker Support** for easy deployment
- **Real-time Predictions** based on developer metrics
- **Interactive API Documentation** with Swagger UI

## 📋 Prerequisites

- Docker Desktop (recommended for API)
- OR Python 3.8+ with pip (for local development)
- Streamlit (for web UI)

## 🐳 Quick Start with Docker

### Pull from Docker Hub

```bash
docker pull YOUR_USERNAME/my-api:latest
docker run -d -p 8080:80 --name my-api YOUR_USERNAME/my-api:latest
```

### Build Locally

```bash
# Clone the repository
git clone <your-repo-url>
cd <project-directory>

# Build the Docker image
docker build -t my-api:latest .

# Run the container
docker run -d -p 8080:80 --name my-api my-api:latest
```

## 🎨 Streamlit Web Interface

### Run the Interactive UI

```bash
# Install Streamlit and dependencies
pip install streamlit pandas joblib scikit-learn

# Run the Streamlit app
streamlit run streamlit.py
```

The web interface will automatically open in your browser at `http://localhost:8501`

### Using the Streamlit UI

1. **Select Input Parameters** from the sidebar:
   - Lines of Code (50-2000)
   - AI Usage Hours (1-24)
   - Cognitive Load (20-100)
   - Task Duration Hours (input manually)
   - Errors (input manually)

2. **Review Your Selection** in the main panel

3. **Click "Predict"** to get the predicted Task Success Rate

4. **View Results** displayed on the screen

## 🔧 Local Development Setup

### For FastAPI (REST API)

```bash
# Install dependencies
pip install fastapi uvicorn joblib pandas scikit-learn pydantic

# Run the API
uvicorn api:app --host 0.0.0.0 --port 80
```

### For Streamlit (Web UI)

```bash
# Install dependencies
pip install streamlit pandas joblib scikit-learn

# Run the Streamlit app
streamlit run streamlit.py
```

### Install All Dependencies at Once

```bash
pip install fastapi uvicorn streamlit joblib pandas scikit-learn pydantic
```

## 📡 API Usage

### Endpoint

**POST** `/predict`

### Request Body

```json
{
  "Lines_of_Code": 500,
  "AI_Usage_Hours": 3,
  "Cognitive_Load": 7,
  "Task_Duration_Hours": 4.5,
  "Errors": 2.0
}
```

### Response

```json
{
  "prediction": 85.5
}
```

### Example with cURL

```bash
curl -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Lines_of_Code": 500,
    "AI_Usage_Hours": 3,
    "Cognitive_Load": 7,
    "Task_Duration_Hours": 4.5,
    "Errors": 2.0
  }'
```

### Example with Python

```python
import requests

url = "http://localhost:8080/predict"
data = {
    "Lines_of_Code": 500,
    "AI_Usage_Hours": 3,
    "Cognitive_Load": 7,
    "Task_Duration_Hours": 4.5,
    "Errors": 2.0
}

response = requests.post(url, json=data)
print(response.json())
```

## 🎯 Which Interface Should I Use?

| Feature | FastAPI (REST API) | Streamlit (Web UI) |
|---------|-------------------|-------------------|
| **Best For** | Integration with other apps | Quick testing & demos |
| **Access Method** | HTTP requests | Web browser |
| **Use Case** | Production deployments | Data scientists, quick predictions |
| **Port** | 8080 | 8501 |
| **Documentation** | Auto-generated Swagger UI | Interactive sidebar |
| **Deployment** | Docker, cloud platforms | Streamlit Cloud, local |

## 📊 Input Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `Lines_of_Code` | integer | Number of lines of code written | 500 |
| `AI_Usage_Hours` | integer | Hours spent using AI tools | 3 |
| `Cognitive_Load` | integer | Cognitive load score (1-10) | 7 |
| `Task_Duration_Hours` | float | Time spent on task in hours | 4.5 |
| `Errors` | float | Number of errors encountered | 2.0 |

## 📚 Interactive Documentation

### FastAPI Documentation

Once the API is running, access the interactive documentation at:

- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

### Streamlit Web Interface

Once Streamlit is running, access the web UI at:

- **Streamlit UI**: http://localhost:8501

## 🛠️ Project Structure

```
.
├── api.py                                          # FastAPI application
├── streamlit.py                                    # Streamlit web interface
├── Dockerfile                                      # Docker configuration
├── AI_Developer_Performance.joblib                 # Trained ML model
├── AI_Developer_Performance_Extended_1000.ipynb    # Model training notebook
└── README.md                                       # This file
```

## 🔍 How It Works

1. The API receives developer metrics via POST request
2. Input data is validated using Pydantic models
3. The pre-trained machine learning model processes the metrics
4. A performance prediction is returned

## 🚢 Deployment

### FastAPI (Docker Hub)

```bash
# Tag your image
docker tag my-api:latest YOUR_USERNAME/my-api:latest

# Push to Docker Hub
docker push YOUR_USERNAME/my-api:latest
```

### Streamlit Cloud (Free Hosting)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy `streamlit.py`
5. Your app will be live at `https://your-app.streamlit.app`

### Cloud Platforms (API)

This Docker container can be deployed to:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- Heroku
- DigitalOcean App Platform

## 🧪 Testing

### Test the FastAPI

Test the health of your API:

```bash
# Check if the API is running
curl http://localhost:8080/docs

# Make a test prediction
curl -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Lines_of_Code": 1000,
    "AI_Usage_Hours": 5,
    "Cognitive_Load": 6,
    "Task_Duration_Hours": 8.0,
    "Errors": 1.5
  }'
```

### Test the Streamlit UI

1. Run `streamlit run streamlit.py`
2. Open browser at http://localhost:8501
3. Adjust the input parameters in the sidebar
4. Click "Predict" to see results
5. Try different combinations to test the model

## 📝 Model Information

The machine learning model (`AI_Developer_Performance.joblib`) was trained on developer performance data to predict productivity metrics based on:
- Code output volume
- AI assistance utilization
- Mental workload
- Time management
- Error rates

See `AI_Developer_Performance_Extended_1000.ipynb` for model training details.

## 🐛 Troubleshooting

### FastAPI Issues

**Container not starting**
```bash
# Check logs
docker logs my-api

# Restart container
docker restart my-api
```

**Port already in use**
```bash
# Use a different port
docker run -d -p 8081:80 --name my-api my-api:latest
```

### Streamlit Issues

**Port 8501 already in use**
```bash
# Run on a different port
streamlit run streamlit.py --server.port 8502
```

**Model file not found**
```bash
# Make sure the model file is in the same directory
ls AI_Developer_Performance.joblib
```

**Streamlit not opening in browser**
```bash
# Manually open the URL
# http://localhost:8501
```

### General Issues

**Model file not found**
Ensure `AI_Developer_Performance.joblib` is in the same directory as both `api.py` and `streamlit.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

YOUR_NAME

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Web UI with [Streamlit](https://streamlit.io/)
- Machine Learning with [scikit-learn](https://scikit-learn.org/)
- Containerized with [Docker](https://www.docker.com/)

---

**Note**: Replace `YOUR_USERNAME` and `YOUR_NAME` with your actual Docker Hub username and name before publishing.
