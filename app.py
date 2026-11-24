from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        # Ambil parameter dari form berdasarkan atribut name="nama"
        nama = request.form.get("hilmi", "").strip()
        if nama:
            hasil = f"Mantap,{nama} kamu hadir ☝🏻"
        else:
            hasil = "Nama tidak boleh kosong."
    return render_template("index.html", hasil=hasil)

if __name__ == "_main_":
    app.run(debug=True)