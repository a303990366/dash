import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
df_model1 = pd.read_csv('C:/Users/x5748/Downloads/LDA/new/topicmodel_day_article.csv')
#df_model2 = pd.read_csv('C:/Users/x5748/Downloads/flask_for_reaction_score.csv')
df_model3 = pd.read_csv('C:/Users/x5748/Downloads/LDA/new/topicmodel_month_article.csv')
df_model4 = pd.read_csv('C:/Users/x5748/Downloads/LDA/new/topicmodel_month_comment.csv')
df_model5 = pd.read_csv('C:/Users/x5748/Downloads/LDA/new/revelance_score.csv')
df = pd.read_csv('C:/Users/x5748/Downloads/flask_for_reaction_score.csv')

def generate_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#表格長寬
table_length=['600px','180px']

app.layout =html.Div(style={'backgroundColor': '#000000','min-height':'900px'},children=[
    html.Div(style={'backgroundColor': '#000000'},children=[
    #header
    html.H1(children='WOAD - Weather Opinion Analysis Dashboard(v1)', style={
        'textAlign': 'center',
        'color':'#2894FF',
        'font-size':'30px',
        'font-weight':'bold'
    }),
    html.Div(style={'background':'#EA0000'},children=[
    #-------------------------------------left------------------------------
    html.Div(style={
        #'margin-left':'15px',
        'color':'#D9B300',
        'background':'#000000',#'#FFBB73',#之後改掉
        #'width':table_length[0],
        #'height':'650px',
        'float':'left',
        'font-weight':'bold'},children=['模組01-每日媒體氣象新聞主題之發覺(前五名)',
    dash_table.DataTable(
        data=df_model1.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_model1.columns],
        style_cell_conditional=[
            {
                'textAlign': 'left',
                'vertical-align':'middle','vertical-align':'middle'
            }],
        style_header={'backgroundColor': '#2894FF'},
        style_cell={
        'backgroundColor': '#3C3C3C',
        'color': 'white',
        #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
        },
        page_action='none',
        fixed_rows={'headers': True},
        style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
    html.Div(children='模組02-每日民眾氣象輿情主題之發覺(前五名)', style={
        #'margin-left':'10px',
        'color':'#D9B300',
        'font-weight':'bold'}),
     #第二張表
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_cell_conditional=[
            {
                'textAlign': 'left',
                'vertical-align':'middle','vertical-align':'middle'
            }],
        style_header={'backgroundColor': '#2894FF'},
        style_cell={
        'backgroundColor': '#3C3C3C',
        'color': 'white',
        #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
        },
        page_action='none',
        fixed_rows={'headers': True},
        style_table={'width':table_length[0],'height': table_length[1], 'overflowY': 'auto'}),
    #第三張表
    html.Div(children='模組03-每月媒體氣象新聞主題之發覺(前五名)', style={
        'color':'#D9B300',
        'font-weight':'bold',
        #'margin-left':'10px'
    }),
    dash_table.DataTable(
        data=df_model3.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_model3.columns],
        style_cell_conditional=[
            {
                'textAlign': 'left',
                'vertical-align':'middle','vertical-align':'middle'
            }],
        style_header={'backgroundColor': '#2894FF'},
        style_cell={
        'backgroundColor': '#3C3C3C',
        'color': 'white',
        #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
        },
        page_action='none',
        fixed_rows={'headers': True},
        style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
                                       #]),
        html.Div(children='© IF.Lab. All rights reserved. ', style={
        'color':'#E63F00',
        'font-weight':'bold',
        'margin-top':'50px'})
        ]),
    #----------------------------------center-------------------------------------
    html.Div(style={
        'background':'#000000',#之後改掉
        #'width':'400px',
        #'height':'600px',
        'position':'absolute',
        'left':'35%',
        'color':'#D9B300',
        'font-weight':'bold'},children=['模組04-每月民眾氣象輿情主題之發覺(前五名)',
        dash_table.DataTable(
            data=df_model4.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_model4.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
        html.Div(children='模組05-每月媒體新聞主題與民眾輿情主題之關聯性分析(前五名)', style={
            #'margin-left':'10px',
            'color':'#D9B300',
            'font-weight':'bold'}),
         #第五張表
        dash_table.DataTable(
            data=df_model5.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_model5.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height': table_length[1], 'overflowY': 'auto'}),
        html.Div(children='模組06-每日民眾對於氣象預報之輿情反應分析', style={
            'color':'#D9B300',
            'font-weight':'bold',
            #'margin-left':'10px'
        }),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
        html.Div(children='© Contributors:黃福銘,趙恭岳,周柏佳,張育誠,黃昭元,賴祐全,林庭嘉, 黃任杰, 彭鈺湄', style={
        'color':'#E63F00',
        'font-weight':'bold',
        'margin-top':'50px'})
        ]),                        
                                       
    
    
    #-------------------------right--------------------------------------
    html.Div(style={
        'background':'#000000',#之後改掉
        #'width':'400px',
        #'height':'600px',
        #'line-height':'100px',
        #'text-align':'center',
        'float':'right',
        'color':'#D9B300',
        'font-weight':'bold'},children=['模組07-民眾對於特定天災假期之輿情反應分析',
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
        html.Div(children='模組08-每月民眾氣象輿情之主要意見領袖追蹤', style={
            #'margin-left':'10px',
            'color':'#D9B300',
            'font-weight':'bold'}),
         #第八張表
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height': table_length[1], 'overflowY': 'auto'}),
        html.Div(children='模組09-每日中央氣象局綜合好感度解析', style={
            'color':'#D9B300',
            'font-weight':'bold',
            #'margin-left':'10px'
        }),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {
                    'textAlign': 'left',
                    'vertical-align':'middle','vertical-align':'middle'
                }],
            style_header={'backgroundColor': '#2894FF'},
            style_cell={
            'backgroundColor': '#3C3C3C',
            'color': 'white',
            #'minWidth': '100px', 'width': '180px', 'maxWidth': '100px'
            },
            page_action='none',
            fixed_rows={'headers': True},
            style_table={'width':table_length[0],'height':table_length[1], 'overflowY': 'auto'}),
        html.Div(children='© 東吳大學巨量資料管理學院', style={
        'color':'#E63F00',
        'font-weight':'bold',
        'textAlign': 'right',
        'margin-top':'50px'})
        ]),  
    ])
]) 
])#max
    

    #分層
if __name__ == '__main__':
    app.run_server(debug=True)
