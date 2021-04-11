from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models
from PIL import Image
import shutil
import os
from .validate import Form


def validate(*args, **kwargs):
    Form.to_python(kwargs)

@view_config(route_name='home', renderer='masha:templates/layout.mako')
def my_view(request):
    # url_media = request.static_url('masha:image/BZPY9746.JPG')
    # print(url_media)
    # print('Url here new')
    try:
        query = request.dbsession.query(models.Image).all()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': query, 'project': 'masha'}


@view_config(route_name='home2', renderer='masha:templates/mytemplate.mako')
def home2(request):
    if request.method == 'POST':
        print(request.POST['file'])
        test = request.POST['test']
        name = request.POST['name']
        chislo = request.POST['chislo']
        filename = request.POST['file'].filename
        input_file = request.POST['file'].file
        this_directory = request.registry.settings.get('media_location')
        data = {'test': test,
                'name': name,
                'chislo': chislo}
        try:
            Form.to_python({'test':test})
        except Exception as e:
            return Response('Invalid form, {}'.format(e))

        # We first write to a temporary file to prevent incomplete files from
        # being used.
        temp_file_path = this_directory + filename
        url = 'image/' + filename
        print(temp_file_path)
        # Finally write the data to a temporary file
        input_file.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)

        new_img = models.Image(id=request.POST['id'], img=url)
        request.dbsession.add(new_img)
    return {'obj': 'obj11'}





# Its my comment