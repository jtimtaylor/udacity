<!DOCTYPE html>
<html>
<head>
  <link type="text/css" rel="stylesheet" href="/static/main.css" />

  <title>CS 253 Blog</title>
</head>

<body>
  <a href="/blog" class="main-title">
    Tim's Blog!
  </a>
  <div>
    <a href="/blog/newpost">New post</a>

  <div class="login-area">
      <a class="login-link" href="/blog/login">login</a>
      |
      <a class="login-link" href="/blog/signup">signup</a>
  </div>
  <hr>
    %for post in blogposts:
      <div class="blogs">
        <div class="post-title">{{post[1]}}</div>
        <pre class="post-content">{{post[2]}}</pre>
      </div>
    %end
</body>

</html>
