from bottle import Bottle, template

app=Bottle()
path_to_templates = template_lookup=["./views"]

@app.route("/include1")
def include1_template():
    tpl = """
    <HTML>
      <HEAD><TITLE>{{title}}</TITLE></HEAD>
      <BODY>
      % include('menu.tpl')
      <H1>{{title}}</H1>
      </BODY>
    </HTML>
    
    """
    return template(tpl, title="Hello World!", template_lookup=path_to_templates)

@app.route("/include2")
def include2_template():
    tpl = """
    <HTML>
      <HEAD><TITLE>{{item}}</TITLE></HEAD>
      <BODY>
      % include('menu.tpl')
      <H1>{{item}}</H1>
      </BODY>
    </HTML>
    
    """
    return template(tpl, item="A shoe!", template_lookup=path_to_templates)


if __name__ == "__main__":
    app.run(Debug=True)
