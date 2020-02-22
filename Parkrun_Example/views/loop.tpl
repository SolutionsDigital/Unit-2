<html>
    <head><title>{{header}}</title></head>
    <body>
         <h1>{{header}}</h1>

         <ul>
          % for name in students:
             <li>{{name}}</li>
          % end
         </ul>

    </body>
</html>
