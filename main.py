import eel
from PIL import Image
import base64 as b64
import os
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import shutil

eel.init('UI')

img=''

def genData(data): 
		newd = [] 
		
		for i in data: 
			newd.append(format(ord(i), '08b')) 
		return newd 
		
def modPix(pix, data): 
	
	datalist = genData(data) 
	lendata = len(datalist) 
	imdata = iter(pix) 

	for i in range(lendata): 
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]] 
									
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				
				if (pix[j]% 2 != 0): 
					pix[j] -= 1
					
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1

		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 

def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 
	
	for pixel in modPix(newimg.getdata(), data): 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1


		




@eel.expose
def Decrypt_python():
    global img
    #print(img)
    location="C:\\Users\\{0}\\Desktop\\".format(os.getlogin())
    try:
        image = Image.open(img, 'r') 
        
        data = '' 
        imgdata = iter(image.getdata())
        try:
            os.remove(img)
        except:
            pass

        
        while (True): 
                pixels = [value for value in imgdata.__next__()[:3] +
                                                                imgdata.__next__()[:3] +
                                                                imgdata.__next__()[:3]] 
                binstr = '' 
                
                for i in pixels[:8]: 
                        if (i % 2 == 0): 
                                binstr += '0'
                        else: 
                                binstr += '1'
                                
                data += chr(int(binstr, 2)) 
                if (pixels[-1] % 2 != 0): 
                        return data 

    except Exception as e:
        file=open(location+'error_log.txt','w')
        file.write(str(e))
        file.close()

        return 'Some error crept in. Check error_log in Desktop and please retry.'






@eel.expose
def Encrypt_python(data,name):
    global img
    #print(img)
    #print(img,data,name)
    #print(type(img),type(data),type(name))
    location="C:\\Users\\{0}\\Desktop\\".format(os.getlogin())
    try:
        image = Image.open(img, 'r') 
                        
        newimg = image.copy() 
        encode_enc(newimg, data) 
        if name=='': name='xxxx'
        new_img_name =  location+name+'.png'
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
        try:
            os.remove(img)
        except:
            pass
        return "Done!"
    except Exception as e:
        file=open(location+'error_log.txt','w')
        file.write(str(e))
        file.close()
        return "Error. Open error_log file in desktop."
    
    
@eel.expose
def Browse_python():
    global  img
    try:
        root=Tk()
        root.iconbitmap('UI/Images/color-palette.ico')
        root.withdraw()
        file=askopenfilename()

        new_file=file.split('/')[-1]
        shutil.copy(file,os.getcwd()+'\\UI\\'+new_file)
        #print(new_file)
        img='UI//'+new_file
        return new_file
    except:

        
        return ''



eel.start('index.html',size=(1000,500))


