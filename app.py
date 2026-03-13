from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/favorite-course')
def favorite_course():
    # Grabs ?subject=BMGT&course_number=407 from the URL
    subject = request.args.get('subject', 'BMGT')
    course_num = request.args.get('course_number', '407')
    return render_template('favorite-course.html', subject=subject, course_num=course_num)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # This part runs AFTER you hit submit
        first = request.form.get('first_name')
        last = request.form.get('last_name')
        email = request.form.get('email')
        major = request.form.get('major')
        return render_template('contact.html', submitted=True, first=first, last=last, email=email, major=major)

    # This part runs when you first visit the page
    return render_template('contact.html', submitted=False)