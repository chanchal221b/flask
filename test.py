from flask import Flask,render_template,request,redirect
import os

var1=0 #hamming_yes
var2=0 #hamming_no
var3=0 #Google_API
var4=0 #Pocketsphinx
var5=0 #data_creation
var6=0 #sneha
var7=0 #folder_1
var8=0 #folder_2

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test.html')

@app.route('/reg',methods=['GET','POST'])
def run():
    if request.method=='POST':
        os.system("python3 /home/chanchal/gui/hello.py")
        file = open("/home/chanchal/gui/email.txt","w+")
        email = request.form['email']
        #print(email)
        file.write(str(email)+"\n")
        file.close()
        url = request.form['url']
        file = open("/home/chanchal/gui/email.txt","a")
        file.write(str(url))
        file.close()
        words = request.form['words']
        li = list(words.split(" ")) 
        file = open("/home/chanchal/gui/email.txt","a")
        for i in range (len(li)):
            file.write(str(url)+"       ")
            file.write(li[i]+ "\n")
        file.close()
        audio = request.form['files']
        file.write(audio)
        if request.form.get('hamming_yes'):
            var1 = 1
        if request.form.get('hamming_no'):
            #print(request.form.get('hamming_no'))
            var2 = 1
        if request.form.get('api'):
            var3 = 1
        if request.form.get('Pocketsphinx'):
            var4 = 1
        if request.form.get('data'):
            var5 = 1
        if request.form.get('sneha'):
            var6 = 1
        if request.form.get('google'):
            var6 = 1
        if request.form.get('folder1'):
            var7 = 1
        if request.form.get('folder2'):
            var8 = 1
                          
        return "hello"
    return redirect('test.html')

if __name__ == '__main__':
    app.run(debug=True)