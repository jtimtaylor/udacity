<!DOCTYPE html>

<html>
  <head>
    <title>Login Page</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>

  <body>
    <h2>Login</h2>
    <form method="post">
    <table>
        <tr>
            <td class="label">
                Username
            </td>
            <td>
                <input type="text" name="username" value="{{username}}">
            </td>
            <td class="error">
                {{!username_error}}
            </td>
        </tr>
        <tr>
            <td class="label">
                Password
            </td>
            <td>
                <input type="password" name="password" value="">
            </td>
            <td class="error">
                {{password_error}}
            </td>
    </table>
    <br>
    <input type="submit">
    </form>
  </body>
</html>
