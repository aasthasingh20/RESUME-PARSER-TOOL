# RESUME-PARSER-TOOL
Built a modular tool using HTML, CSS, Python, NLP, and database integration to extract and categorize candidate details based on skill  requirements. 
Helps users improve their resumes. Designed in alignment with IEEE project standards.
# Resume Parser Tool

A modular tool that extracts and categorizes candidate details from resumes using NLP and database integration.

## Features

- Extracts personal information (name, email, phone)
- Identifies skills from resume text
- Parses work experience and education
- Stores parsed data in a searchable database
- Filters candidates by skills
- Supports PDF, DOCX, DOC, and TXT formats

## Technologies

- **Backend**: Python with Flask
- **Frontend**: React.js
- **NLP**: spaCy
- **Database**: SQLite
- **File Processing**: PyPDF2, python-docx

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
2. Create and activate a virtual environment:
3. Install dependencies:

4. Download spaCy English model:
 5. Run the backend server:

### Frontend Setup

1. Navigate to the frontend directory
2. Install dependencies
3. Start the development server

Project Structure
backend:    Flask application with NLP processing

app.py:      Main Flask application

nlp_processor.py:   Resume text processing logic

database.py:     Database interaction

uploads:       Temporary storage for uploaded files

frontend:      React application

src:        React components and styles

database:     SQL initialization scripts











