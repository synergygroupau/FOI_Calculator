from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FloatField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
import sqlalchemy as sa
from app import db
from app.models import User, Survey
import os
import csv
from flask import current_app

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
    survey_name = StringField('Name', validators=[DataRequired(),Length(min=0, max=140)])
    
    field1 = SelectField('Time Taken', choices=[(1, "1 hour"), (1.5, "1.5 hours"),(2, "2 hours")],coerce=float,validators=[DataRequired()],
                         description="Reading into file - Existing file, with correspendence (Not 'discovered' documents)")
    
    comment1 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field2 = SelectField('Time Taken', choices=[(0.6, "0.6 hours"), (1.2, "1.2 hours"),(1.8, "1.8 hours")],coerce=float,validators=[DataRequired()],
                         description="With OOT matters - and if the documents provided by agency are 'out of scope,' i.e. there are excess documents. This will require file notes a) identifying the relevant documents or pages within a given document, e.g. Document 10, pages 6-11. b) Relevant detials contained in the 'out of scope' document, c) rationale as to why the document or pages are not 'in scope,' and d) covering email with a copy of the file note, explaining the removal of the documents/pages. ")
    comment2 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field3 = SelectField('Time Taken', choices=[(0.6, "0.6 hours"), (1.2, "1.2 hours"),(1.8, "1.8 hours")],coerce=float,validators=[DataRequired()],
                         description="Creating schedule of 'in scope' documents")
    comment3 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field4 = FloatField('Amount', validators=[DataRequired()],
                        description="a) Initial review of confirmed 'in scope' documents (2min)")
    comment4 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field5 = FloatField('Amount', validators=[DataRequired()],
                        description="b) Identification of 3rd parties for consult (1min)")
    comment5 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field6 = FloatField('Amount', validators=[DataRequired()],
                        description="c) Summary Identification of Potential Exemption Arguments (PEAs - 1 min)")
    comment6 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field7 = FloatField('Amount', validators=[DataRequired()],
                        description="d) Summary of PEA & Inputting data into calculator (1 min)")
    comment7 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field8 = SelectField('Time Taken', choices=[(1, "1 hour"), (1.5, "1.5 hours"),(2, "2 hours"),(2.5,"2.5 hours"),(3,"3 hours")],coerce=float,validators=[DataRequired()],
                         description="Drafting Chronology for FOI Determination")
    comment8 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field9 = SelectField('Time Taken', choices=[(1, "1 hour"), (1.5, "1.5 hours"),(2, "2 hours"),(2.5,"2.5 hours"),(3,"3 hours")],coerce=float,validators=[DataRequired()],
                         description="Research & Review of background, policies & other materials for understanding material facts for FOI Determination")
    comment9 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field10 = FloatField('Amount', validators=[DataRequired()],
                         description="Corro - 3rd party consultation drafting letter, confirming address details for email, creating copies of relevant documents for consideration, specific explanation required if complex")
    comment10 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field11 = SelectField('Time Taken', choices=[(0.5, "0.5 hours"), (1, "1 hour"),(1.5, "1.5 hours")],coerce=float,validators=[DataRequired()],
                          description="Review 3rd party contentions, making files of same, consideration for inclusion in Material Statement of Fact and Draft FOI Determination")
    field12 = FloatField('Consultations', validators=[DataRequired()])

    comment12 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field13 = SelectField('Time Taken', choices=[(1, "1 hour"), (1.5, "1.5 hours"),(2, "2 hours"),(2.5,"2.5 hours"),(3,"3 hours")],coerce=float,validators=[DataRequired()],
                          description="Access Refusal for other grounds - Available in public register, Archives, National Film & Sound, etc.")
    comment13 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field14 = SelectField('Time Taken', choices=[(1.5, "1.5 hours"), (1.75, "1.75 hours"),(2, "2 hours")],coerce=float,validators=[DataRequired()],
                          description="Finalisation of Schedule of Documents, reflecting exemption grounds")
    comment14 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field15 = SelectField('Time Taken', choices=[(1, "1 hours"), (1.5, "1.5 hours"),(2, "2 hours")],coerce=float,validators=[DataRequired()],
                          description="Redaction of any information or sections of partially released documents")
    comment15 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field16 = SelectField('Time Taken', choices=[(1, "1 hour"), (1.5, "1.5 hours"),(2, "2 hours")],coerce=float,validators=[DataRequired()],
                          description="Converting partial or fully documents into 'printed' PDF versions (so inalterable, no metadata retained)")
    comment16 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field17 = SelectField('Time Taken', choices=[(1, "1 hour"), (2, "2 hours"),(3, "3 hours")],coerce=float,validators=[DataRequired()],
                          description="Final review of Draft FOI Decision, confirming findings of facts with Ops or Other Group")
    comment17 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field18 = SelectField('Time Taken', choices=[(0.5, "0.5 hours"), (1, "1 hour"),(1.5, "1.5 hours")],coerce=float,validators=[DataRequired()],
                          description="Collating Final FOI decision, all printed PDF documents with information regarding review & appeal rights, including 3rd parties' right to object if determination = to release")
    comment18 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])

    field19 = SelectField('Time Taken', choices=[(1, "1 hours"), (1.5, "1.5 hours"),(2, "2 hours")],coerce=float,validators=[DataRequired()],
                          description="Drafting briefings for executives regarding draft final decision")
    comment19 = TextAreaField('Say something', validators=[ Length(min=0, max=140)])


    result = FloatField('Total time', validators=[DataRequired()],render_kw={'readonly': True})
    submit_survey = SubmitField('Save')

    def __init__(self, original_survey_content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_survey_content = original_survey_content
    
   



    def validate(self):
        # Call the parent's validate method first
        if not super().validate():
            return False

        # Calculate the sum of field1, field2, and field3
        total = 0
        if self.field1.data:
            total += self.field1.data
        if self.field2.data:
            total += self.field2.data
        if self.field3.data:
            total += self.field3.data

        # Set the result field with the calculated total
        self.result.data = total

        return True

class EmptyForm(FlaskForm): 
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class SurveyForm(FlaskForm):
    survey_name = StringField('Name', validators=[DataRequired(),Length(min=0, max=140)])
    submit = SubmitField('Create')

class ExemptionForm(FlaskForm):
    exemption_name = SelectField('Exemption',
                                 choices=[("sss", "sss"), ("sss", "sss")],validators=[DataRequired()])
    exemption_instance = FloatField('Instances', validators=[DataRequired()])
    exemption_multiplier = SelectField('Multiplier', choices=[
        (0.1, 0.1),(0.2, 0.2),(0.3, 0.3),(0.4, 0.4),(0.5, 0.5),(0.6, 0.6),(0.7, 0.7),(0.8, 0.8),(0.9, 0.9)
        ],coerce=float,validators=[DataRequired()])
    exemption_time = SelectField('Time Taken', choices=[(2, "2 hours"), (3, "3 hours"),(4, "4 hours")],coerce=float,validators=[DataRequired()])
    submit_exemption = SubmitField('Add')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.exemption_instance.data = 7
        self.exemption_name.choices = self.load_exemptions()

    @staticmethod
    def load_exemptions():
        choices = []
        
        csv_file_path = os.path.join(current_app.root_path, 'static', 'dropdowns', 'exemptions.csv')
        
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                choices.append((row[0], row[1])) 
    
        return choices