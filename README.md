
# My Server Project

## Overview

My Server Project is a Python-based web server that allows you to host an HTML website with a customizable domain name. This project is built using Flask, a lightweight WSGI web application framework, to serve static files and make your local development environment mimic a real-world scenario where you can access your site using a custom domain without specifying a port number.

## Features

- **Custom Domain Support:** Easily configure and access your website using a custom domain name.
- **Static File Serving:** Serve HTML, CSS, JavaScript, and other static files from a predefined directory.
- **Port-Free Access:** Optionally configure the server to run on port 5000, allowing you to access your site without specifying a port number in the URL.
- **Easy Configuration:** Simple and flexible configuration through a single `config.py` file.
- **Local Development Mimicking Real-World Deployment:** Test and develop your website locally as if it were hosted on a real web server with a custom domain.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/coderooz/my_server_project.git
   cd my_server_project
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Flask:**
   ```sh
   pip install flask
   ```

### Configuration

1. **Edit the configuration file:**

   Open `config.py` and set your custom domain and static files directory:
   ```python
   class Config:
       SERVER_NAME = "www.myserverproject.proj:5000"
       STATIC_FOLDER = "static_files"
   ```

2. **Update your hosts file:**

   Add the following line to your hosts file to map your custom domain to `127.0.0.1`:

   - **Windows:**
     ```sh
     127.0.0.1   www.myserverproject.proj
     ```
     (Located at `C:\Windows\System32\drivers\etc\hosts`)

   - **Mac/Linux:**
     ```sh
     sudo nano /etc/hosts
     ```
     Add:
     ```sh
     127.0.0.1   www.myserverproject.proj
     ```

### Running the Server

1. **Run the Flask application:**
   ```sh
   sudo python run.py  # Use sudo only if running on port 5000
   ```

2. **Access your website:**

   Open your browser and go to `http://www.myserverproject.proj`. You should see your website without specifying a port number.

### Changing the Custom Domain or Static Files Directory

To change the custom domain or the static files directory, simply update the `config.py` file:
```python
class Config:
    SERVER_NAME = "newdomain.proj:5000"
    STATIC_FOLDER = "new_static_folder"
```

Make sure to update your hosts file accordingly if you change the domain name.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request. All contributions are welcome!

## Contact

For any questions or suggestions, please contact [viewersweb02gmial.com].

---

**This description covers the key features, installation steps, configuration, and usage instructions to help users get started with your project.**
