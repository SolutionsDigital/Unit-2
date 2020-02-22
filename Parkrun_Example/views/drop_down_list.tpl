<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Drop down list</title>
</head>
<body>
    <h1>Sample drop down list</h1>
        <form method="POST" action="/dropdown">
            <label for="currency">Club</label>
            <select name="Club">
                % for club in ClubNames:
                <!--ClubNames is a list of lists so club is a list-->
                   <option value={{club[1]}}>{{club[0]}}</option>
                % end
                <input type="submit">
            </select>
        </form>

</body>
</html>
