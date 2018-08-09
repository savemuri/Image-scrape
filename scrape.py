#! python3
import os, requests, bs4

def tiny_pic_downloader(keyword, directory):
    os.chdir(directory)
    page = 1
    num = 1
    os.mkdir('%s' %keyword)
    try :
        while True:
            linklist = []
            res = requests.get('http://tinypic.com/search.php?page=%s&tag=%s' % (page, keyword))
            imgur_bs_obj = bs4.BeautifulSoup(res.text, 'html.parser')
            images_element = imgur_bs_obj.select('img')
            for i in range(0,len(images_element)-1):
                a = str(images_element[i].get('src'))
                a = a.replace('d_th.jpg','d.jpg')
                a = a.replace('oi42','http://s5')
                linklist.append(a)
            del linklist[0]
            del linklist[0]
            del linklist[len(linklist)-1]
            for i in range(0,len(linklist)):
                res = requests.get(linklist[i])
                res.raise_for_status()
                imageFile = open(('%s\\'+os.path.basename(linklist[i])) %keyword , 'wb')
                print ('Downloading File : %s' %num)
                for chunk in res.iter_content():
                    imageFile.write(chunk)
                imageFile.close()
                num += 1
            page+=1
    except:
        print ('Download Completed.')


def imgur_downloader(keyword, directory):
    os.chdir(directory)
    res = requests.get('http://imgur.com/search/score/all?q=%s' % keyword)
    imgur_bs_obj = bs4.BeautifulSoup(res.text, 'html.parser')
    images_element = imgur_bs_obj.select('#imagelist img')
    num = 1
    linklist = []
    os.mkdir('%s' % keyword)
    try:
        for i in range(0, len(images_element) - 1):
            a = str(images_element[i].get('src'))
            a = a[2:]
            a = a.replace('b.jpg', 'g.jpg')
            a = a.replace('i.i', 'http://i.i')
            linklist.append(a)
        for i in range(0, len(linklist)):
            res = requests.get(linklist[i])
            res.raise_for_status()
            imageFile = open(('%s\\' + os.path.basename(linklist[i])) % keyword, 'wb')
            print('Downloading File : %s' % num)
            for chunk in res.iter_content():
                imageFile.write(chunk)
            imageFile.close()
            num += 1
    except:
        print('Download Completed.')
