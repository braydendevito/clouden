print ('''<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{{ url_for('static', filename='jquery.mobile-1.4.5.min.css')}}">
<link rel="stylesheet" href="{{ url_for('static', filename='style.css')}}">
<script src="{{ url_for('static', filename='jquery-1.11.2.min.js')}}"></script>
<script src="{{ url_for('static', filename='jquery.mobile-1.4.5.min.js')}}"></script>
</head>
<center>
<div data-role="page" id="pageone">
  <div data-role="header">
  </div>
  <div data-role="main" class="ui-content">
<center>
<img src="{{ url_for('static', filename='logo.png')}}" width="100%">
<h1 class="close">Wi-Fi Configuration</h1>

</center>
    <div class="CSSTableGenerator">
<table>
<tbody>
<tr><td><h2 class="close"><a href="#pagetwo" data-transition="flip">''')
with open('iwlist/sep1.txt', 'r') as infile:
	data = infile.read()
print (data[0:0]+data[1-1:14])

print ('''</a>
<tr><td><h2 class="close"><a href="#pagetwo" data-transition="flip">''')
with open('iwlist/sep2.txt', 'r') as infile:
	data = infile.read()
print (data[0:0]+data[1-1:14])

print ('''</a>
<tr><td><h2 class="close"><a href="#pagetwo" data-transition="flip">''')
with open('iwlist/sep3.txt', 'r') as infile:
	data = infile.read()
print (data[0:0]+data[1-1:14])

print ('''</a>
<tr><td><h2 class="close"><a href="#pagetwo" data-transition="flip">''')
with open('iwlist/sep4.txt', 'r') as infile:
	data = infile.read()
print (data[0:0]+data[1-1:14])
print ('''</a>
<tr><td><h2 class="close"><a href="#pagetwo" data-transition="flip">''')
with open('iwlist/sep5.txt', 'r') as infile:
	data = infile.read()
print (data[0:0]+data[1-1:14])
print ('''</a>
</tbody>
</table>
</div>
  </div>
</div> 
<div data-role="page" data-dialog="true" id="pagetwo">
  <div data-role="header">
    <h1>Wi-Fi name</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>
<input class="textbox" type="input">


    </div>
</div> 
</div>
</html>''')
