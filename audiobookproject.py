import PyPDF2
from gtts import gTTS

from PyPDF2 import PdfReader

reader = PdfReader("//Users//krishnaharshabachinappa//Library//Mobile Documents//com~apple~CloudDocs//Python_tutorial//Sample.pdf")
page = reader.pages[0]
pdf_text = page.extract_text()
print(page.extract_text())

tts = gTTS(text = pdf_text, lang='en')
tts.save("output.mp3")
print("MP3 file creation successful!")