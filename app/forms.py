from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FloatField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
import sqlalchemy as sa
from app import db
from app.models import User, Survey


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError('Please use a different username.')
            
class EditSurveyForm(FlaskForm):
    
    
    field1 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment1 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field2 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment2 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field3 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment3 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field4 = FloatField('Amount', validators=[DataRequired()])
    comment4 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field5 = FloatField('Amount', validators=[DataRequired()])
    comment5 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field6 = FloatField('Amount', validators=[DataRequired()])
    comment6 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field7 = FloatField('Amount', validators=[DataRequired()])
    comment7 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field8 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment8 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field9 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment9 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field10 = FloatField('Amount', validators=[DataRequired()])
    comment10 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field11 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    field12 = FloatField('Consultations', validators=[DataRequired()])

    comment12 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field13 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment13 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field14 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment14 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field15 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment15 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field16 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment16 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field17 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment17 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field18 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment18 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field19 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment19 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])


    result = FloatField('Total', validators=[DataRequired()])
    submit = SubmitField('Save')

    def __init__(self, original_survey_content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_survey_content = original_survey_content
    
    # def __init__(self, original_survey, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.survey.data = original_survey.body
    #     self.field1.data = original_survey.field1
    #     self.field2.data = original_survey.field2
    #     self.field3.data = original_survey.field3

    # def validate_survey(self, survey):
    #     if survey.data != self.original_survey_content:
    #         existing_survey = db.session.scalar(sa.select(Survey).where(
    #             Survey.body == survey.data)) 
    #         if existing_survey is not None:
    #             raise ValidationError('Please use a different survey response.')


class EmptyForm(FlaskForm): 
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class SurveyForm(FlaskForm):
    field1 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment1 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field2 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment2 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field3 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment3 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field4 = FloatField('Amount', validators=[DataRequired()])
    comment4 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field5 = FloatField('Amount', validators=[DataRequired()])
    comment5 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field6 = FloatField('Amount', validators=[DataRequired()])
    comment6 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field7 = FloatField('Amount', validators=[DataRequired()])
    comment7 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field8 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment8 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field9 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment9 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field10 = FloatField('Amount', validators=[DataRequired()])
    comment10 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field11 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    field12 = FloatField('Consultations', validators=[DataRequired()])

    comment12 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field13 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment13 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field14 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment14 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field15 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment15 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field16 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment16 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field17 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment17 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field18 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment18 = TextAreaField('Say something', validators=[Length(min=0, max=140)])

    field19 = SelectField('Time Taken', choices=[(1, 1), (1.5, 1.5),(2, 2)],coerce=float,validators=[DataRequired()])
    comment19 = TextAreaField('Say something', validators=[Length(min=0, max=140)])


    result = FloatField('Total', validators=[DataRequired()])
    submit = SubmitField('Submit')