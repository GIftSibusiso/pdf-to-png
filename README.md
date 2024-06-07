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

1. Download the latest Poppler binary from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/).
2. Extract the contents and add the `bin` folder to your system PATH.

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
    python pdf_to_png.py input.pdf output_folder
    ```

### Example

```sh
python pdf_to_png.py sample.pdf ./output
