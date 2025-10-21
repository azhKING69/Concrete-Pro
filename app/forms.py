# app/forms.py
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional
from ml_model.config import DESIGN_MIX_TABLE

# --- Form for Page 1: Predictor ---
class PredictionForm(FlaskForm):
    cement = FloatField('Cement (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    slag = FloatField('Blast Furnace Slag (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    fly_ash = FloatField('Fly Ash (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    water = FloatField('Water (kg/m³)', validators=[InputRequired(), NumberRange(min=100)])
    superplasticizer = FloatField('Superplasticizer (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    coarse_aggregate = FloatField('Coarse Aggregate (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    fine_aggregate = FloatField('Fine Aggregate (kg/m³)', validators=[InputRequired(), NumberRange(min=0)])
    age = FloatField('Curing Age (Days)', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Predict Strength')

# --- Form for Page 2: Recommender ---
class RecommenderForm(FlaskForm):
    grade_choices = [(grade, grade) for grade in DESIGN_MIX_TABLE.keys()]
    grade = SelectField('Select Concrete Grade',
                        choices=grade_choices,
                        default='M25')
    submit = SubmitField('Get Recommended Mix')

# --- Form for Page 3: Optimizer (Final Version) ---
class OptimizerForm(FlaskForm):
    # This is now a flexible numerical input
    strength = FloatField('Target Characteristic Strength (MPa, at 28 days)',
                          validators=[InputRequired(), NumberRange(min=5, max=100)],
                          default=30)

    # Optional additives with toggles
    use_slag = BooleanField('Include Blast Furnace Slag')
    slag = FloatField('Slag (kg/m³)', validators=[Optional(), NumberRange(min=0)], default=0)

    use_fly_ash = BooleanField('Include Fly Ash')
    fly_ash = FloatField('Fly Ash (kg/m³)', validators=[Optional(), NumberRange(min=0)], default=0)

    use_superplasticizer = BooleanField('Include Superplasticizer')
    superplasticizer = FloatField('Superplasticizer (kg/m³)', validators=[Optional(), NumberRange(min=0)], default=0)

    submit = SubmitField('Find Optimal Mix')