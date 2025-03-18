# Dynamic CV Generator

The Dynamic CV Generator is a Python-based application that allows users to create, save, and load dynamic CVs (Curriculum Vitae) using a graphical user interface (GUI) built with Tkinter. The application also supports exporting the CV to a PDF format using the ReportLab library.

## Features

1. **User-Friendly Interface**: The application provides a simple and intuitive interface for users to input their personal information, skills, education, work experience, and projects.
2. **Backup and Load Functionality**: Users can save their CV data as a JSON file for future editing and load previously saved backups.
3. **PDF Generation**: The application can generate a well-formatted PDF version of the CV, including sections for personal information, profile summary, skills, education, certificates, work experience, and projects.

## How It Works

1. **Input Fields**: Users fill in various input fields for personal information, skills, education, certificates, work experience, and projects.
2. **Save Backup**: Users can save their input data as a JSON file by clicking the "Save Backup" button.
3. **Load Backup**: Users can load previously saved data by clicking the "Load Backup" button, which populates the input fields with the saved data.
4. **Generate CV**: Users can generate a PDF version of their CV by clicking the "Generate CV" button. The application collects all input data, formats it, and saves it as a PDF file.

## Technologies Used

- **Python**: The core programming language used for the application.
- **Tkinter**: Used for building the graphical user interface.
- **ReportLab**: Used for generating PDF documents.
- **JSON**: Used for saving and loading backup data.

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd CV_gen
    ```

2. **Install the required libraries**:
    ```sh
    pip install reportlab
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Fill in the input fields**: Enter your personal information, skills, education, certificates, work experience, and projects.

3. **Save Backup**: Click the "Save Backup" button to save your input data as a JSON file.

4. **Load Backup**: Click the "Load Backup" button to load previously saved data.

5. **Generate CV**: Click the "Generate CV" button to generate a PDF version of your CV.

## Code Structure

- **Imports**: Necessary libraries and modules are imported at the beginning.
- **Functions**: Functions for saving backups, loading backups, preparing the PDF, and generating the CV are defined.
- **GUI Setup**: The Tkinter GUI is set up with labels, entry fields, text areas, buttons, and a scrollable frame.
- **Main Loop**: The Tkinter main loop runs the application.

## Test & Results
![image](https://github.com/user-attachments/assets/e7ece1c8-5149-4e63-8b71-f7aae07e420d)

![image](https://github.com/user-attachments/assets/db6d2131-a0dd-4f4d-aa6e-c23997c21062)



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI components.
- [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) for PDF generation.
- [Python](https://www.python.org/) for being the core programming language.
