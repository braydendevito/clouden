with open('sep1.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid1 = ''.join(lhs.split())[:-2]
#####
with open('sep2.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid2 = ''.join(lhs.split())[:-2]
#####
with open('sep3.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid3 = ''.join(lhs.split())[:-2]
#####
with open('sep4.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid4 = ''.join(lhs.split())[:-2]
####
with open('sep5.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid5 = ''.join(lhs.split())[:-2]
####
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
<img src="{{ url_for('static', filename='logo.png')}}" width="70%">
<br>
<br>

<h1 class="close">Wi-Fi Configuration</h1>

</center>
    <div class="CSSTableGenerator">
<table>
<tbody>
<tr><td><h2 class="close"><a href="#one" data-transition="flip">''')
print ssid1
print ('''</a>
<tr><td><h2 class="close"><a href="#two" data-transition="flip">''')
print ssid2
print ('''</a>
<tr><td><h2 class="close"><a href="#three" data-transition="flip">''')
print ssid3
print ('''</a>
<tr><td><h2 class="close"><a href="#four" data-transition="flip">''')
print ssid4
print ('''</a>
<tr><td><h2 class="close"><a href="#five" data-transition="flip">''')
print ssid5
print ('''</a>
</tbody>
</table>
</div>
  </div>
</div> 
<div data-role="page" data-dialog="true" id="one">
  <div data-role="header">
    <h1>''')
print ssid1
print ('''</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>

<form method="POST">
        {{ form.hidden_tag() }}
        {{ form.password }}
        <input type="submit" value="CONNECT"/>
    </form>


    </div>
</div> 
</div>
<div data-role="page" data-dialog="true" id="two">
  <div data-role="header">
    <h1>''')
print ssid2
print ('''</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>

<form method="POST">
        {{ form.hidden_tag() }}
        {{ form.password }}
        <input type="submit" value="CONNECT"/>
    </form>


    </div>
</div> 
</div>
<div data-role="page" data-dialog="true" id="three">
  <div data-role="header">
    <h1>''')
print ssid3
print ('''</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>

<form method="POST">
        {{ form.hidden_tag() }}
        {{ form.password }}
        <input type="submit" value="CONNECT"/>
    </form>


    </div>
</div> 
</div>
<div data-role="page" data-dialog="true" id="four">
  <div data-role="header">
    <h1>''')
print ssid4
print ('''</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>

<form method="POST">
        {{ form.hidden_tag() }}
        {{ form.password }}
        <input type="submit" value="CONNECT"/>
    </form>


    </div>
</div> 
</div>


<div data-role="page" data-dialog="true" id="five">
  <div data-role="header">
    <h1>''')
print ssid5
print ('''</h1>
  </div>
  <div data-role="main" class="ui-content">
    <p>Please enter your Wi-Fi password.
<br><br>

<form method="POST">
        {{ form.hidden_tag() }}
        {{ form.password }}
        <input type="submit" value="CONNECT"/>
    </form>


    </div>
</div> 
</div>



</html>''')
