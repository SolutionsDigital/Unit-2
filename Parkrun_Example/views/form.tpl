<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Testing forms with the bottle framework</title>
</head>
<body>
    <h1>Form Page</h1>
        <form method="post" action="/using_forms">
            <fieldset>
                <legend>
                    SAMPLE FORM
                </legend>
                <ul>
                    <li>First Name: <input name="first"></li>
                    <li>Last Name: <input name="last"></li>
                </ul>
                <input type="submit" value="Submit Form">
            </fieldset>

            <p>{{message}}</p>
</body>
</html>
