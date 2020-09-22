import sys, re
import lxml.html as lh
from bs4 import BeautifulSoup as bs
from flask_frozen import Freezer
from flask import Flask, render_template, request, jsonify, abort, redirect, send_from_directory
from events import events
from members import members
from mentors import mentors

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.url_map.strict_slashes=False
freezer = Freezer(app)

def page(temp): return re.sub("(<!--.*?-->)", "", re.sub(">\s*<", "><", temp), flags=re.DOTALL)

@app.route("/")
def index():
    temp= render_template(
        'home.html',
        events= events,
        members= members,
        mentors= mentors,
        pageTitle= 'DSC-IIIT Delhi | Students | Google Developers',
        pageDescr= 'Developer Student Clubs are university based community groups for students interested in Google developer technologies. By joining a DSC, students grow their knowledge in a peer-to-peer learning environment and build solutions for local businesses and their community.',
        slug= ''
    )
    return page(temp)
 
@app.route("/events/<string:event_name>/")
def each_event(event_name):
    temp= render_template(
        'event.html',
        eventName= event_name,
        eventDetail= events.get(event_name),
        pageTitle= event_name + ' | DSC-IIIT Delhi | Students | Google Developers',
        pageDescr= event_name + ' | ' + events.get(event_name)['desc']  + ' | Developer Student Clubs are university based community groups for students interested in Google developer technologies. By joining a DSC, students grow their knowledge in a peer-to-peer learning environment and build solutions for local businesses and their community.',
        slug= event_name
    )
    return page(temp)

@freezer.register_generator
def each_event():
    for product in events:
        yield {'event_name': product}

@app.route("/robots.txt/")
def toboots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '404.html', 
        pageTitle= 'Page Not Found | DSC-IIIT Delhi | Students | Google Developers',
        pageDescr= 'Page Not Found | DSC-IIIT Delhi | Students | Google Developers',
        slug= '404'
    ), 404

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug= True, port= 4000)