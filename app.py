from flask import Flask,render_template,url_for
import pandas as pd


app = Flask(__name__,template_folder="templates")

@app.route('/')
def index():
    data = pd.read_excel("Book1.xlsx")

    context = {
        "record_count":data.shape[0],
        "dataset_name":"Education",
        "project_objective":"analyze the education industry data",
        "variable_count": data.size,
        "data_type":"",
        "data_structure":"",
        "exploration_insights":"",
        "exploration_content":"",
        "analysis_techniques":"",
        "analysis_findings":"The analysis showed that the company`s costs has been raised by 20% this year.",
        "author_or_organization":"Azeem"
    }

    return render_template("report_template.html",**context)

if __name__ == "__main__":
    app.run(debug=True)