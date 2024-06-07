# PDF to PNG Converter

This script converts PDF files to PNG images using Python. To run this script, you need to have the `pdf2image` library installed and Poppler installed on your system.

## Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **pdf2image**: Install the `pdf2image` library. You can install it using pip:
    ```sh
    pip install pdf2image
    ```
3. **Poppler**: You need to have Poppler installed. Follow the instructions below to install it based on your operating system.

### Installing Poppler

#### Windows

1. Install WSL ([Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)).
2. Use Linux command on WSL to install poppler

*NB*: On windows, you'll have to open WSL to run to run the file not cmd

#### macOS

1. Use Homebrew to install Poppler:
    ```sh
    brew install poppler
    ```

#### Linux

1. Use your package manager to install Poppler. For example, on Ubuntu:
    ```sh
    sudo apt-get install poppler-utils
    ```

## Usage

1. Clone this repository or download the script.
2. Make sure you have all the prerequisites installed.
3. Run the script by using the following command:
    ```sh
    python3 main.py
    ```

### Example

```sh
python3 main.py
