from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__) 

def convert(milisec):
    # milisec = int(input("Milisec : "))
    milisec=int(milisec)
    h,m,s = 0,0,0
    res=""
    if milisec<1000:
        print(f"just {milisec} milisecond/s")
        res += "just " + str(milisec) + " miliseconds "
        return res 
    else:
        if milisec>=3600000:
            h = milisec//3600000
            milisec = milisec%3600000
            res += str(h) + " hour/s "
            
        if milisec>=60000:
            m = milisec//60000
            milisec = milisec%60000
            print(m,"minute/s",end=" ")
            res += str(m) + " minute/s "
        if milisec>=1000:
            s = milisec//1000
            print(s,"second/s")
            res += str(s) + " second/s "
        return res
        
@app.route("/",methods=['GET','POST'])

def home():
    if request.method == 'POST':
        num = request.form['number']
        if not num.isdigit():
            return render_template("index.html",not_valid=True,developer_name="johnS.")
        elif float(num) < 1:
            return render_template("index.html",not_valid=True,developer_name="johnS.")        
        result = convert(num)
        return render_template("result.html",developer_name="johnS.",milliseconds=num,result=result)
    else:
        return render_template("index.html",developer_name="johnS.")

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0",port=80)