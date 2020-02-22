<html>
<head>Team form</head>
<body>
<h1>Team creation</h1>
<form method="POST" action="/team_creation">
    <fieldset>
        <legend>What's the name of the team you would like to create?</legend>
        <li>Enter a team name: <input name="teams"></li>
        <input type="submit" value="Submit Form">
    </fieldset>
</form>
<h1>Team registration</h1>
<form method="POST" action="/teams">
    <fieldset>
        <legend>Which team would you like to join?</legend>
         <form method="POST" action="/team_creation">
            <label for="Teams">Club</label>
            <select name="Teams">
                % for team in teams:
                <!--ClubNames is a list of lists so club is a list-->
                   <option name="option" value={{team[1]}}>{{team[0]}}</option>
                % end
                <input type="submit">
            </select>
        </form>
    </fieldset>
</body>
</html>
