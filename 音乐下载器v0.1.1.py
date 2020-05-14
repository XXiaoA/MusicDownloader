"""
音乐下载器v1.0
作者QQ：970582298
GitHub项目地址：https://github.com/XXiaoA/MusicDownloader
"""

import tkinter as tk
import tkinter.ttk
import requests
import re
import os
from random import randint
import time
import multiprocessing

class Download:
    def __init__(self):
        self.headers = {
            "user-agent": 'Mozilla/5.0 (Linux; Android 7.1.1; MP1603 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'}

    # 下载QQ音乐
    def qqMusic(self, url, path, FileName):
        req = requests.get(url, headers=self.headers)
        html = req.text
        DownloadUrl = re.findall(
            "http://aqqmusic.+m4a.+fromtag=\d+", html)
        try:
            DownloadUrl = DownloadUrl[0]
        except:
            print(url+"is")
        music = requests.get(DownloadUrl)
        with open(f"{path}{FileName}.m4a", "wb") as f:
            f.write(music.content)
    
    # 下载网易云音乐
    def neteaseCloudMusic(self, url, path, FileName):
        id = re.findall("id=\d+", url)[0]
        id = re.sub("id=", "", id)
        DownloadUrl = f"http://music.163.com/song/media/outer/url?id={id}.mp3"
        music = requests.get(DownloadUrl, headers=self.headers)
        # print(DownloadUrl)
        with open(f"{path}{FileName}.mp3", "wb") as f:
            f.write(music.content)


class Gui:  # Gui类，实现图形化页面
    def __init__(self):
        self.window = tk.Tk()
        # 窗口大小
        self.length = 1340
        self.width = 680
        # 保存路径
        self.path = ""
        # 10个网址字典套列表 列表第一个元素是网址 第二个是文件名 第三个是QQ音乐/网易云音乐
        self.UrlDict = {f"url{i}": [
            "", "", ""] for i in range(1, 11)}

    # 初始化窗口
    def setWindow(self):
        # 设置标题
        self.window.title("音乐下载器v1.0")
        # 设置窗口大小
        self.window.geometry(f"{self.length}x{self.width}")

    # 设置用户输入网址的文本框
    def inputUrl(self):
        text1 = tk.Label(self.window, text=" 网址")
        text1.grid(column=0, row=0)
        self.url1 = tk.Entry(self.window, width=40)
        self.url1.grid(column=0, row=1)
        self.url2 = tk.Entry(self.window, width=40)
        self.url2.grid(column=0, row=2)
        self.url3 = tk.Entry(self.window, width=40)
        self.url3.grid(column=0, row=3)
        self.url4 = tk.Entry(self.window, width=40)
        self.url4.grid(column=0, row=4)
        self.url5 = tk.Entry(self.window, width=40)
        self.url5.grid(column=0, row=5)
        self.url6 = tk.Entry(self.window, width=40)
        self.url6.grid(column=0, row=6)
        self.url7 = tk.Entry(self.window, width=40)
        self.url7.grid(column=0, row=7)
        self.url8 = tk.Entry(self.window, width=40)
        self.url8.grid(column=0, row=8)
        self.url9 = tk.Entry(self.window, width=40)
        self.url9.grid(column=0, row=9)
        self.url10 = tk.Entry(self.window, width=40)
        self.url10.grid(column=0, row=10)

    # 下载音乐的文件名
    def inputFileName(self):
        text1 = tk.Label(self.window, text=" 下载后的文件名")
        text1.grid(column=2, row=0)
        self.FileName1 = tk.Entry(self.window, width=15)
        self.FileName1.grid(column=2, row=1)
        self.FileName2 = tk.Entry(self.window, width=15)
        self.FileName2.grid(column=2, row=2)
        self.FileName3 = tk.Entry(self.window, width=15)
        self.FileName3.grid(column=2, row=3)
        self.FileName4 = tk.Entry(self.window, width=15)
        self.FileName4.grid(column=2, row=4)
        self.FileName5 = tk.Entry(self.window, width=15)
        self.FileName5.grid(column=2, row=5)
        self.FileName6 = tk.Entry(self.window, width=15)
        self.FileName6.grid(column=2, row=6)
        self.FileName7 = tk.Entry(self.window, width=15)
        self.FileName7.grid(column=2, row=7)
        self.FileName8 = tk.Entry(self.window, width=15)
        self.FileName8.grid(column=2, row=8)
        self.FileName9 = tk.Entry(self.window, width=15)
        self.FileName9.grid(column=2, row=9)
        self.FileName10 = tk.Entry(self.window, width=15)
        self.FileName10.grid(column=2, row=10)

    # 在输入网址旁边添加选择框，让用户选择是QQ音乐还是网易云音乐
    def choiceMusic(self):
        self.choice1 = tk.ttk.Combobox(self.window)
        self.choice1['values'] = ("网易云音乐", "QQ音乐")
        self.choice1.current(0)
        self.choice1.grid(column=3, row=1)
        self.choice2 = tk.ttk.Combobox(self.window)
        self.choice2['values'] = ("网易云音乐", "QQ音乐")
        self.choice2.current(0)
        self.choice2.grid(column=3, row=2)
        self.choice3 = tk.ttk.Combobox(self.window)
        self.choice3['values'] = ("网易云音乐", "QQ音乐")
        self.choice3.current(0)
        self.choice3.grid(column=3, row=3)
        self.choice4 = tk.ttk.Combobox(self.window)
        self.choice4['values'] = ("网易云音乐", "QQ音乐")
        self.choice4.current(0)
        self.choice4.grid(column=3, row=4)
        self.choice5 = tk.ttk.Combobox(self.window)
        self.choice5['values'] = ("网易云音乐", "QQ音乐")
        self.choice5.current(0)
        self.choice5.grid(column=3, row=5)
        self.choice6 = tk.ttk.Combobox(self.window)
        self.choice6['values'] = ("网易云音乐", "QQ音乐")
        self.choice6.current(0)
        self.choice6.grid(column=3, row=6)
        self.choice7 = tk.ttk.Combobox(self.window)
        self.choice7['values'] = ("网易云音乐", "QQ音乐")
        self.choice7.current(0)
        self.choice7.grid(column=3, row=7)
        self.choice8 = tk.ttk.Combobox(self.window)
        self.choice8['values'] = ("网易云音乐", "QQ音乐")
        self.choice8.current(0)
        self.choice8.grid(column=3, row=8)
        self.choice9 = tk.ttk.Combobox(self.window)
        self.choice9['values'] = ("网易云音乐", "QQ音乐")
        self.choice9.current(0)
        self.choice9.grid(column=3, row=9)
        self.choice10 = tk.ttk.Combobox(self.window)
        self.choice10['values'] = ("网易云音乐", "QQ音乐")
        self.choice10.current(0)
        self.choice10.grid(column=3, row=10)

    # 下载路径输入框
    def inputPath(self):
        text1 = tk.Label(self.window, text=" 下载路径(文件夹，默认为当前工作目录)")
        text1.grid(column=0, row=12)
        self.path1 = tk.Entry(self.window, width=40)
        self.path1.grid(column=0, row=13)

    # 开始下载按键
    def startDownload(self):
        # 点击事件
        def clicked():
            # 如果网址输入框不为空则添加进UrlDict
            if self.url1.get() != "":
                self.UrlDict["url1"][0] = self.url1.get()
            if self.url2.get() != "":
                self.UrlDict["url2"][0] = self.url2.get()
            if self.url3.get() != "":
                self.UrlDict["url3"][0] = self.url3.get()
            if self.url4.get() != "":
                self.UrlDict["url4"][0] = self.url4.get()
            if self.url5.get() != "":
                self.UrlDict["url5"][0] = self.url5.get()
            if self.url6.get() != "":
                self.UrlDict["url6"][0] = self.url6.get()
            if self.url7.get() != "":
                self.UrlDict["url7"][0] = self.url7.get()
            if self.url8.get() != "":
                self.UrlDict["url8"][0] = self.url8.get()
            if self.url9.get() != "":
                self.UrlDict["url9"][0] = self.url9.get()
            if self.url10.get() != "":
                self.UrlDict["url10"][0] = self.url10.get()

            # 如果文件名输入框不为空则添加进UrlDict
            # 如果为空添加 music加随机5位数
            if self.FileName1.get() != "":
                self.UrlDict["url1"][1] = self.FileName1.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName2.get() != "":
                self.UrlDict["url2"][1] = self.FileName2.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName3.get() != "":
                self.UrlDict["url3"][1] = self.FileName3.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName4.get() != "":
                self.UrlDict["url4"][1] = self.FileName4.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName5.get() != "":
                self.UrlDict["url5"][1] = self.FileName5.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName6.get() != "":
                self.UrlDict["url6"][1] = self.FileName6.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName7.get() != "":
                self.UrlDict["url7"][1] = self.FileName7.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName8.get() != "":
                self.UrlDict["url8"][1] = self.FileName8.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName9.get() != "":
                self.UrlDict["url9"][1] = self.FileName9.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            if self.FileName10.get() != "":
                self.UrlDict["url10"][1] = self.FileName10.get()
            else:
                self.UrlDict["url1"][1] = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"

            # 网址音乐 QQ音乐/网易云音乐
            if self.choice1.get() != "":
                self.UrlDict["url1"][2] = self.choice1.get()
            if self.choice2.get() != "":
                self.UrlDict["url2"][2] = self.choice2.get()
            if self.choice3.get() != "":
                self.UrlDict["url3"][2] = self.choice3.get()
            if self.choice4.get() != "":
                self.UrlDict["url4"][2] = self.choice4.get()
            if self.choice5.get() != "":
                self.UrlDict["url5"][2] = self.choice5.get()
            if self.choice6.get() != "":
                self.UrlDict["url6"][2] = self.choice6.get()
            if self.choice7.get() != "":
                self.UrlDict["url7"][2] = self.choice7.get()
            if self.choice8.get() != "":
                self.UrlDict["url8"][2] = self.choice8.get()
            if self.choice9.get() != "":
                self.UrlDict["url9"][2] = self.choice9.get()
            if self.choice10.get() != "":
                self.UrlDict["url10"][2] = self.choice10.get()

            # 如果路径输入框不为空则添加
            # 为空则为当前工作目录
            if self.path1.get() != "":
                self.path = self.path1.get()
            else:
                self.path = os.getcwd()
            if self.path[-1] != "/" and self.path[-1] != "\\":
                self.path += "/"
            # print(self.UrlDict)
            # print(self.path)
            # 下载音乐

            D = Download()
            # t = time.time()
            for music in self.UrlDict:
                if self.UrlDict[music][2] == "QQ音乐":
                    if self.UrlDict[music][0] != "":
                        url = self.UrlDict[music][0]
                        FileName = self.UrlDict[music][1]
                        path = self.path
                        p = multiprocessing.Process(target=D.qqMusic, args=(url, path, FileName, ))
                        p.start()
                    else:
                        continue
                elif self.UrlDict[music][2] == "网易云音乐":
                    if self.UrlDict[music][0] != "":
                        url = self.UrlDict[music][0]
                        FileName = self.UrlDict[music][1]
                        path = self.path
                        p = multiprocessing.Process(target=D.neteaseCloudMusic, args=(url, path, FileName, ))
                        p.start()
                    else:
                        continue
            # print(time.time()-t)

        start = tk.Button(self.window, text="点我开始下载", command=clicked)
        start.grid(column=2, row=12)

    # 下载成功提示框
    def promptBox(self):
        box = tk.Text(self.window, width=25, height=2)
        # box.insert("insert", "文本")
        box.grid(column=3, row=12)
        self.window.mainloop()


gui = Gui()
gui.setWindow()
gui.inputUrl()
gui.inputFileName()
gui.choiceMusic()
gui.inputPath()
gui.startDownload()
gui.promptBox()
