import PyPDF2
import os
import traceback
import json



import PyPDF2

def read_file(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        try:
            reader = PyPDF2.PdfReader(file)
            full_text = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    # Replace problematic characters
                    text = text.encode('utf-8', errors='replace').decode('utf-8')
                    full_text.append(text)
            return "\n".join(full_text)
        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")

    elif filename.endswith(".txt"):
        try:
            text = ""
            while True:
                chunk = file.read(1024 * 1024)  # Read 1 MB at a time
                if not chunk:
                    break
                text += chunk.decode("utf-8", errors='ignore')  # Ignore decoding errors
            return text
        except Exception as e:
            raise Exception(f"Error reading TXT file: {e}")

    else:
        raise Exception("Unsupported file format. Only PDF and TXT are supported.")


    
def get_table_data(quiz_str):
        try:
            # convert the quiz from a str to dict
            quiz_dict=json.loads(quiz_str)
            quiz_table_data=[]
            
            # iterate over the quiz dictionary and extract the required information
            for key,value in quiz_dict.items():
                mcq=value["mcq"]
                options=" || ".join(
                    [
                        f"{option}-> {option_value}" for option, option_value in value["options"].items()
                    
                    ]
                )
                
                correct=value["correct"]
                quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})
            
            return quiz_table_data
            
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            return False
