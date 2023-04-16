
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

#first page (MAIN PAGE Intro)
@app.route("/")
def hello_world():
    return render_template('base.html')

@app.route("/about")
def about():
    return render_template('about.html')



@app.route('/input', methods=["GET", "POST"])
def input():
    if request.method == 'POST':
        #FIXED EXPENSES 
        expenses1 =request.form.getlist('field1[]')
        total_fixed = 0
        for value in expenses1: 
            total_fixed +=  float(value)
            print(value)
        print(total_fixed)
        #FLEX EXPENSES
        expenses2 =request.form.getlist('field2[]')
        total_flex = 0
        for value in expenses2: 
            total_flex +=  float(value)
            print(value)
        print(total_flex)
        #SAVE EXPENSES
        expenses3 =request.form.getlist('field3[]')
        total_save = 0
        for value in expenses3: 
            total_save +=  float(value)
            print(value)
        print(total_save)
        labels = [
            'Fixed Income',
            'Flexable Spending',
            'Savings',
            
        ]

        data = [total_fixed,total_flex,total_save]
        goal_fix = 0.5
        goal_flex = 0.3
        goal_save = 0.2
       
        #text = request.form['text']
        total = total_fixed + total_flex + total_save
    #differnces between the amounts
        percent_fix = total_fixed/total 
        percent_flex = total_flex/total
        percent_save = total_save/total
        
        print (percent_fix)
        print(percent_flex)
        print(percent_save)
        fix_diff = goal_fix - percent_fix 
        flex_diff = goal_flex - percent_flex
        save_diff = goal_save - percent_save
        print(fix_diff)
        print(flex_diff)
        print(save_diff)

        grade = (fix_diff + flex_diff + save_diff)/3.0
        print("Average diff: " , grade)
        return render_template(
            template_name_or_list='chartjs-example.html',
            data=data,
            labels=labels,
        )
    else:
        return render_template("fixed.html")