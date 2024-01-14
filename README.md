# Kaide's Portfolio

Portfolio website build with [Reflex](https://reflex.dev) and using Github API.

# Getting Started
### Prerequisites:
Download and install Python (Version 3.10+ is recommended).

### Setting up the project:
1. Clone the GitHub repository:

```bash
git clone https://github.com/kaidewu/portfolio-reflex
```

1. Navigate to the project directory:

```bash
cd portfolio-reflex
```

2. (Recommended) Create a Python virtual environment: You can follow the Python official documentation for virtual environments.

```bash
python3 -m venv venv
```

3. Activate the virtual environment:
  
  - On Windows:

    ```
    .\venv\Scripts\activate
    ```

  - On MacOS and Linux:
  
    ```bash
    source venv/bin/activate
    ```

4. Install the required Python packages from requirements.txt:

```bash
pip install -r requierements.txt
```

5. Start Reflex Application:


```bash
reflex init
```

6.  Run Reflex Application:

```bash
reflex run
```

## Build Reflex Container Image

To build your container image run the following command:

```bash
docker build -t portfolio-reflex:latest .
```

## Start Container Service

Finally, you can start your Reflex container service as follows:

```bash
docker run -p 3000:3000 -p 8000:8000 --name portfolio portfolio-reflex:latest
```
