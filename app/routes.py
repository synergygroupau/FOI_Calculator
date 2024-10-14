from datetime import datetime, timezone
from urllib.parse import urlsplit
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, \
    EmptyForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm, SurveyForm, EditSurveyForm, ExemptionForm
from app.models import User, Post, Survey, Exemption
from app.email import send_password_reset_email


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()


# @app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = db.paginate(current_user.following_posts(), page=page,
                        per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@app.route('/index_survey', methods=['GET', 'POST'])
@login_required
def index_survey():
    # form = SurveyForm()
    # if form.validate_on_submit():
    #     survey = Survey(
    #         body=form.survey.data,
    #         author=current_user,
    #         field1 = form.field1.data,
    #         field2 = form.field2.data,
    #         field3 = form.field3.data
    #     )
    #     db.session.add(survey)
    #     db.session.commit()
    #     flash('Your survey is now live!')
    #     return redirect(url_for('index_survey'))


    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey(
            author=current_user,
            survey_name = form.survey_name.data
        )

        db.session.add(survey)
        db.session.commit()
        flash('Survey created!')
        return redirect(url_for('edit_survey',id=survey.id))


    page = request.args.get('page', 1, type=int)
    surveys = db.paginate(current_user.following_surveys(), page=page,
                        per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('index_survey', page=surveys.next_num) \
        if surveys.has_next else None
    prev_url = url_for('index_survey', page=surveys.prev_num) \
        if surveys.has_prev else None
    return render_template('index_survey.html', title='Home',
                           surveys=surveys.items, next_url=next_url,
                           prev_url=prev_url,form=form)

   
@app.route('/new_survey', methods=['GET', 'POST'])
@login_required
def new_survey():
    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey(
            author=current_user,
            survey_name = form.survey_name.data,

            field1 = form.field1.data,
            comment1 = form.comment1.data,

            field2 = form.field2.data,
            comment2=  form.comment2.data,

            field3 = form.field3.data,
            comment3 = form.comment3.data,

            field4 = form.field4.data,
            comment4 = form.comment4.data,

            field5 = form.field5.data,
            comment5 = form.comment5.data,

            field6 = form.field6.data,
            comment6 = form.comment6.data,

            field7 = form.field7.data,
            comment7 = form.comment7.data,

            field8 = form.field8.data,
            comment8 = form.comment8.data,

            field9 = form.field9.data,
            comment9 = form.comment9.data,

            field10 = form.field10.data,
            comment10 = form.comment10.data,

            field11 = form.field11.data,
            field12 = form.field12.data,
            comment12 = form.comment12.data,

            field13 = form.field13.data,
            comment13 = form.comment13.data,

            field14 = form.field14.data,
            comment14 = form.comment14.data,

            field15 = form.field15.data,
            comment15 = form.comment15.data,

            field16 = form.field16.data,
            comment16 = form.comment16.data,

            field17 = form.field17.data,
            comment17 = form.comment17.data,

            field18 = form.field18.data,
            comment18 = form.comment18.data,

            field19 = form.field19.data,
            comment19 = form.comment19.data,
           
            result=form.result.data
            
        )
        db.session.add(survey)
        db.session.commit()
        flash('Survey submitted!')
        return redirect(url_for('index_survey'))
    # page = request.args.get('page', 1, type=int)
    # surveys = db.paginate(current_user.following_surveys(), page=page,
    #                     per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    # next_url = url_for('index_survey', page=surveys.next_num) \
    #     if surveys.has_next else None
    # prev_url = url_for('index', page=surveys.prev_num) \
    #     if surveys.has_prev else None
    return render_template('new_survey.html', title='New survey', form1=form,form2=form)

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    query = sa.select(Post).order_by(Post.timestamp.desc())
    posts = db.paginate(query, page=page,
                        per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Explore', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/exemptions')
@login_required
def exemptions():
    page = request.args.get('page', 1, type=int)
    query = sa.select(Post).order_by(Post.timestamp.desc())
    # posts = db.paginate(query, page=page,
    #                     per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    # next_url = url_for('explore', page=posts.next_num) \
    #     if posts.has_next else None
    # prev_url = url_for('explore', page=posts.prev_num) \
    #     if posts.has_prev else None
    return render_template('exemptions.html', title='Exemptions')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index_survey'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index_survey')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index_survey'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index_survey'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index_survey'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data))
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index_survey'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index_survey'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    page = request.args.get('page', 1, type=int)
    query = user.posts.select().order_by(Post.timestamp.desc())
    posts = db.paginate(query, page=page,
                        per_page=app.config['POSTS_PER_PAGE'],
                        error_out=False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url, form=form)


@app.route('/survey/<id>')
@login_required
def survey(id):
    survey = db.first_or_404(sa.select(Survey).where(Survey.id == id))
    page = request.args.get('page', 1, type=int)
    # query = user.surveys.select().order_by(Survey.timestamp.desc())
    # surveys = db.paginate(query, page=page,
    #                     per_page=app.config['POSTS_PER_PAGE'],
    #                     error_out=False)
    # next_url = url_for('survey', id=survey.id, page=surveys.next_num) \
    #     if surveys.has_next else None
    # prev_url = url_for('survey', id=survey.id, page=survey.prev_num) \username
    #     if survey.has_prev else None
    form = EmptyForm()
    return render_template('survey.html', survey=survey)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/edit_survey/<id>', methods=['GET', 'POST'])
@login_required
def edit_survey(id):
    survey = db.first_or_404(sa.select(Survey).where(Survey.id == id))

   
    
    form1 = EditSurveyForm(id)
    form2 = ExemptionForm()


    if form2.validate_on_submit():
        exemption = Exemption(
            exemption_name=form2.exemption_name.data,
            exemption_instance=form2.exemption_instance.data,
            exemption_multiplier=form2.exemption_multiplier.data,
            exemption_time=form2.exemption_time.data,
            survey_id = survey.id
            
        )


        db.session.add(exemption)
        db.session.commit()
        # flash('Exemption submitted!')
        
        


    if form1.validate_on_submit():
        survey.survey_name = form1.survey_name.data

        survey.field1 = form1.field1.data
        survey.comment1=form1.comment1.data

        survey.field2 = form1.field2.data
        survey.comment2=form1.comment2.data

        survey.field3 = form1.field3.data
        survey.comment3 = form1.comment3.data

        survey.field4 = form1.field4.data
        survey.comment4 = form1.comment4.data

        survey.field5 = form1.field5.data
        survey.comment5 = form1.comment5.data

        survey.field6 = form1.field6.data
        survey.comment6 = form1.comment6.data

        survey.field7 = form1.field7.data
        survey.comment7 = form1.comment7.data

        survey.field8 = form1.field8.data
        survey.comment8 = form1.comment8.data

        survey.field9 = form1.field9.data
        survey.comment9 = form1.comment9.data

        survey.field10 = form1.field10.data
        survey.comment10 = form1.comment10.data

        survey.field11 = form1.field11.data
        survey.field12 = form1.field12.data
        survey.comment12 = form1.comment12.data

        survey.field13 = form1.field13.data
        survey.comment13 = form1.comment13.data

        survey.field14 = form1.field14.data
        survey.comment14 = form1.comment14.data

        survey.field15 = form1.field15.data
        survey.comment15 = form1.comment15.data

        survey.field16 = form1.field16.data
        survey.comment16 = form1.comment16.data

        survey.field17 = form1.field17.data
        survey.comment17 = form1.comment17.data

        survey.field18 = form1.field18.data
        survey.comment18 = form1.comment18.data

        survey.field19 = form1.field19.data
        survey.comment19 = form1.comment19.data
        
        survey.result=form1.result.data
            
        
    
        db.session.commit()
        flash('Your changes have been saved.')
    

        return redirect(url_for('edit_survey', id=id)) 
    

    elif request.method == 'GET':
        form1.survey_name.data = survey.survey_name

        form1.field1.data = survey.field1
        form1.comment1.data = survey.comment1

        form1.field2.data = survey.field2
        form1.comment2.data = survey.comment2

        form1.field3.data = survey.field3
        form1.comment3.data = survey.comment3

        form1.field4.data = survey.field4
        form1.comment4.data = survey.comment4

        form1.field5.data = survey.field5
        form1.comment5.data = survey.comment5

        form1.field6.data = survey.field6
        form1.comment6.data = survey.comment6

        form1.field7.data = survey.field7
        form1.comment7.data = survey.comment7

        form1.field8.data = survey.field8
        form1.comment8.data = survey.comment8

        form1.field9.data = survey.field9
        form1.comment9.data = survey.comment9

        form1.field10.data = survey.field10
        form1.comment10.data = survey.comment10

        form1.field11.data = survey.field11
        form1.field12.data = survey.field12
        form1.comment12.data = survey. comment12

        form1.field13.data = survey.field13
        form1.comment13.data = survey.comment13

        form1.field14.data = survey.field14
        form1.comment14.data = survey.comment14

        form1.field15.data = survey.field15
        form1.comment15.data = survey.comment15

        form1.field16.data = survey. field16
        form1.comment16.data = survey.comment16

        form1.field17.data = survey.field17
        form1.comment17.data = survey.comment17

        form1.field18.data = survey.field18
        form1.comment18.data = survey.comment18

        form1.field19.data = survey.field19
        form1.comment19.data = survey.comment19
        
        form1.result.data = survey.result

    
    exemptions = db.paginate(survey.following_exemptions(),error_out=False)
        

    

    return render_template('edit_survey.html', exemptions=exemptions.items, title='Edit Survey',
                           form1=form1,form2=form2)




