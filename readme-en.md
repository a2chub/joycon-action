# Joycon Action

A web application built with Streamlit.

## Overview

This project provides a web application that runs in browsers using Python and mini JavaScript. It's built on the Streamlit framework with a modular and extensible design.

## Tech Stack

- **Backend**: Python 3.8+
- **Frontend**: Streamlit + JavaScript
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Altair

## Project Structure

```
joycon-action/
├── docs/                    # Documentation
│   ├── architecture.md      # Architecture design
│   ├── development.md       # Development guide
│   └── api.md              # API specification
├── src/                     # Source code
│   ├── main.py             # Main application
│   ├── components/         # Reusable components
│   └── utils/              # Utility functions
├── static/                  # Static files
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Application

```bash
streamlit run src/main.py
```

### 3. Access

Access http://localhost:8501 in your browser.

## Features

### Current Features
- Hello World display
- Interactive UI
- Navigation system
- Responsive design
- Chart display demo

### Planned Features
- User authentication
- Database integration
- API integration
- Custom components

## Development

### Setting up Development Environment

1. Install Python 3.8 or higher
2. Create virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Adding New Features

1. Create new components in `src/components/`
2. Add pages to `src/main.py`
3. Update documentation in `docs/` as needed

For detailed development guide, see `docs/development.md`.

## Documentation

- [Architecture Design](docs/architecture.md)
- [Development Guide](docs/development.md)
- [API Specification](docs/api.md)

## License

This project is released under the MIT License.

## Contributing

Contributions to the project are welcome. Please report bugs or feature requests through GitHub Issues.

## Support

For technical questions or issues, please contact the development team.