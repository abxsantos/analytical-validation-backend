
from modules.validation_analysis import Linearity

################
#  Test cases  #
################

# ordinary_least_squares_linear_regression: should return slope_pvalue, intercept_pvalue, r_squared, slope, intercept, stderr

# check_hypothesis: should return bool slope_is_significative, intercept_is_significative, r2_accepted

# breusch_pagan:  should return bool isHomokedastic and breusch_pagan_pvalue
# breusch_pagan: isHomokedastic = false, should use huber regression and remake the other old_tests


# anova_analysis: should return degrees_of_freedom_regression, sum_of_squares_regression, regression_mean_square, \
#                degrees_of_freedom_residual, sum_of_squares_residual, residual_mean_square, \
#                sum_of_squares_total, degrees_of_freedom, f_anova, p_anova


# check_dixon_outliers: should return a array of outliers and the non_outlier_analytical_data.
# If there's an outlier, redo the old_tests with the new non_outlier_analytical_data

# durbin_watson: should return a 0 < value < 4

# Example of inputs
analytical_data = [[0.188, 0.192, 0.203], [0.349, 0.346, 0.348], [0.489, 0.482, 0.492], [0.637, 0.641, 0.641],
                   [0.762, 0.768, 0.786], [0.931, 0.924, 0.925]]
volume_of_samples = 50.00
dilution_factor = [125.0, 62.5, 50.0, 35.71429, 31.25, 25.0]
mass_of_samples = [50.0, 50.1, 50.8]
number_of_replicas = 3
alpha = 0.05

linearity_analysis = Linearity(analytical_data, volume_of_samples, mass_of_samples,
                               number_of_replicas, dilution_factor, alpha)

def test_mean_result():
    assert (linearity_analysis.data_mean_calculation()) == [0.19433333333333333, 0.3476666666666666, 0.4876666666666667, 0.6396666666666667, 0.7719999999999999, 0.9266666666666667]

def test_standard_deviation_result():
    assert (linearity_analysis.data_std_calculation()) == [0.0077674534651540365, 0.0015275252316519481, 0.005131601439446889, 0.0023094010767585054, 0.012489995996796807, 0.0037859388972001857]

def test_concentration_calculation():
    assert (linearity_analysis.concentration_calculation()) == [[0.008, 0.008016, 0.008128], [0.016, 0.016032, 0.016256], [0.02, 0.02004, 0.02032], [0.027999996640000406, 0.028055996633280407, 0.02844799658624041], [0.032, 0.032064, 0.032512], [0.04, 0.04008, 0.04064]]

def test_flatten_axis_data():
    assert (linearity_analysis.flatten_axis_data()) == ([0.008, 0.008016, 0.008128, 0.016, 0.016032, 0.016256, 0.02, 0.02004, 0.02032, 0.027999996640000406, 0.028055996633280407, 0.02844799658624041, 0.032, 0.032064, 0.032512, 0.04, 0.04008, 0.04064], [0.188, 0.192, 0.203, 0.349, 0.346, 0.348, 0.489, 0.482, 0.492, 0.637, 0.641, 0.641, 0.762, 0.768, 0.786, 0.931, 0.924, 0.925])

def test_ordinary_least_squares_linear_regression():
    assert (linearity_analysis.ordinary_least_squares_linear_regression()) == (-2.3991789493457705e-05, 23.25038677191697, 0.4470350165979073, 2.813769707716701e-19, 0.9984023695562387, 0.994119943600169, 0.9343053999849873, [0.0020208976141576906, 0.0056488914258070455, 0.014044848107352348, -0.02298219656117806, -0.026726208937879414, -0.029934295574788772, 0.024016256351154064, 0.016086240880277436, 0.01957613258414065, -0.013986759702891538, -0.011288781205876397, -0.020402931726769657, 0.018011615088150412, 0.022523590334747712, 0.03010741706092901, 0.00100852091281467, -0.00785151002893858, -0.01987172662121217], 1.2726397502466964)

def test_anova_analysis():
    assert (linearity_analysis.anova_analysis()) == (1, 1.4795462222222224, 1.4795462222222224, 16, 0.3697542222222222, 0.023109638888888888, 1.1097920000000001, 17, 0.0012369221951155753, 0.9987639443389845)

def test_grubbs_critical_value_calculation():
    assert (linearity_analysis.grubbs_critical_value_calculation()) == 1.1543048513440384