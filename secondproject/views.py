from curses.ascii import HT
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):


  return render(request,'textutilities.html')
 





###############################################
def myaction(request):
  # return HttpResponse()
   
  tasks=str("")
  inputtext=request.GET.get('giventext','default')
  givecount=request.GET.get('givencc','')
  givemap=request.GET.get('giventt','default')
  
  removepunctuation=request.GET.get('rp','off')
  capitalizemaker=request.GET.get('cm','off')
  spaceremover=request.GET.get('sr','off')


  if removepunctuation=='on':
    tasks=tasks+" Remove_Punctuation "
    punctuation='''!@$%&^*(,?\#);':/<>!\@*-+|[]{}'''
    output1=""
    for char in inputtext:
      if char not in punctuation:
        output1=output1+char
  else:
    output1=inputtext

  if capitalizemaker=='on':
    tasks=tasks+" Capitalizing "
     
    output2=output1.upper()
  else:
    output2=output1

  if spaceremover=='on':
      tasks=tasks+" Space Remover"
      analyzed=""
      analyzed=output2.strip()
  else:
    analyzed=output2

  out1=""
  strc=""
  if(len(givecount)>0):

   
    if capitalizemaker=='on':
      strc=givecount.upper()
      out1=analyzed.count(givecount.upper())
    else:
      strc=givecount
      out1=analyzed.count(givecount)

  a=""
  b="" 
  if(len(givemap)>1):
    a,b=givemap.split(',')
    if(capitalizemaker=='on'):
        
        a=a.upper()
        b=b.upper() 
        
    
  mytable = analyzed.maketrans(a, b)
  out2=analyzed.translate(mytable)
 
  userdata={'Task':tasks,'orignal_text':inputtext,'analyzed_text':analyzed,'output1':(out1,strc),'output2':out2,'str1':a,'str2':b}
  return render(request,'textanalyzer.html',userdata)


  # usertext=f'''{inputtext}'''
  # if removepunctuation=='on':
  #   punctuation='''!@$%&^*(,?\#);':/<>!\@*-+|[]{}'''
  #   analyzed=""
  #   for char in inputtext:
  #     if char not in punctuation:
  #       analyzed=analyzed+char
  #   userdata={'Task':'Remove punctuations','orignal_text':usertext,'analyzed_text':analyzed}
  #   return render(request,'textanalyzer.html',userdata)
  # elif capitalizemaker=='on':
     
  #   analyzed=""
  #   for char in inputtext:
      
  #       analyzed=analyzed+char.upper()
  #   userdata={'Task':'Capitalization','orignal_text':usertext,'analyzed_text':analyzed}
  #   return render(request,'textanalyzer.html',userdata)
  
  # elif spaceremover=='on':
  #   analyzed=''
  #   # analyzed=inputtext.strip()
  #   # for char in inputtext:
      
  #   #     analyzed=analyzed+char.upper()
  #   # analyzed=inputtext
  #   for index,char in enumerate(inputtext):
  #     if not(inputtext[index]==' ' and inputtext[index+1]==' '):
  #       analyzed=analyzed+char
        

   

  #   userdata={'Task':'Space remover','orignal_text':usertext,'analyzed_text':analyzed}
  #   return render(request,'textanalyzer.html',userdata)
  
 
# else:
#     return HttpResponse('ERROR the text cannot be analyzed')

  

# def removepunctuation(request):
#   return HttpResponse('capitalize')
# def capitalize(request):
#   return HttpResponse('capitalize')
# def spaceremover(request):
#   return HttpResponse('spacremover')









###########################################
####################################
 
