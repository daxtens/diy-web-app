%setdefault('active',None)
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Generate your very own witty political slogans!">
    <meta name="author" content="Daniel Axtens">
    <link rel="shortcut icon" href="/static/ico/favicon.png">

    <title>{{get('title', "Slogan Generator")}}</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/jumbotron-narrow.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/static/js/html5shiv.js"></script>
      <script src="/static/js/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="container">
      <div class="header">
        <ul class="nav nav-pills pull-right">
          <li class="{{'active' if active == 'Home' else ''}}"><a href="/">Home</a></li>
          <li class="{{'active' if active == 'About' else ''}}"><a href="#">About</a></li>
          <li class="{{'active' if active == 'Contact' else ''}}"><a href="/contact">Contact</a></li>
        </ul>
        <h3 class="text-muted">Slogan Generator</h3>
      </div>

      %include

      <div class="footer">
        <p>&copy; Daniel Axtens 2013</p>
      </div>

    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
