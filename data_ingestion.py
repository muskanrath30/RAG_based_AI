import PyPDF2
import requests
from bs4 import BeautifulSoup

def extract_key_sections(text):
    """Key sections such as education, experience, and projects."""
    education = []
    experience = []
    projects = []
    lines = text.splitlines()

    for line in lines:
        if "bachelor" in line.lower() or "degree" in line.lower() or "programme" in line.lower() or "Post Graduation" in line.lower():
            education.append(line)
        elif "experience" in line.lower() or "work" in line.lower() or "organisation" in line.lower():
            experience.append(line)
        elif "project" in line.lower() or "internship" in line.lower():
            projects.append(line)

    return "\n".join(education), "\n".join(experience), "\n".join(projects)

def ingest_pdf_data(file_paths=['MuskanRathResume (3).pdf', 'Profile.pdf']):
    """Function to ingest data from PDF files."""
    data = []
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        data.append(text)
                    else:
                        print(f"Warning: Page with no extractable text found in {file_path}.")
        except FileNotFoundError:
            print(f"PDF file {file_path} not found. Skipping PDF data ingestion.")
        except Exception as e:
            print(f"Error while reading {file_path}: {e}")

    if not data:
        print("No data extracted from the PDFs.")
    combined_text = " ".join(data)
    education, experience, projects = extract_key_sections(combined_text)
    return combined_text, education, experience, projects  # Ensure all values are returned

def ingest_text_file_data(file_path='personal_info.txt'):
    """Function to ingest data from a text file."""
    data = []
    try:
        with open(file_path, 'r') as file:
            data.append(file.read())
    except FileNotFoundError:
        print("Text file not found. Skipping text file data ingestion.")
    except Exception as e:
        print(f"Error while reading text file: {e}")

    if not data:
        print("No data extracted from the text file.")
    return " ".join(data)

def ingest_data():
    """Main function to ingest data from multiple sources."""
    pdf_data, education, experience, projects = ingest_pdf_data()  # Ensure this returns the expected components
    text_data = ingest_text_file_data()

    # Combine all data sources into one
    all_data = " ".join([pdf_data, text_data])

    if not all_data.strip():
        print("Warning: Combined data is empty, check data sources.")
    else:
        print("Data successfully ingested from all sources.")

    return all_data, education, experience, projects  # Ensure it returns all expected values

if __name__ == "__main__":
    try:
        all_data, education, experience, projects = ingest_data()
        pass
        # print("Education Extracted:", education)
        # print("Experience Extracted:", experience)
        # print("Projects Extracted:", projects)
    except ValueError as e:
        print(f"Error unpacking data: {e}")