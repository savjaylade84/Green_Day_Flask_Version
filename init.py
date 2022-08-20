import os
import json
from flask import Flask,url_for,render_template,redirect


'''
    iniatiate flask object 
    arguments that past on it are the 
    templates(folder for the html) and 
    the static(folder for others like css, javascript,and etc)
    folder paths
'''
app = Flask(__name__,template_folder='templates',static_folder='static')

''' 
    redirect to a internal pages 
'''
@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/music/')
def music():
    return render_template('music.html',music_record=get_music())

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/about/')
def about():
    return render_template('about.html',links=get_link())


'''
    get the data from the json files
'''
def get_link()->dict:
    filename = os.path.join(app.static_folder,'external_link','external_link.json')
    with open(filename,'r') as file:
        _json = json.load(file)
        return _json
    
def get_music()->dict:
    filename = os.path.join(app.static_folder,'music','music_record.json')
    with open(filename,'r') as file:
        _json = json.load(file)
        return _json

'''
    this part is to redirect to the external sites
'''
@app.route('/github/')
def github():
    return redirect('https://www.github.com/savjaylade84/',code=302)

@app.route('/facebook_page/')
def facebook_page():
    return redirect('https://www.facebook.com/Jisun-102294825339373/',code=302)

@app.route('/portfolio/')
def portfolio():
    return redirect('https://www.savjaylade84.github.io/Jisun.github.io/',code=302)

@app.route('/linkedin/')
def linkedin():
    return redirect('https://www.linkedin.com/mwlite/in/john-jayson-de-leon-73532818b/',code=302)

if __name__ == '__main__':
    app.run(debug=True)