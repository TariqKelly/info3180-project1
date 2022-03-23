"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, send_from_directory, url_for, flash, session, abort, redirect
from werkzeug.utils import secure_filename
from app.forms import NewPropertyForm
from app.models import Property
from . import db


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties')
def properties():
    properties = db.session.query(Property).all()
    return render_template('properties.html', properties=properties)


@app.route('/properties/create', methods=['GET','POST'])
def properties_create():
    property_form = NewPropertyForm()
    file_folder = app.config['UPLOAD_FOLDER']
    if request.method == 'POST':
        if property_form.validate_on_submit():
            
            property_photo = request.files['photo']
            file_name = secure_filename(property_photo.filename)
            property_photo.save(os.path.join(file_folder, file_name))

            property = Property(
            request.form['title'],
            request.form['description'],
            request.form['number_of_bedrooms'],
            request.form['number_of_bathrooms'],
            request.form['location'],
            request.form['price'],
            request.form['property_type'],
            file_name
            )

            db.session.add(property)
            db.session.commit()
            return redirect(url_for('properties'))

    return render_template('create-property.html', form=property_form)

@app.route("/properties/create/<filename>")
def get_uploaded_file(filename):
    root_dir = os.getcwd()

    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties/<propertyid>', methods=['GET','POST'])
def propertyid(propertyid):
    property = db.session.query(Property).filter_by(id = propertyid).first()
    print(str(property))
    return render_template('property.html', property=property)

def get_uploaded_images():
    file_names = []
    rootdir = os.getcwd()

    for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
            for file in files:
                filenames_lst = os.path.join(subdir,file)
                file_names.append(os.path.basename(filenames_lst))
    return file_names



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
