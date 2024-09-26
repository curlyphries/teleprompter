# 📜 Teleprompter Script

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-red?logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Welcome to the **Teleprompter Application**!

An easy-to-use teleprompter built with Python and Tkinter that allows you to:

- 📝 **Enter text** as you want it read per line.
- 🎚️ **Adjust text size** on the teleprompter.
- ⏱️ **Adjust the scroll speed** in seconds.
- ▶️ **Start** and ⏹️ **Stop** the scrolling text.
- ⏯️ **Pause and resume** scrolling with the space bar or any key.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Step-by-Step Guide](#step-by-step-guide)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Features

- **Customizable Text Input:** Enter your script line by line.
- **Adjustable Font Size:** Modify the text size to your preference.
- **Variable Scroll Speed:** Set how long each line stays on screen (in seconds).
- **Control Buttons:** Start and stop the scrolling at any time.
- **Keyboard Control:** Use the space bar to pause and resume scrolling.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your system.
- Basic knowledge of running Python scripts.

---

## Installation

Follow these steps to get a copy of the project running on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/curlyphries/teleprompter.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd teleprompter
   ```

3. **Install Dependencies**

   The application uses the built-in `tkinter` library, which comes pre-installed with most Python distributions. If not, you may need to install it:

   - **For Debian/Ubuntu:**

     ```bash
     sudo apt-get install python3-tk
     ```

   - **For macOS:**

     Tkinter is included with Python on macOS. If you encounter issues, consider reinstalling Python from [python.org](https://www.python.org/downloads/mac-osx/).

   - **For Windows:**

     Tkinter is included with the standard Python installer from [python.org](https://www.python.org/downloads/windows/).

---

## Usage

Follow these steps to run the Teleprompter Application:

1. **Run the Application**

   ```bash
   python teleprompter.py
   ```

2. **Enter Your Text**

   - In the left pane, enter your script line by line as you want it to appear.

3. **Load the Text**

   - Click on the **Load Text** button to load your script into the teleprompter.

4. **Adjust Settings**

   - **Speed (seconds):** Use the slider to set how many seconds each line will display.
   - **Font Size:** Use the slider to adjust the size of the text in the teleprompter.

5. **Control the Teleprompter**

   - Click **Start** to begin scrolling through your script.
   - Click **Stop** to pause the scrolling.
   - Press the **Space Bar** to toggle between pause and resume.

---

## Step-by-Step Guide

Here's a detailed guide to help you run the application:

### 1. Ensure Python is Installed

Check if Python is installed:

```bash
python --version
```

If Python is not installed, download it from the [official website](https://www.python.org/downloads/).

### 2. Install Tkinter (if necessary)

- **Linux (Debian/Ubuntu):**

  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk
  ```

- **macOS and Windows:**

  Tkinter should be included with your Python installation. If not, reinstall Python using the installer from [python.org](https://www.python.org/downloads/).

### 3. Download the `teleprompter.py` File

You can download the file directly or clone the repository:

```bash
git clone https://github.com/curlyphries/teleprompter.git
cd teleprompter
```
python teleprompter.py
