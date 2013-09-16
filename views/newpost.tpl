<!DOCTYPE html>
<html>
<head>
  <link type="text/css" rel="stylesheet" href="/static/main.css" />

  <title>New Post</title>
</head>

<body>
  <h1>New Post</h1>
  <form method="post">
    <label>
      <div>Title</div>
      <input type="text" name="subject" value="{{subject}}">
    </label>

    <label>
      <div>Content</div>
        <textarea name="content">{{content}}</textarea>
    </label>
    <div class="error">
      {{error}}
    </div>
    <input type="submit">

</body>

</html>
