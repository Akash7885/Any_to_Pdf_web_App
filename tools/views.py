from importlib.resources import path
from django.shortcuts import redirect, render
from . models import UserFile, UserFeedback
from fpdf import FPDF
import img2pdf
import random
import os
import string
import aspose.words as aw
from django.contrib import messages
# Create your views here.


def TextToPdf(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/jpg2pdf/', str(res))
        os.makedirs(path_to_upload)

        files = request.FILES.get('files')
        UserFile(files=files).save()
        Pdf = UserFile.objects.last()
        
        newPath=os.path.join('C:\Akash\AnyToPdf\static\Files',str(Pdf.files))
   
        pd = FPDF()
        pd.add_page()
        pd.set_font("Arial", size=15)
        f = open(newPath, "r") 
        for x in f:
            pd.cell(256, 10, txt=x, ln=1, align="l")

        pd.output(path_to_upload+"/sample.pdf")
        os.rename(path_to_upload + "/sample.pdf",path_to_upload + "/sample.pdf")
        return render(request, 'Downloadpage.html', {'url': str(res)})
    return render(request, 'TextToPdf.html')


def DownloadPage(request):
    return render(request, 'Downloadpage.html')


def ImgToPdf(request):
    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join(
            './static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)

        files = request.FILES
        files_list = []

        for file in files.getlist('files'):
            files_list.append(file)

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)

        with open(path_to_upload + "/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        os.rename(path_to_upload + "/sample.pdf",path_to_upload + "/sample.pdf")

        return render(request, 'Downloadpage.html', {'url': str(res)})
    return render(request, 'ImgToPdf.html')


def DocxToPdf(request):
    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)

        files = request.FILES.get('files')
        UserFile(files=files).save()
        Pdf = UserFile.objects.last()
        

        newPath=os.path.join('C:\Akash\AnyToPdf\static\Files',str(Pdf.files))

        doc = aw.Document(newPath)  
        doc.save(path_to_upload+"/sample.pdf")

        return render(request, 'Downloadpage.html', {'url': str(res)})
    return render(request, 'DocxToPdf.html')


def PngtoPdf(request):
    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join(
            './static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)

        files = request.FILES
        files_list = []

        for file in files.getlist('files'):
            files_list.append(file)

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)

        with open(path_to_upload + "/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        os.rename(path_to_upload + "/sample.pdf",path_to_upload + "/sample.pdf")

        return render(request, 'Downloadpage.html', {'url': str(res)})
    return render(request, 'PngtoPdf.html')


def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']

        UserFeedback(name=name, email=email, msg=msg).save()
        messages.info(
            request, "We got your feedback ,Thankyou for your feedback")
        return redirect("/")

    return render(request, 'feedback.html')
