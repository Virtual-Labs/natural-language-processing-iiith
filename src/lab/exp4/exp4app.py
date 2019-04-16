from flask import Flask, request ,redirect , render_template
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')



from flask_sqlalchemy import SQLAlchemy


from flask import json

from flask import jsonify





app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'


db = SQLAlchemy(app)

class BigramTable (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    formid = db.Column (db.Integer(),unique=False,nullable=False)
    corpus = db.Column (db.Integer(),unique=False , nullable=False  )
    answer = db.Column (db.String(4),unique=False ,nullable=False )

    def __init__ (self,corpus,formid,answer):
        self.corpus= corpus
        self.formid = formid 
        self.answer= answer 

#    def __repr__(self) :
#        return '<User %r>' % self.formid % self.answer

db.create_all()


class Quiztable (db.Model):
    id = db.Column (db.Integer(),primary_key=True)
    question = db.Column (db.String(140),nullable=False )
    opt1= db.Column (db.String(70),nullable=False)
    opt2= db.Column (db.String(70),nullable=False)
    opt3= db.Column (db.String(70),nullable=False)
    opt4= db.Column (db.String(70),nullable=False)
    answer= db.Column (db.String(70),nullable=False)

    def __init__ (self,question,opt,answer):
        self.question = question
        self.opt1 = opt[0]
        self.opt2 = opt[1]
        self.opt3 = opt[2]
        self.opt4 = opt[3]
        self.answer = answer 




@app.route("/questions/create", methods= ["POST"])
def create ():
    question = request.form['question']
    opt1  = (request.form['opt1'])
    opt2  = (request.form['opt2'])
    opt3  = (request.form['opt3'])
    opt4  = (request.form['opt4'])
    answer= int (request.form['answer'])
    db.create_all()
    neQues = Quiztable (question=question , opt=[opt1,opt2,opt3,opt4] , answer=answer  )
    db.session.add(neQues)
    db.session.commit()
    temp = {
            'question': neQues.question ,
            'opt' : [opt1,opt2,opt3,opt4] ,
            'answer' : neQues.answer
            }    
    a= json.dumps (temp )
#    Student.query.all()
    return jsonify(a)







"""
def create (): 
    sentence1= "(eos) Can I sit near you (eos) You can sit (eos) Sit near him (eos) I can sit you (eos)"
    sentence1=sentence1.split()
    sentence=[]
    for i in sentence1:
        if i not in sentence:
            sentence.append(i)
    count=0 
    corpus=0
    for i in range(len(sentence)):
        for j in range(len(sentence)):
            formid=count
            count+=1
            counti=0
            countt=0
            for k in range(len(sentence1)):
                if sentence1[k]==sentence[i]:
                    counti+=1
                    if sentence[j]==sentence1[i+1]:
                        countt+=1
            answer=float(countt)/counti
            db.create_all()
            newentry=BigramTable(corpus,formid,answer)
            db.session.add(newentry)
            db.session.commit()

db.create_all()

print ("exec complete")
"""
                                                            













@app.route('/')
def root():
    return render_template("Introduction.html")

@app.route ('/Introduction.html')
def root1():
    return render_template("Introduction.html")

@app.route ('/Theory.html')
def root2():
    return render_template("Theory.html")

@app.route ('/Objective.html')
def root3():
    return render_template("Objective.html")

@app.route ('/Quizzes.html')
def root4():
    db.create_all()
    allques = Quiztable.query.all()
    quesarr=[]
    for quesa in allques :
        l=[]
        opt=[]
        l.append(quesa.question)
        opt.append(quesa.opt1)
        opt.append(quesa.opt2)
        opt.append(quesa.opt3)
        opt.append(quesa.opt4)
        l.append(opt)
        l.append(quesa.answer)
        quesarr.append(l)
    return render_template("Quizzes.html",quizarr=quesarr)



@app.route('/parse',methods=['POST'])
def rootwq():
    global mystr1  
    mystr1 = ""
    mystr1 += str(request.get_data())
#    mystr1=mystr1.split(" ")
    mystr1=mystr1[2:-1:]
    print (mystr1)
    return mystr1
#    return redirect('/Experiment.html')

@app.route ('/Experiment.html',methods=['GET','POST'])
def experiment ():
        return render_template("Experiment.html",mystr=[],n=0)


@app.route ('/Experiment1.html',methods=['GET','POST'])
def experiment1 ():
    if request.method== 'POST':
        mystr1 = str(request.get_data())
        print ("ok")
        mystr1=mystr1.split()
        print (mystr1)
        print (len(mystr1))
        print ("ok")
        return render_template("Experiment1.html",mystr=mystr1,n=len(mystr1))
    elif request.method=='GET':
        mystr1 = str(request.get_data())
        mystr1=mystr1.split()
        return render_template("Experiment1.html",mystr=mystr1,n=len(mystr1))
"""
    global mystr1
#   mystr1 =rootwq()
    mystr = str(mystr1).split()
#    print (mystr,"dfsgdfg")
    if mystr == "" or mystr ==[] or len (mystr)==0 :
        return render_template("Experiment.html",mystr=["abc","bcd","cda"],n=3)
    else: 
        return render_template("Experiment.html",mystr=mystr,n=len(mystr))
"""

"""
@app.route ('/checkans.html',methods=['GET','POST'])
def hello():
    userans=""
    cno=str(request.get_data())
    count=0
    if(cno==0):
        count=7
    else:
        count=11
    answers=BigramTable.query.all()
    for i in range(count):
        inputans=request.form['form'+str(count)]
        for ans in answers:
            if(str(ans.formid)==str(count) and str(ans.corpus)==str(cno)):
                if str(ans.answer)==str(inputans):
                    userans+='1'
                else:
                    userans+='0'
    print(userans)
    return userans
"""
@app.route ('/Procedure.html')
def root5():
    return render_template("Procedure.html")

@app.route ('/Further Readings.html')
def root6():
    return render_template("Further Readings.html")


@app.route ('/Feedback.html')
def root7():
    
    return render_template("Feedback.html")



@app.route("/quizans.html",methods=['GET','POST'])
def quizans():
    i=1
    n=0
    allans=Quiztable.query.all()
    arr=[]
    ansarr=[]
    score=[]
    for ele in allans:
        qrstr=""
        qrstr="quest_"+str(i)
        ansarr.append(ele.answer)
        userans = request.form[qrstr]
        arr.append(userans)
        i+=1
    for j in range(i-1):
        if str(arr[j])==str(ansarr[j]):
            score.append(1)
            n+=1
        else :
            score.append(0)
    print (ansarr)
    print (arr)
    return render_template("quizans.html",score=score,arr=arr,ansarr=ansarr,n=n)

# @app.route ('/Introduction.html')
#     return render_template("Introduction.html")

# @app.route ('/Introduction.html')
#     return render_template("Introduction.html")

# @app.route ('/Introduction.html')
#     return render_template("Introduction.html")



if __name__ == "__main__":
    mystr2 ="hello boy hi " 
    app.run()
