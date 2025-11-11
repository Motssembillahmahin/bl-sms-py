# Banglalink SMS API

> A modern, fast, and production-ready FastAPI wrapper for Banglalink Bulk SMS services

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

A high-performance Python SDK and REST API gateway for integrating Banglalink operator bulk SMS services. Send promotional messages, OTPs, and transactional SMS with ease using FastAPI's async capabilities.[web:21][web:22]

## ✨ Features

- **Fast & Async**: Built on FastAPI for high-performance async SMS operations[web:22]
- **Bulk SMS**: Send messages to thousands of recipients efficiently
- **Delivery Reports**: Track message delivery status with webhook support
- **Authentication**: Secure API key-based authentication
- **Rate Limiting**: Built-in rate limiting to prevent API abuse
- **Type Safety**: Full Pydantic validation for request/response models[web:22]
- **Auto Documentation**: Interactive API docs with OpenAPI/Swagger UI[web:22]
- **Production Ready**: Docker support, logging, and error handling included

## 🚀 Quick Start

### Prerequisites

- Python 3.7+[web:22]
- Banglalink SMS API credentials
- `pip` or `uv` package manager

### Installation
Clone the repository
```bash
https://github.com/Motssembillahmahin/bl-sms-py.git
cd bl-sms-py
 ```
###  Install Dependencies

```bash
uv pip install  uvicorn fastapi httpx
```
or
```bash
uv sync
```

This command will automatically:
- Detect or download the appropriate Python version
- Create a virtual environment in `.venv`
- Install all project dependencies from `pyproject.toml`
- Generate/update the `uv.lock` lockfile

### Activate Virtual Environment (Optional)

**Linux/macOS**
```bash
.venv\bin\activate
```
**Windows**
```bash
.venv\Scripts\activate
```

### 5. Configure Environment Variables

Create a `.env` file in your project root with the following variables:

```dotenv
bl_base_dir=https://corpsms.banglalink.net/bl/api/v1/smsapigw/
bl_username=username
bl_password=password
bill_msisdn=msisdn
```
 or 
``` bash 
cp .env.example .env
```
### Run the Application

**Using just**
```bash
just run
```

The API will be available at `http://localhost:8000`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The amazing web framework[web:22]
- [Banglalink](https://www.banglalink.net/) - SMS service provider
- All contributors who help improve this project

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/banglalink-sms-api/issues)
- **Email**: asmahin8@gmail.com

## 🗺️ Roadmap

- [ ] Add support for MMS
- [ ] Implement message scheduling
- [ ] Add support for multiple operators (Grameenphone, Robi)
- [ ] Create Python SDK package
- [ ] Add Redis caching for rate limiting
- [ ] Implement message queue with Celery
- [ ] Add monitoring with Prometheus/Grafana

---

**Made with ❤️ for the Bangladesh developer community**
