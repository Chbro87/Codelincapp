
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

#first page (MAIN PAGE Intro)
@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


# Math Starts
@app.route('/input', methods=["GET", "POST"])
def input():
    if request.method == 'POST':
        salary = request.form['salary']
        #FIXED EXPENSES 
        expenses1 =request.form.getlist('field1[]')
        total_fixed = 0
        for value in expenses1: 
            total_fixed +=  float(value)
        fix_num = (0.5*float(salary))/total_fixed

        #FLEX EXPENSES
        expenses2 =request.form.getlist('field2[]')
        print(expenses2)
        total_flex = 0
        for value in expenses2: 
            total_flex +=  float(value)
        flex_num = (0.3*float(salary))/total_flex
        #SAVE EXPENSES
        expenses3 =request.form.getlist('field3[]')
        total_save = 0
        for value in expenses3: 
            total_save +=  float(value)
        save_num = (0.2*float(salary))/total_save

        labels = [
            'Fixed Income',
            'Flexable Spending',
            'Savings',
            
        ]
        fix_grade = 0
        flex_grade = 0
        save_grade = 0

        if fix_num >= 2:
            fix_grade = 6
        elif fix_num >= 1 and fix_num < 2:
            fix_grade = 5
        elif fix_num >= 0.8 and fix_num < 1:
            fix_grade = 4
        elif fix_num >= 0.6 and fix_num < 0.8:
            fix_grade = 3
        elif fix_num >= 0.4 and fix_num < 0.6:
            fix_grade = 2
        else:
            fix_grade = 1

        if flex_num >= 2:
            flex_grade = 6
        elif flex_num >= 1 and flex_num < 2:
            flex_grade = 5
        elif flex_num >= 0.8 and flex_num < 1:
            flex_grade = 4
        elif flex_num >= 0.6 and flex_num < 0.8:
            flex_grade = 3
        elif flex_num >= 0.4 and flex_num < 0.6:
            flex_grade = 2
        else:
            flex_grade = 1

        if save_num >= 2:
            save_grade = 6
        elif save_num >= 1 and save_num < 2:
            save_grade = 5
        elif save_num >= 0.8 and save_num < 1:
            save_grade = 4
        elif save_num >= 0.6 and save_num < 0.8:
            save_grade = 3
        elif save_num >= 0.4 and save_num < 0.6:
            save_grade = 2
        else:
            save_grade = 1


        overall_grade = (fix_grade + flex_grade + save_grade)/3

        letter_grade = 0
        if overall_grade == 6:
            letter_grade = "A+"
        elif overall_grade >= 5 and overall_grade < 6:
            letter_grade = "A"
        elif overall_grade >= 4 and overall_grade < 5:
            letter_grade = "B"
        elif overall_grade >= 3 and overall_grade < 4:
            letter_grade = "C"
        elif overall_grade >= 2 and overall_grade < 3:
            letter_grade = "D"
        else: 
            letter_grade = "F"
        
        print(letter_grade)

        # Math ENDS



        
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

@app.route("/goal")
def goal():
    return render_template('goal.html')