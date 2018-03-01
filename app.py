import datetime as dt
import numpy as np
import pandas as pd
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Belly_Button_Biodiversity.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
samples_metadata = Base.classes.samples_metadata
Otu = Base.classes.otu
samples = Base.classes.samples

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################



#################################################
# Flask Routes
#################################################

#Homepage
@app.route("/")

def homepage():
    return render_template("index.html")

#List of Sample Names

@app.route("/names")
def passengers():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(samples).statement

    # Create a dictionary from the row data and append to a list of all_passengers
    dataframe = pd.read_sql_query(results, session.bind)
    dataframe.set_index("otu_id", inplace = True)

    return jsonify(list(dataframe.columns))
    console.log(jsonify(list(dataframe.columns)))
#OTU Descriptions 

@app.route("/otu")
def otu():
    results=session.query(Otu.lowest_taxonomic_unit_found).all()
    otu_lists = list(np.ravel(results))
    return jsonify(otu_lists)

@app.route('/metadata/<sample>')

def metadata(sample):
    samp = [samples_metadata.AGE, samples_metadata.BBTYPE, samples_metadata.ETHNICITY, 
    samples_metadata.GENDER
    samples_metadata.LOCATION, samples_metadata.SAMPLEID]

    results = session.query(*samp).filter(samples_metadata.SAMPLEID==sample[3:]).all()
        def row2dict():
            d = {}
            for column in results.columns:
                results[column.name] = str(getattr(row, column.name))

            return jsonify(d)

    #convert to dict
    #return json
@app.route('/wfreq/<sample>')
    results = session.query(samples_metadate.WFREQ).filter(samples_metadata.SAMPLEID==sample[3:]).all()
    dataframe = pd.read_sql_query(results, session.bind)
    dataframe.set_index("SAMPLEID", inplace = True)
    return jsonify(list(dataframe.columns))
    console.log(jsonify(list(dataframe.columns)))


@app.route('/samples/<sample>')
def sample2():

if __name__ == '__main__':
    app.run(debug=True)

