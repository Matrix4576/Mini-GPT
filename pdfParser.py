import PyPDF2 as pdf

reader = pdf.PdfReader("train-data//b1.pdf")
reader2 = pdf.PdfReader("train-data//b2.pdf")
for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    if len(text) == 0:
        continue
    else:
        file = open(f"sample-texts//b1//pg{i}.txt", "w")
        try:
            file.write(text)
            print(f"Page {i} of Book 1 extracted")
            file.close()
        except UnicodeEncodeError as UE:
            print('Error encounterd page is skipped')
            print(UE)
            continue
for i in range(len(reader2.pages)):
    page = reader2.pages[i]
    text = page.extract_text()
    if len(text) == 0:
        continue
    else:
        file = open(f"sample-texts//b2//pg{i}.txt", "w")
        try:
            file.write(text)
            print(f"Page {i} of Book 2 extracted")
            file.close()
        except UnicodeEncodeError as UE:
            print('Error encounterd page is skipped')
            print(UE)
            continue