from setuptools import setup,find_packages

setup(name="msqgenerator",
      version="0.0.1",
      requires=["openai","langchain","streamlit","PyPDF2","python-dotenv"],
      author="ilias baher",
      author_email="iliasbessiness123456@gmail.com",
      packages=find_packages())  
