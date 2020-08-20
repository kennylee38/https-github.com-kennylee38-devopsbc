from flask import Flask

# print a nice greeting.
def say_hello(username = "World of Kitty"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Kolabear Men</title> </head>\n<body>'''
instructions = '''
<img src="https://images-na.ssl-images-amazon.com/images/I/514ogtKoy0L._SX258_BO1,204,203,200_.jpg" alt="Girl in a jacket" width="500" height="600">

<iframe width="560" height="315" src="https://www.youtube.com/embed/_bC0_2h8Cc4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<p>Reference to 芒果TV音乐频道 MGTV Music Channel</p>

<img src="https://ca.slack-edge.com/T013RLQAASY-U013J4J1M4M-5805170924f6-512" alt="Girl in a jacket" width="500" height="600">

    <p style="background: yellow">: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
    
    
