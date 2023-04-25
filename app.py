from flask import Flask, render_template, jsonify
import pandas as pd
from api_ga4 import sample_run_report

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    # création de l'objet DataFrame
    response = sample_run_report()
    rows = response.rows

    data = []
    for row in rows:
        row_dict = {}
        dimensions = row.dimension_values
        for i, dimension in enumerate(dimensions):
            row_dict[f"dimension_{i + 1}"] = dimension.value
        metrics = row.metric_values
        for i, metric in enumerate(metrics):
            row_dict[f"metric_{i + 1}"] = metric.value
        data.append(row_dict)

    df = pd.DataFrame(data)
    # 1ère visualisation
    df1 = df.loc[:, ['dimension_1', 'metric_1', 'metric_3']]
    df1[['metric_1', 'metric_3']] = df1[['metric_1', 'metric_3']].astype(int)
    df1 = df1.sort_values(by='dimension_1')
    df1 = df1.groupby('dimension_1')[['metric_1', 'metric_3']].sum().reset_index()

    # 2ème visualisation
    df2 = df.loc[:, ['dimension_2', 'metric_5']]
    df2["metric_5"] = df2["metric_5"].astype(int)
    df2 = df2.groupby('dimension_2')['metric_5'].sum().reset_index()

    # 3ème visualisation
    df3 = df.loc[:, ['dimension_4', 'metric_5']]
    df3["metric_5"] = df3["metric_5"].astype(int)
    df3 = df3.groupby('dimension_4')['metric_5'].sum().reset_index()

    # 4ème visualisation
    df4 = df.loc[:, ['dimension_3', 'metric_4']]
    df4["metric_4"] = df4["metric_4"].astype(int)
    df4 = df4.groupby('dimension_3')['metric_4'].sum().reset_index()

    # 5ème visualisation
    df5 = df.loc[:, ['metric_9', 'metric_6', 'dimension_1']]
    df5[['metric_9', 'metric_6']] = df5[['metric_9', 'metric_6']].astype(float)
    df5[['metric_9', 'metric_6']] = df5[['metric_9', 'metric_6']].round().astype(int)
    df5 = df5.sort_values(by='dimension_1')
    df5 = df5.groupby('dimension_1')[['metric_9', 'metric_6']].sum().reset_index()

    # 6ème visualisation
    df6 = df.loc[:, ['metric_2', 'metric_10', 'dimension_1']]
    df6[['metric_2', 'metric_10']] = df6[['metric_2', 'metric_10']].astype(float)
    df6['metric_10'] = df6['metric_10'] / 60
    df6[['metric_2', 'metric_10']] = df6[['metric_2', 'metric_10']].round().astype(int)
    df6 = df6.sort_values(by='dimension_1')
    df6 = df6.groupby('dimension_1')[['metric_2', 'metric_10']].sum().reset_index()

    # 7ème visualisation
    df7 = df.loc[:, ['dimension_5', 'metric_5']]
    df7["metric_5"] = df7["metric_5"].astype(int)
    df7 = df7.groupby('dimension_5')['metric_5'].sum().reset_index()
    df7 = df7.nlargest(7, 'metric_5')

    # 8ème visualisation
    df8 = df.loc[:, ['dimension_1', 'metric_2', 'metric_4', 'metric_7']]
    df8[['metric_2', 'metric_4', 'metric_7']] = df8[['metric_2', 'metric_4', 'metric_7']].astype(float)
    df8[['metric_2', 'metric_4', 'metric_7']] = df8[['metric_2', 'metric_4', 'metric_7']].round().astype(int)
    df8 = df8.groupby('dimension_1')[['metric_2', 'metric_4', 'metric_7']].sum().reset_index()

    # Traiter les données et les formater pour Chart.js
    chart_data = {
        'labels': df1['dimension_1'].values.tolist(),
        'datasets': [{
            'label': "Nombre d'utilisateurs",
            'data': df1['metric_1'].values.tolist(),
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 1
        },
            {
                'label': "Nouveaux utilisateurs",
                'data': df1['metric_3'].values.tolist(),
                'backgroundColor': 'rgba(153, 102, 255, 0.2)',
                'borderColor': 'rgba(153, 102, 255, 1)',
                'borderWidth': 1
            }
        ]
    }
    chart_data2 = {
        'labels': df2['dimension_2'].values.tolist(),
        'datasets': [{
            'label': 'Langue la plus utilisée',
            'data': df2['metric_5'].values.tolist(),
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(201, 203, 180, 0.2)',
                'rgba(253, 150, 238, 0.2)',
                'rgba(144, 200, 144, 0.2)'
            ],
            'borderColor': [
                'rgb(255, 99, 132)',
                'rgb(153, 102, 255)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(255, 159, 64)',
                'rgb(201, 203, 180)',
                'rgb(253, 150, 238)',
                'rgb(144, 200, 144)'
            ],
            'hoverOffset': 2,
            'borderWidth' : 1
        }]

    }
    chart_data3 = {
        'labels': df3['dimension_4'].values.tolist(),
        'datasets': [{
            'label': "Catégorie d'appareils",
            'data': df3['metric_5'].values.tolist(),
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            'borderColor': [
                'rgb(255, 99, 132)',
                'rgb(153, 102, 255)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)'
            ],
            'hoverOffset': 2,
            'borderWidth': 1
        }]
    }
    chart_data4 = {
        'labels': df4['dimension_3'].values.tolist(),
        'datasets': [{
                'label': 'Nombre unique de vues',
                'data': df4['metric_4'].values.tolist(),
                'backgroundColor': 'rgba(153, 102, 255, 0.2)',
                'borderColor' : 'rgb(153, 102, 255)',
                'borderWidth': 1
            }]
    }
    chart_data5 = {
        'labels': df5['dimension_1'].values.tolist(),
        'datasets': [{
            'type' : 'bar',
            'label': 'Session par utilisateur',
            'data': df5['metric_9'].values.tolist(),
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgb(255, 99, 132)',
            'borderWidth': 1
        },
            {
            'type' : 'line',
            'label': "Taux d'engagement",
            'data': df5['metric_6'].values.tolist(),
            'backgroundColor': 'rgba(255, 159, 64, 0.2)',
            'borderColor': 'rgb(255, 159, 64)',
            'borderWidth': 1
            }
        ]
    }
    chart_data6 = {
        'labels': df6['dimension_1'].values.tolist(),
        'datasets': [{
            'label': 'Sessions',
            'data': df6['metric_2'].values.tolist(),
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgb(255, 99, 132)',
            'borderWidth': 1,
            'pointBackgroundColor': 'rgb(255, 99, 132)',
            'pointHoverBorderColor': 'rgb(255, 99, 132)'
        }, {
            'label': 'Durée moyenne de sessions (min)',
            'data': df6['metric_10'].values.tolist(),
            'backgroundColor': 'rgba(255, 205, 86, 0.2)',
            'borderColor': 'rgb(255, 205, 86)',
            'borderWidth': 1,
            'pointBackgroundColor': 'rgb(255, 205, 86)',
            'pointHoverBorderColor': 'rgb(255, 205, 86)'

        }]
    }
    chart_data7 = {
        'labels': df7['dimension_5'].values.tolist(),
        'datasets': [{
            'label': 'Utilisateurs',
            'data': df7['metric_5'].values.tolist(),
            'backgroundColor':[
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
           ],
            'borderColor':[
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            'borderWidth': '1'
        }]
    }
    chart_data8 = {
        'labels': df8['dimension_1'].values.tolist(),
        'datasets': [{
            'label': 'Sessions',
            'data': df8['metric_2'].values.tolist(),
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 1
        },
            {
                'label': "Vues de page d'écran",
                'data': df8['metric_4'].values.tolist(),
                'backgroundColor': 'rgba(80, 60, 180, 0.2)',
                'borderColor': 'rgba(80, 60, 180, 1)',
                'borderWidth': 1
            },
            {
                'label': "Taux de rebond",
                'data': df8['metric_7'].values.tolist(),
                'backgroundColor': 'rgba(10, 11, 255, 0.2)',
                'borderColor': 'rgba(10, 11, 255, 1)',
                'borderWidth': 1
            }]
    }

    return jsonify(chart_data, chart_data2, chart_data3, chart_data4, chart_data5, chart_data6, chart_data7, chart_data8)

if __name__ == "__main__":
    app.run(debug=True)
