# Starfield Simulation

This repo contains a python app for a starfield simulation, similar to the Windows 95 screensaver.

It was created using ChatGPT o3-mini-high on 06/02/2025 using the following prompt only (one shot):

    `Create python code for a starfield simulation screensaver, similar to the Windows 95 one.`

The python code output was used to create 'starfield.py' and it worked with no noticeable bugs.

## Installation Instructions

### Prerequisites
- [Python 3.x and Pip](https://www.python.org/) Python package manager installed
- [Git](https://git-scm.com/) distributed version control system installed

### Installation Steps

1. Clone this repository:

    `git clone https://github.com/colinmccrae/Starfield/`

2. Navigate to the project directory:

    `cd Starfield`

3. Run the installation script: `install.bat`. If you do this you can move straight to Step 7. If you don't want to run this batch file, you can alternatively manually swtich to a virtual environment and install the dependencies as per Steps 4-6.

4. Create a virtual environment:

    `python -m venv starfield-env`

5. Activate the virtual environment:

    `.\starfield-env\Scripts\activate`

6. Install dependencies from requirements.txt

    `pip install -r requirements.txt -U`

7. Run the Python script

    `python starfield.py`