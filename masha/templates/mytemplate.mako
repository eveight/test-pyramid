<%inherit file="base.mako"/>
<%def name="title()">
    - Second Level
  </%def>

<%def name="main()">
<form action="/home2" method="post" enctype="multipart/form-data">
    <div class="form-group">
        <input type="number" class="form-control" id="exampleInputNumber" name="id">
    </div>
    <div class="form-group">
        <input type="text" class="form-control" id="exampleInputText" name="test">
    </div>
    <div class="form-group">
        <input type="text" class="form-control" id="exampleInputText" name="name">
    </div>
    <div class="form-group">
        <input type="number" class="form-control" id="exampleInputNumber" name="chislo">
    </div>
    <div class="form-group">
        <label for="exampleFormControlFile1">Example file input</label>
        <input type="file" class="form-control-file" id="exampleFormControlFile1" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
  </%def>