# app/routes.py
from flask import Blueprint, render_template, request, flash
from app.forms import PredictionForm, RecommenderForm, OptimizerForm
from ml_model.predict import predict_strength
from ml_model.recommender import get_mix_recommendation
from ml_model.optimize import run_optimizer
from ml_model.config import RECOMMENDER_MATERIAL_PRICES, OPTIMIZER_MATERIAL_PRICES

main = Blueprint('main', __name__)

# --- NEW Route for Homepage ---
@main.route('/')
def home():
    """Route for the new homepage."""
    return render_template('home.html', title='Welcome')

# --- Route for Page 1: Predictor (Moved to /predict) ---
@main.route('/predict', methods=['GET', 'POST'])
def predict(): # Renamed function for clarity
    form = PredictionForm()
    prediction = None
    if form.validate_on_submit():
        try:
            features = [
                form.cement.data, form.slag.data, form.fly_ash.data,
                form.water.data, form.superplasticizer.data,
                form.coarse_aggregate.data, form.fine_aggregate.data,
                form.age.data
            ]
            prediction = predict_strength(features)
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
    # Render index.html, but the route is now /predict
    return render_template('index.html', title='Strength Predictor', form=form, prediction=prediction)

# --- Route for Page 2: Recommender ---
@main.route('/recommend', methods=['GET', 'POST'])
def recommend():
    form = RecommenderForm()
    results = None
    if request.method == 'GET':
        results = get_mix_recommendation(form.grade.default)
    if form.validate_on_submit():
        try:
            results = get_mix_recommendation(form.grade.data)
            if not results:
                flash(f'Could not find data for grade {form.grade.data}.', 'warning')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')

    return render_template('recommender.html',
                           title='Mix Recommender',
                           form=form,
                           results=results,
                           prices=RECOMMENDER_MATERIAL_PRICES)

# --- Route for Page 3: Optimizer ---
@main.route('/optimize', methods=['GET', 'POST'])
def optimize():
    form = OptimizerForm()
    results = None
    if form.validate_on_submit():
        try:
            target_strength = form.strength.data
            fixed_slag = form.slag.data if form.use_slag.data else 0
            fixed_fly_ash = form.fly_ash.data if form.use_fly_ash.data else 0
            fixed_superplasticizer = form.superplasticizer.data if form.use_superplasticizer.data else 0

            results = run_optimizer(
                target_strength,
                fixed_slag, fixed_fly_ash, fixed_superplasticizer
            )

            if results and results.get('success'):
                if results.get('was_fine_tuned'):
                    flash('ML optimizer successfully fine-tuned the baseline mix!', 'success')
                else:
                    flash('ML optimizer could not find a better mix, returning the reliable baseline from the design table.', 'info')
            elif results:
                 flash(f'Optimization failed: {results.get("message")}', 'danger')

        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')

    return render_template('optimizer.html',
                           title='ML Mix Optimizer',
                           form=form,
                           results=results,
                           prices=OPTIMIZER_MATERIAL_PRICES)