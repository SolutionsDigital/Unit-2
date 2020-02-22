<html>
<body>
<p>Here are the current teams</p>
<table border="1">
    %for row in rows:
    <tr>
        %for col in row:
          <td>{{col}}</td>
        %end
    </tr>
    %end
</table>
<p>Create a new team</p>
<form action="/teams" method="post">
    <input type="text" size="100" maxlength="100" name="newteam">
    <input type="submit" value="Submit New Team">
</form>
</body>
</html>
