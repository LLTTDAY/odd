import pandas as pd
import altair as alt

def feature_importance(homes, model):
    """Plot feature importances for RandomForestRegressors using homes vectors"""
    lst = homes.drop(columns=['vpu','v20pu','v19pu','pin']).columns
    lst2 = list(model.feature_importances_)
    df = pd.DataFrame(list(zip(lst, lst2)), 
                columns=['Name', 'val'])
    chart = alt.Chart(df.sort_values(by='val', ascending=False).head(25)).mark_bar().encode(
        x = alt.X('Name:N', sort='-y'),
        y = alt.Y('val:Q')
    )
    return chart


def aggregate_samples(test, number, size):
    """Make set of n non-overlapping samples of size s from the test set"""
    n = 0
    s = {}
    while n < number:
        s[n] = test.sample(size)
        n += 1
    return s


def aggregate_samples_2(test, number, size):
    """Make set of 1,000 non-overlapping samples from the test set"""
    n = 0
    s = {}
    while n < number:
        s[n] = test.sample(size).index
        n += 1
    return s


def aggregate_errors(model, y, tests):
    test_results = []
    for key,val in tests.items():
        tp = pd.DataFrame(y)
        test_results.append((key, sum(model.predict(val)), float(tp[tp.index.isin(val.index)].sum())))
    tr = pd.DataFrame(test_results, columns=['Sample','Actual','Predicted'])
    tr['Error'] = ( tr['Actual'] - tr['Predicted'] ) / tr['Actual']
    return tr


def aggregate_errors_2(y_pred, y_true, tests):
    test_results = []
    for key, val in tests.items():
        test_results.append((key, y_pred[y_pred.index.isin(val)].sum(), y_true[y_true.index.isin(val)].sum()))
    tr = pd.DataFrame(test_results, columns=['Sample','Predicted','Actual'])
    tr['Error'] = ( tr['Actual'] - tr['Predicted'] ) / tr['Actual']
    return tr


def plot_agg_error(tr):
    actual_point = alt.Chart(tr).mark_point(filled=True,color='lime').encode(
    y=alt.X('Actual:Q'),
    x=alt.Y('Sample:N')
    )
    predicted_point = alt.Chart(tr).mark_point(filled=True, color='orange').encode(
    y=alt.X('Predicted:Q'),
    x=alt.Y('Sample:N'),
    )
    (actual_point + predicted_point).display()