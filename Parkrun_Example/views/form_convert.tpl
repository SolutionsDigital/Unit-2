<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Currency converter</title>
</head>
<body>
    <h1>Currency converter</h1>
        <form method="GET" action="/convert">
            <label for="amount">Amount</label>
            <input type="text" name="amount">

            <label for="currency">Currency</label>
            <select name="currency">
                <option value="USD" selected>US Dollars</option>
                <option value="GBP">British pounds</option>
                <option value="EUR">Euros</option>
            </select>

            <input type="submit">
        </form>

    % if result:
    <h2> Result of conversion</h2>
    <p>{{currency}} {{amount}} = AUD {{result}}</p>
    % end

</body>
</html>
