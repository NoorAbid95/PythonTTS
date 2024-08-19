from gtts import gTTS
import PyPDF2

# Initialising the pdf_reader variable which will open and read the pdf in our directory.
pdf_reader = PyPDF2.PdfReader(open('sample_pdf.pdf', 'rb'))

""" Creating a complete_text variable as an empty string in order to combat the issue of the reader only reading 
# the last page of the PDF """
complete_text = ""
# Creating the for loop to loop through each page of the PDF file.
for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n", ' ')
    # Appending the originally empty complete_text variable to now contain the clean_text data.
    complete_text += clean_text

# Instantiating the Google text to speech (tts) object and passing in the cleaned text as an argument.
tts = gTTS(complete_text)

# Saving the tts file as a mp3 file.
tts.save("speech.mp3")