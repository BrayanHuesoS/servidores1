from flask import Flask, render_template,url_for
servidor1 = Flask(_name_)
@servidor1.route('/inicio')
def home():
    return render_template ('template.html')
    if _name_ == '_main_':
        servidor1.run(debug=True, port=5001)