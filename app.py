from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


@app.route('/test2')
def test2(chartID = 'test2', chart_type = 'column', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	title = {"text": 'Browser market shares. January, 2018'}
	xAxis = {"type": 'category'}
	yAxis = {"title": {"text": 'Total percent market share'}}
	series = [{"name": "Browsers", "colorByPoint": 'true', "data": [{"name": "Chrome", "y": 62.74, "drilldown": "Chrome"}]}]
	drilldown = {"series":[{"name": 'Chrome', "id": 'Chrome', "data": [["v65.0", 0.1], ["v64.0", 1.3]]}]}
	return render_template('test2.html', chartID=chartID, chart=chart, title=title, xAxis=xAxis, yAxis=yAxis, series=series, drilldown=drilldown)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080)
