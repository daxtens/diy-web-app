<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Generate your very own witty political slogans!">
    <meta name="author" content="Daniel Axtens">
    <link rel="shortcut icon" href="/static/ico/favicon.png">

    <title>Slogan Generator</title>

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
          <li class="active"><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
        <h3 class="text-muted">Slogan Generator</h3>
      </div>

      <div class="jumbotron">
        <h1>{{slogan}}</h1>
        <p class="lead">If you can't boil it down to a slogan, you
        can't sell it.</p>
        <p><a class="btn btn-lg btn-success" href="/" role="button">Generate more policy</a></p>
      </div>

      <div class="row marketing">
        <div class="col-lg-6">
          <h4>What is this?</h4>
          <p>CompCon 2013 "From 0 to DIY Web App in 120 minutes" Slogan Generator demo app.</p>
	</div>

	<div class="col-lg-6">
          <h4>Who is responsible for this travesty?</h4>
          <p>Daniel Axtens. <a href="mailto:daniel@axtens.net">daniel@axtens.net</a> @daxtens on twitter.</p>
	  <p>Definitely <emph>not</emph> the CompCon 2013 organisers.</p>
	</div>

	<div class="col-lg-6">
          <h4>I have a better slogan!</h4>
          <p>Excellent. You'll be able to submit it soon.</p>
        </div>

      </div>

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
