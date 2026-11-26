from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")

def inicial():
    
    return render_template("index.html")

@app.route("/formulario.html")

def form():
    
    return render_template("formulario.html")

@app.route("/mamiferos.html")

def mamiferos():
    
    return render_template("mamiferos.html")

@app.route("/aves.html")

def aves():
    
    return render_template("aves.html")

@app.route("/peces.html")

def peces():
    
    return render_template("peces.html")

@app.route("/reptiles.html")

def reptiles():
    
    return render_template("reptiles.html")


@app.route("/anfibios.html")

def anfibios():
    
    return render_template("anfibios.html")




if __name__ == "__main__":
    app.run(debug=True)