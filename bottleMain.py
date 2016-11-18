from bottle import route, template, static_file, run
import rand

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@route('/figures/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static\figures')

@route('/images/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static\images')

@route('/attrib')
def attrib():
    attribVals = str(rand.attribute())
    attribVals2 = str(rand.attribute())
    attribVals3 = str(rand.attribute())
    attribVals4 = str(rand.attribute())
    attribVals5 = str(rand.attribute())
    attribVals6 = str(rand.attribute())
    return(template('default',row=attribVals,row2=attribVals2,row3=attribVals3,row4=attribVals4,row5=attribVals5,row6=attribVals6))

run(host='localhost', port=8080, debug=True)