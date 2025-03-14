# Collaborative Storytelling App

## Overview
The Collaborative Storytelling App is a web application that allows users to register, create stories, and contribute to ongoing narratives. This platform fosters creativity and collaboration among users, enabling them to build stories together.

## Features
- User registration and login
- Create new stories
- Contribute to existing stories
- View stories contributed by the user

## Project Structure
```
collaborative-storytelling-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── register.html
│       ├── login.html
│       ├── create_story.html
│       └── contribute.html
├── instance
│   └── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd collaborative-storytelling-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the configuration:
   - Modify `instance/config.py` to set your secret key and any other necessary configurations.

## Usage
1. Run the application:
   ```
   flask run
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

3. Register a new account or log in with an existing account to start creating and contributing to stories.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.