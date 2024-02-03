# AudioBook Creator

## Overview

The AudioBook Creator is a simple Python program developed using the tkinter library for creating an audiobook from a PDF file. This application leverages the PyPDF2 library for handling PDFs, pyttsx3 for text-to-speech conversion, and tkinter for creating the graphical user interface.

## Features

- **PDF Selection:** Users can browse and select a PDF file of their choice.
  
- **Text-to-Speech Conversion:** The application extracts text from each page of the PDF and converts it into an audiobook.

- **Voice Options:** Users can choose between a male or female voice for the audiobook.

- **Save Audiobook:** The created audiobook is saved as an 'audio.mp3' file.

## How to Use

1. **Install Dependencies:**
   Ensure that you have the required dependencies installed. You can do this by running:

   ```bash
   pip install PyPDF2
   ```
   
    ```bash
   pip install pyttsx3
   ```
    
     ```bash
   pip install tkinter
   ```

2. **Run the Application:**
   Execute the Python script in your terminal or preferred Python environment:

   ```bash
   python audiobook_creator.py
   ```

3. **Browse PDF File:**
   Click the "Browse a File" button to select the PDF file you want to convert.

4. **Choose Voice:**
   Check either "Male Voice" or "Female Voice" based on your preference.

5. **Create and Save Audiobook:**
   Click the "Create and Save the Audio File" button to generate the audiobook. Once complete a status and confirmation messages will be displayed.

6. **Saved Audiobook:**
   The audiobook is saved as 'audio.mp3' in the same directory as the script.

## Notes

- Ensure the PDF file is formatted correctly to achieve optimal results.
- Make sure the pdf only contains text.
- Adjust volume settings on your system for an enhanced audio experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
